import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import spacy
import re

def build_Kgraph(entity_pairs):
    nlp = spacy.load('en_core_web_sm')

    source = [i[1] for i in entity_pairs]

    for x in source:
        entity_pairs.extend([[x,"Address","has"]])


    source = [i[1] for i in entity_pairs]

    target = [i[0] for i in entity_pairs]

    relations = [i[2] for i in entity_pairs]

    kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})

    G=nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())

    return G

def show_KG(G):

    plt.figure(figsize=(10,10))

    pos = nx.spring_layout(G)
    nx.draw_spring(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues)
    plt.show()

def get_city(G):
    return list(nx.neighbors(G,"CITY"))