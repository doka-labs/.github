//! Radial cubic connections in the normalized design coordinate system.

/// A two-dimensional design coordinate.
#[derive(Clone, Copy, Debug)]
pub(super) struct Point(pub f64, pub f64);

impl Point {
    /// Euclidean distance in the unscaled design plane.
    fn distance(self, other: Self) -> f64 {
        (self.0 - other.0).hypot(self.1 - other.1)
    }
}

/// One cubic whose endpoint handles are radial to the connected circles.
#[derive(Debug)]
pub(super) struct Curve(pub [Point; 4]);

impl Curve {
    /// Clip a cubic to circle boundaries; overlapping circles have no visible connection.
    pub(super) fn between(
        source: (Point, f64),
        target: (Point, f64),
        controls: [Point; 2],
    ) -> Option<Self> {
        let (a, ra) = source;
        let (b, rb) = target;
        let distance = a.distance(b);

        if !distance.is_finite() || ra <= 0.0 || rb <= 0.0 || distance <= ra + rb {
            return None;
        }

        let c1 = orient(controls[0], a, b);
        let c2 = orient(controls[1], b, a);

        // A radial tangent requires a handle outside its disk, even for close neighbors.
        let c1 = extend(a, c1, ra);
        let c2 = extend(b, c2, rb);
        let curve = Self([boundary(a, c1, ra), c1, c2, boundary(b, c2, rb)]);

        if (0..=1000).all(|index| {
            let point = curve.point(index as f64 / 1000.0);
            point.distance(a) >= ra - 1e-6 && point.distance(b) >= rb - 1e-6
        }) {
            return Some(curve);
        }

        // Arbitrary custom layouts can make a fitted port curve reenter a disk.
        // The line between disjoint circle centers is the exact safe radial solution.
        Some(Self([
            boundary(a, b, ra),
            boundary(a, b, ra),
            boundary(b, a, rb),
            boundary(b, a, rb),
        ]))
    }

    /// Evaluate the cubic for boundary verification and deterministic regression tests.
    fn point(&self, t: f64) -> Point {
        let [a, b, c, d] = self.0;
        let u = 1.0 - t;

        Point(
            u.powi(3) * a.0 + 3.0 * u * u * t * b.0 + 3.0 * u * t * t * c.0 + t.powi(3) * d.0,
            u.powi(3) * a.1 + 3.0 * u * u * t * b.1 + 3.0 * u * t * t * c.1 + t.powi(3) * d.1,
        )
    }

    /// Scale the complete curve so non-square canvases retain ellipse-boundary alignment.
    pub(super) fn path(&self, sx: f64, sy: f64) -> String {
        let [a, b, c, d] = self.0.map(|point| Point(point.0 * sx, point.1 * sy));

        format!(
            "M{:.6} {:.6}C{:.6} {:.6} {:.6} {:.6} {:.6} {:.6}",
            a.0, a.1, b.0, b.1, c.0, c.1, d.0, d.1
        )
    }
}

/// Turn backward handles toward the neighbor while preserving their bend side.
fn orient(control: Point, center: Point, other: Point) -> Point {
    let Point(dx, dy) = Point(other.0 - center.0, other.1 - center.1);
    let Point(vx, vy) = Point(control.0 - center.0, control.1 - center.1);

    if vx * dx + vy * dy > 0.0 {
        return control;
    }

    let side = if -dy * vx + dx * vy >= 0.0 { 1.0 } else { -1.0 };

    Point(
        center.0 + 0.35 * dx - side * 0.18 * dy,
        center.1 + 0.35 * dy + side * 0.18 * dx,
    )
}

/// Preserve the handle ray while guaranteeing a nonzero outward endpoint tangent.
fn extend(center: Point, control: Point, radius: f64) -> Point {
    if center.distance(control) > radius {
        control
    } else {
        boundary(center, control, radius + 1.0)
    }
}

/// Intersect a center-to-handle ray with its circle.
fn boundary(center: Point, control: Point, radius: f64) -> Point {
    let factor = radius / center.distance(control);

    Point(
        center.0 + (control.0 - center.0) * factor,
        center.1 + (control.1 - center.1) * factor,
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn boundary_tangents_and_samples_stay_outside_circles() {
        let a = Point(900.0, 465.0);
        let b = Point(470.0, 360.0);

        let curve = Curve::between(
            (a, 61.0),
            (b, 48.0),
            [Point(756.866, 321.866), Point(675.0, 360.0)],
        )
        .unwrap();

        assert!((curve.0[0].distance(a) - 61.0).abs() < 1e-9);
        assert!((curve.0[3].distance(b) - 48.0).abs() < 1e-9);

        for index in 0..=1000 {
            let p = curve.point(index as f64 / 1000.0);
            assert!(p.distance(a) >= 61.0 - 1e-9 && p.distance(b) >= 48.0 - 1e-9);
        }
    }

    #[test]
    fn overlapping_and_coincident_circles_do_not_emit_invalid_paths() {
        let a = (Point(0.0, 0.0), 20.0);
        let controls = [Point(0.0, 0.0), Point(10.0, 10.0)];

        let coincident = Curve::between(a, a, controls);
        let overlapping = Curve::between(a, (Point(10.0, 0.0), 20.0), controls);

        assert!(coincident.is_none());
        assert!(overlapping.is_none());
    }
}
