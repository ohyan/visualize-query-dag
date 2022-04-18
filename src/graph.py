from typing import Dict

from graphviz import Digraph


def create_dependencies_graph(dependencies: Dict):
    # draw graph
    graph = Digraph()
    graph.attr('node', shape='box')
    with graph.subgraph(name='querys') as c:
        c.attr(color='blue', label='querys')
        for name, refs in dependencies.items():
            for ref in refs:
                c.node(name, style='bold, filled' if name=='main' else 'solid, filled', fillcolor='#FFFFFF' if name=='main' else '#80CBC4')
                c.node(ref, style='solid, filled', fillcolor='#81C784' if '.' in ref else '#80CBC4')
                c.edge(name, ref)
    return graph
