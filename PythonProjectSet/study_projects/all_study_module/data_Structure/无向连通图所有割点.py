# -*- coding: utf-8 -*-
# @CreateTime : 2023/11/8 008 17:18
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/无向连通图所有割点.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

def find_articulation_points(graph):
    n = len(graph)
    visited = [False] * n
    low = [float('inf')] * n
    disc = [float('inf')] * n
    parent = [-1] * n
    articulation_points = []

    def dfs(u, time):
        children = 0
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1

        for v in graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                dfs(v, time)
                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    articulation_points.append(u)
                elif parent[u] != -1 and low[v] >= disc[u]:
                    articulation_points.append(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    dfs(0, 0)
    return articulation_points


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3, 5],
    5: [2, 4]
}

print(find_articulation_points(graph))


"""
C语言版本：
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 1000

int n, m;
int head[MAXN], next[MAXN * 2], to[MAXN * 2];
int dfn[MAXN], low[MAXN], cut[MAXN];
int stack[MAXN], top;
int bridge_cnt;

void add_edge(int u, int v) {
    next[++m] = head[u];
    head[u] = m;
    next[++m] = head[v];
    head[v] = m;
}

void tarjan(int u, int fa) {
    dfn[u] = low[u] = ++ bridge_cnt;
    stack[++top] = u;
    for (int i = head[u]; i; i = next[i]) {
        int v = to[i];
        if (!dfn[v]) {
            tarjan(v, u);
            low[u] = min(low[u], low[v]);
            if (low[v] > dfn[u]) {
                cut[u] = 1;
            }
        } else if (v != fa) {
            low[u] = min(low[u], dfn[v]);
        }
    }
    if (dfn[u] == low[u]) {
        while (top >= 0 && stack[top] != u) {
            cut[stack[top]] = 1;
            top--;
        }
        top--;
    }
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= m; i++) {
        int u, v;
        scanf("%d%d", &u, &v);
        add_edge(u, v);
        add_edge(v, u);
    }
    memset(dfn, 0, sizeof(dfn));
    memset(low, 0, sizeof(low));
    memset(cut, 0, sizeof(cut));
    memset(head, -1, sizeof(head));
    bridge_cnt = 0;
    top = -1;
    for (int i = 1; i <= n; i++) {
        if (!dfn[i]) {
            tarjan(i, -1);
        }
    }
    for (int i = 1; i <= n; i++) {
        if (cut[i]) {
            printf("%d ", i);
        }
    }
    return 0;
} 
"""
# END
