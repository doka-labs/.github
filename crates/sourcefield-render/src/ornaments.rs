//! Approved SOURCEFIELD node ornaments, independent from labels and graph geometry.

use std::fmt::Write as _;

use sourcefield_core::{Node, NodeKind, ProfileState};

use super::{Palette, node_color, path};

/// Render local ornaments without introducing a transform around stable labels.
pub(super) fn render(output: &mut String, node: &Node, state: &ProfileState, p: Palette) {
    if node.kind == NodeKind::Domain {
        organization(output, node, state, p);

        return;
    }

    let radius = node.radius;
    let color = node_color(node, p);

    // Sibling transforms preserve opposite motion instead of canceling nested rotations.
    let _ = write!(
        output,
        "<g class=\"rotate\" data-project-ring=\"outer\"><circle r=\"{radius}\" \
         fill=\"none\" stroke=\"{color}\" stroke-opacity=\".4\" stroke-dasharray=\"3 11\"/>\
         <circle cx=\"{radius}\" r=\"3\" fill=\"{color}\" filter=\"url(#glow)\"/></g>\
         <g class=\"rotate reverse\" data-project-ring=\"middle\"><circle r=\"{}\" \
         fill=\"none\" stroke=\"{color}\" stroke-opacity=\".4\" stroke-dasharray=\"34 120\"/></g>",
        (radius - 8.0).max(1.0)
    );

    let _ = write!(
        output,
        "<circle r=\"{}\" fill=\"{}\" stroke=\"{color}\" stroke-opacity=\".65\"/>",
        (radius - 16.0).max(1.0),
        p.surface
    );

    let glyph = match node.visual.as_deref() {
        Some("lab") => "M-17 -12H17V14H-17ZM-17 -4H17M-8 -12V14",
        _ => "M0 -23L20 -11V12L0 24L-20 12V-11ZM-20 -11L0 0L20 -11M0 0V24",
    };

    path(output, glyph, color, ".95", "");
}

/// Center the inner orbit between the 40-unit core ring and the outer package orbit.
fn organization(output: &mut String, node: &Node, state: &ProfileState, p: Palette) {
    let radius = node.radius;
    let inner = (40.0 + radius) / 2.0;
    let _ = write!(
        output,
        "<g class=\"rotate reverse\" data-ring=\"organization-outer\"><circle \
         r=\"{radius}\" fill=\"none\" stroke=\"{}\" stroke-opacity=\".4\" \
         stroke-dasharray=\"2 10\"/></g><g class=\"rotate\" \
         data-ring=\"organization-inner\"><circle r=\"{inner}\" fill=\"none\" \
         stroke=\"{}\" stroke-opacity=\".26\" stroke-dasharray=\"34 120\"/></g>\
         <circle r=\"40\" fill=\"none\" stroke=\"{}\" stroke-opacity=\".30\"/>\
         <g transform=\"scale(0.49)\" data-glyph=\"organization-data\"><path \
         d=\"M0 -65 L56 -32 L56 32 L0 65 L-56 32 L-56 -32Z\" fill=\"{}\" \
         fill-opacity=\".92\" stroke=\"url(#organization-gradient)\" stroke-width=\"2.4\"/>\
         <path d=\"M-30 -14 H30 M-30 0 H30 M-30 14 H30\" fill=\"none\" stroke=\"{}\" \
         stroke-opacity=\".85\" stroke-width=\"2\"/>",
        p.amber, p.blue, p.amber, p.surface, p.blue
    );
    for y in [-14, 0, 14] {
        let _ = write!(
            output,
            "<circle cx=\"-36\" cy=\"{y}\" r=\"2.7\" fill=\"{}\"/>",
            p.amber
        );
    }

    output.push_str("</g>");
    let count = state
        .nodes
        .iter()
        .filter(|item| item.kind == NodeKind::Package && item.show_in_readme)
        .count();

    for index in 0..count {
        let angle = std::f64::consts::TAU * index as f64 / count as f64 - 1.05;
        let x = angle.cos() * f64::from(radius);
        let y = angle.sin() * f64::from(radius);
        let delay = -(index as f64 * 0.65);
        let color = if index * 2 < count { p.blue } else { p.amber };

        let _ = write!(
            output,
            "<g transform=\"translate({x:.3} {y:.3})\" \
             data-signal-delay=\"{delay:.2}\" \
             class=\"signal\" data-satellite=\"nuget-package\"><path \
             d=\"M0 -4 L3.5 -2 L3.5 2 L0 4 L-3.5 2 L-3.5 -2Z\" fill=\"{}\" \
             stroke=\"{color}\" stroke-width=\"1\"/><circle r=\"1\" fill=\"{color}\"/></g>",
            p.surface
        );
    }
}
