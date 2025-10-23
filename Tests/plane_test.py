import requests
from bs4 import BeautifulSoup


def get_airfleets_info(registration="EC-LVV"):
    # 1. Buscar la matrícula en Airfleets
    search_url = f"https://www.airfleets.net/recherche/?key={registration}"
    resp = requests.get(search_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # 2. Encontrar el primer enlace a la ficha del avión
    link = soup.find("a", href=lambda x: x and x.startswith("/ficheapp/plane-"))
    if not link:
        return {"error": f"No se encontró ficha para {registration}"}

    plane_url = "https://www.airfleets.net" + link["href"]

    # 3. Descargar ficha técnica
    resp = requests.get(plane_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # 4. Extraer tabla principal con datos
    info = {}
    table = soup.find("table", {"class": "fiche"})
    if table:
        for row in table.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) == 2:
                key = cols[0].get_text(strip=True)
                val = cols[1].get_text(strip=True)
                info[key] = val

    info["url_ficha"] = plane_url
    return info


if __name__ == "__main__":
    data = get_airfleets_info("EC-LVV")
    for k, v in data.items():
        print(f"{k}: {v}")