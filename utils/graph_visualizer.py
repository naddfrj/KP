from pyvis.network import Network


def visualize_graph(G):

    net = Network(
        height="900px",
        width="100%",
        bgcolor="white",
        font_color="black",
        directed=False
    )

    # ==========================
    # NODE
    # ==========================

    for node, data in G.nodes(data=True):

        if data.get("type") == "peneliti":

            net.add_node(
                node,
                label=data.get("label"),
                title=data.get("title"),
                size=data.get("size"),
                shape="circularImage",
                image=data.get("image"),   # sekarang berisi Base64
                color=data.get("color")
            )

        else:

            net.add_node(
                node,
                label=data.get("label"),
                title=data.get("title"),
                size=data.get("size"),
                shape="dot",
                color=data.get("color")
            )

    # ==========================
    # EDGE
    # ==========================

    for source, target in G.edges():

        net.add_edge(
            source,
            target
        )

    # ==========================
    # Layout
    # ==========================

    net.barnes_hut(
        gravity=-18000,
        central_gravity=0.08,
        spring_length=220,
        spring_strength=0.03,
        damping=0.09
    )

    # Tidak perlu set_options()

    net.save_graph("graph.html")