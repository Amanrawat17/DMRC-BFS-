from flask import Flask, jsonify, request, render_template
import pickle

class Graph:
    def __init__(self):
        with open('station_map', "rb") as f:
            self.a = pickle.load(f)  # Graph adjacency list
            self.b = pickle.load(f)  # Station names
        self.graph = self.a

    def BFS(self, s, f):
        visited = [False] * len(self.graph)
        queue = []
        dist = [None] * len(self.graph)
        pred = [None] * len(self.graph)
        traversal = []  # List to keep track of the traversal order

        queue.append(s)
        visited[s] = True
        dist[s] = 0
        s1 = s

        while queue:
            s = queue.pop(0)
            traversal.append(s)  # Record the current node in the traversal

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    dist[i] = dist[s] + 1
                    pred[i] = s
                    if i == f:
                        p = pred[i]
                        path = [self.b[f]]
                        while p != s1:
                            path.append(self.b[p])
                            p = pred[p]
                        path.append(self.b[s1])
                        return list(reversed(path)), dist[i], traversal  # Return traversal order

        return [], 0, []  # If no path found


app = Flask(__name__)
graph = Graph()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/find_path', methods=['POST'])
def find_path():
    data = request.get_json()
    source = data.get('source')
    destination = data.get('destination')

    path, distance, traversal = graph.BFS(source, destination)

    return jsonify({
        'path': path,
        'distance': distance,
        'traversal': traversal
    })

@app.route('/stations', methods=['GET'])
def get_stations():
    station_list = [(id, name) for id, name in graph.b.items()]
    return jsonify(station_list)

if __name__ == '__main__':
    app.run(debug=True)
