import networkx as nx

def build_graph(iocs):
    g=nx.Graph()
    for i in iocs:
        g.add_node(i.normalized,type=i.ioc_type,risk=i.risk,severity=i.severity)
    for a in iocs:
        for b in iocs:
            if a is b: continue
            if a.source==b.source and a.tactic and a.tactic==b.tactic:
                g.add_edge(a.normalized,b.normalized,relation="shared-source/tactic")
    return g
