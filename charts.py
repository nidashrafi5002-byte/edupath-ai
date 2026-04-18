import plotly.graph_objects as go

def donut_chart(value: float, label: str, color: str = "#4f46e5", max_val: float = 100):
    """Circular donut chart showing a percentage or score."""
    pct = min(value / max_val * 100, 100)
    remaining = 100 - pct

    if pct >= 70:   arc_color = "#22c55e"
    elif pct >= 45: arc_color = "#f59e0b"
    else:           arc_color = "#ef4444"

    if color != "#4f46e5":
        arc_color = color

    fig = go.Figure(go.Pie(
        values=[pct, remaining],
        hole=0.72,
        marker_colors=[arc_color, "rgba(255,255,255,0.05)"],
        textinfo="none",
        hoverinfo="skip",
        sort=False,
    ))

    fig.update_layout(
        showlegend=False,
        margin=dict(t=10, b=10, l=10, r=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        annotations=[dict(
            text=f"<b>{value:.0f}%</b><br><span style='font-size:11px;color:#a5b4fc'>{label}</span>",
            x=0.5, y=0.5,
            font=dict(size=20, color="white", family="Arial"),
            showarrow=False,
        )],
        height=200,
        width=200,
    )
    return fig


def gauge_chart(value: float, label: str, max_val: float = 100):
    """Half-circle gauge chart."""
    if value >= 70:   bar_color = "#22c55e"
    elif value >= 45: bar_color = "#f59e0b"
    else:             bar_color = "#ef4444"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={"suffix": "%", "font": {"color": "white", "size": 28}},
        title={"text": label, "font": {"color": "#a5b4fc", "size": 13}},
        gauge={
            "axis": {"range": [0, max_val], "tickcolor": "#444", "tickfont": {"color": "#888"}},
            "bar": {"color": bar_color, "thickness": 0.25},
            "bgcolor": "rgba(255,255,255,0.05)",
            "bordercolor": "rgba(255,255,255,0.1)",
            "steps": [
                {"range": [0, max_val * 0.45], "color": "rgba(239,68,68,0.1)"},
                {"range": [max_val * 0.45, max_val * 0.70], "color": "rgba(245,158,11,0.1)"},
                {"range": [max_val * 0.70, max_val], "color": "rgba(34,197,94,0.1)"},
            ],
            "threshold": {"line": {"color": "white", "width": 2}, "value": value},
        }
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "white"},
        margin=dict(t=40, b=10, l=30, r=30),
        height=220,
    )
    return fig


def bar_breakdown(labels: list, values: list, colors: list = None):
    """Horizontal bar chart for breakdowns like principal vs interest."""
    if not colors:
        colors = ["#4f46e5", "#7c3aed", "#06b6d4", "#22c55e", "#f59e0b"]

    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation="h",
        marker=dict(
            color=colors[:len(labels)],
            line=dict(color="rgba(255,255,255,0.1)", width=1)
        ),
        text=[f"{v:.1f}%" for v in values],
        textposition="outside",
        textfont=dict(color="white", size=12),
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "white"},
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 120]),
        yaxis=dict(showgrid=False, tickfont=dict(size=13)),
        margin=dict(t=10, b=10, l=10, r=60),
        height=160,
        bargap=0.3,
    )
    return fig
