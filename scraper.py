import re
from bs4 import BeautifulSoup

def get_army_size(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    total = 0
    for label in soup.select('.datagrid-title'):
        if label.text.strip() in ["Attack Soldiers", "Defense Soldiers", "Super Attack Soldiers", "Super Defense Soldiers"]:
            val = label.find_next(class_="datagrid-content")
            if val:
                try:
                    total += int(val.text.replace(",", "").strip())
                except Exception:
                    continue
    return total

def get_untrained(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    label = soup.find("div", class_="datagrid-title", string="Untrained Soldiers")
    if label:
        val = label.find_next("div", class_="datagrid-content")
        if val:
            return int(val.text.replace(",", "").strip())
    return 0

def get_antibot_token(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    t1_input = soup.find("input", {"name": "time1t"})
    if t1_input and t1_input.get("value"):
        return t1_input["value"]
    return "dummy"  # fallback if not found

def get_bank_info(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    rows = soup.select("table tr")
    info = {}
    for r in rows:
        tds = r.find_all("td")
        if len(tds) == 2:
            label = tds[0].text.strip().lower()
            val = tds[1].text.strip().replace(",", "")
            if "avalible spice" in label:
                info["spice"] = int(val)
            elif "total in bank" in label:
                info["bank"] = int(val)
            elif "bank space left" in label:
                info["bank_space_left"] = int(val)
            elif "total bank size" in label:
                info["bank_size"] = int(val)
    return info

def get_targets(page_html, my_army):
    soup = BeautifulSoup(page_html, 'html.parser')
    targets = []
    for row in soup.select('table.table-vcenter tbody tr'):
        cells = row.find_all('td')
        if len(cells) < 7:
            continue
        try:
            army_size = int(cells[4].get_text(strip=True).replace(',', ''))
            spice = int(cells[5].get_text(strip=True).replace(',', ''))
        except Exception:
            continue
        if army_size < my_army and spice > 0:
            raid_form = cells[6].find('form', action="/attack/raid")
            if raid_form:
                target_id = raid_form.find('input', {'name': 'target_id'})['value']
                attacks = raid_form.find('input', {'name': 'attacks'})['value']
                targets.append({'id': target_id, 'army': army_size, 'spice': spice, 'attacks': attacks, 'row': row})
    return targets

def get_mothership_status(html):
    # Placeholder for actual mothership status scraping
    # You'd parse HP, repair state, upgrades, etc. from the mothership page here.
    return {"needs_repair": True}

def get_repair_status(repair_html):
    """
    Scrape current damaged units for partial repair logic.
    Returns dict like {"att_damaged": int, "def_damaged": int}
    """
    soup = BeautifulSoup(repair_html, 'html.parser')
    result = {"att_damaged": 0, "def_damaged": 0}
    for label in soup.select(".datagrid-title"):
        label_text = label.text.strip()
        val = label.find_next(class_="datagrid-content")
        if not val:
            continue
        try:
            value = int(val.text.replace(",", "").strip())
        except Exception:
            continue
        if "Attack Units Damaged" in label_text:
            result["att_damaged"] = value
        elif "Defense Units Damaged" in label_text:
            result["def_damaged"] = value
    return result