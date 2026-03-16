from flask import Flask, render_template
import requests

app = Flask(__name__)

# Step 2: Replace with your actual API key
api_key = 'd75b842814a4437a9241b224e026ae43'
headers = {'X-Auth-Token': api_key}
url = "http://api.football-data.org/v4/matches"

# Function to fetch scores (similar to your previous project)
def fetch_scores():
    """
    Fetch live football match scores from the API.

    Returns:
        list: A list of dictionaries containing match data for the top 5 matches.
              Returns an empty list if no matches are found.
        str: An error message if an exception occurs during the API request.
    """
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        if 'matches' in data and len(data['matches']) > 0:
            matches = data['matches'][:5]  # Display top 5 matches for brevity
            return matches
        else:
            return []  # Return an empty list if no matches
    except Exception as e:
        return f"Error fetching data: {e}"

# STEP 3: Decoramos la ruta para que responda a la URL raíz ('/')
@app.route('/')
def load_index_page():
    """
    Flask route for the main page.
    Renders the index.html template.
    Returns:
        str: Rendered HTML content of the index page.
    """
    # STEP 4: Cargamos el archivo index.html ubicado en la carpeta components
    return render_template('components/index.html')


# STEP 5: Definimos la ruta para la página de marcadores
@app.route('/scores')
def load_scores_page():
    """
    Flask route for the scores page.
    Renders the scores.html template with the current live scores.
    Returns:
        str: Rendered HTML content of the scores page.
    """
    # Obtenemos los datos de la API llamando a la función fetch_scores()
    live_scores = fetch_scores()

    # STEP 6: Renderizamos el template y le pasamos los datos
    # 'matches' es el nombre que usaremos dentro del archivo HTML (Jinja2)
    return render_template('components/scores.html', matches=live_scores)

if __name__ == '__main__':
    app.run(debug=True)