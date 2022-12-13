from datetime import date
from flask import Flask, redirect, render_template, request
import random
import time

app = Flask(__name__)

app.config['SECRET_KEY'] = '''k"o=07-F]Q,vD|~j/W9qTbBKn)S.+J[85NgRMd^uXz(P6`}YZ'mf%G4pOe_2I#C$wi\lHxcr@VUyshLE3t!*{;a<?&1:A>'''

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gameplay", methods=['GET', 'POST'])
def game_page():
    return render_template("Gamepage.html")

@app.route("/error-message")
def error():
    return render_template("error.html")

@app.route("/select-alien-10", methods=['GET', 'POST'])
def Select_Aline():
    user_selected_aliens = []
    if request.method == "POST":
        if 'ben' not in request.form:
            pass
        else:
            name = "Huwmungosaur"
            best_power = "Earthquake"
            abilites = "Enhanced Strength"
            user_selected_aliens.append("hew.webp")
        if 'ben70' not in request.form:
            pass
        else:
            name = "Ultimate Huwmungosaur"
            best_power = "Missile Generation"
            abilites = "Enhanced Durability"
            user_selected_aliens.append("uhew.webp")
        if 'ben71' not in request.form:
            pass
        else:
            name = "Wildmutt"
            best_power = "Sensing"
            abilites = "Enhanced Hearing"
            user_selected_aliens.append("wildmutt.jpg")
        if 'ben1' not in request.form:
            pass
        else:
            name = "Ultimate Wildmutt"
            best_power = "Sightless Sensing"
            abilites = "Enhanced Speed"
            user_selected_aliens.append("uwildmutt.webp")
        if 'ben2' not in request.form:
            pass
        else:
            name = "Swampfire"
            best_power = "Fertilizer Gas Generation"
            abilites = "Elasticity"
            user_selected_aliens.append("swam.jpg")
        if 'ben3' not in request.form:
            pass
        else:
            name = "Ultimate Swampfire"
            best_power = "Methane Generation"
            abilites = "Azur Pyrokinesis"
            user_selected_aliens.append("US.webp")
        if 'ben4' not in request.form:
            pass
        else:
            name = "Echo Echo"
            best_power = "Sonic Redirection"
            abilites = "Self-Duplication"
            user_selected_aliens.append("echo.webp")
        if 'ben5' not in request.form:
            pass
        else:
            name = "Ultimate Echo Echo"
            best_power = "Sonic Screams"
            abilites = "Duplicating Sonic Disks"
            user_selected_aliens.append("uecho.webp")
        if 'ben6' not in request.form:
            pass
        else:
            name = "Cannonbolt"
            best_power = "Sphere Transformation"
            abilites = "Enhanced Jumping"
            user_selected_aliens.append("cannon.webp")
        if 'ben7' not in request.form:
            pass
        else:
            name = "Ultimate Cannonbolt"
            best_power = "Environmental Perception"
            abilites = "Sphere Transformation"
            user_selected_aliens.append("ucannon.webp")
        if 'ben8' not in request.form:
            pass
        else:
            name = "Spider Monkey"
            best_power = "Webbing Generation"
            abilites = "Enhanced Acrobatics"
            user_selected_aliens.append("sp.webp")
        if 'ben9' not in request.form:
            pass
        else:
            name = "Ultimate Spider Monkey"
            best_power = "Webbing Spit"
            abilites = "Survivability"
            user_selected_aliens.append("usp.jpg")
        if 'ben10' not in request.form:
            pass
        else:
            name = "Bigchill"
            best_power = "Ice Breath"
            abilites = "Hypnosis Resistance"
            user_selected_aliens.append("bigchill.webp")
        if 'ben11' not in request.form:
            pass
        else:
            name = "Ultimate Bigchill"
            best_power = "Wind Breath"
            abilites = "Temperature Resistance"
            user_selected_aliens.append("ubigchill.webp")
        if 'ben12' not in request.form:
            pass
        else:
            name = "Way Big"
            best_power = "Cosmic Rays"
            abilites = "Temperature Resistance"
            user_selected_aliens.append("waybig.webp")
        if 'ben13' not in request.form:
            pass
        else:
            name = "Terraspin"
            best_power = "Tornado Generation"
            abilites = "Enhanced Strength"
            user_selected_aliens.append("spin.webp")
        if 'ben14' not in request.form:
            pass
        else:
            name = "Ampfibian"
            best_power = "Circuitry Travel"
            abilites = "Electrical Telepathy"
            user_selected_aliens.append("ele.webp")
        if 'ben15' not in request.form:
            pass
        else:
            name = "Water Hazard"
            best_power = "Hydrokinetic Flight"
            abilites = "Underwater Breathing"
            user_selected_aliens.append("water.jpg")
        if 'ben16' not in request.form:
            pass
        else:
            name = "Bloxx"
            best_power = "Explosive Projectiles"
            abilites = "Regeneration"
            user_selected_aliens.append("Bloxx.webp")
        if 'ben17' not in request.form:
            pass
        else:
            name = "Brainstorm"
            best_power = "Electric Force Fields"
            abilites = "Enhanced Intelligence"
            user_selected_aliens.append("brain.webp")
        if 'ben18' not in request.form:
            pass
        else:
            name = "Jetray"
            best_power = "Fire Generation"
            abilites = "Speed Swimming"
            user_selected_aliens.append("Jetray.webp")
        if 'ben19' not in request.form:
            pass
        else:
            name = "Goop"
            best_power = "Acidic Slime"
            abilites = "Slippery Body"
            user_selected_aliens.append("goom.webp")
        if 'ben20' not in request.form:
            pass
        else:
            name = "Heatblast"
            best_power = "Fire Breath"
            abilites = "Fire Absorption"
            user_selected_aliens.append("heat.webp")
        if 'ben21' not in request.form:
            pass
        else:
            name = "Eatle"
            best_power = "Laser Beams (after eating)"
            abilites = "Solid Matter Ingestion"
            user_selected_aliens.append("eatle.webp")
        if 'ben22' not in request.form:
            pass
        else:
            name = "Lodestar"
            best_power = "Magnetic Force Field Generation"
            abilites = "Magno-Telekinesis"
            user_selected_aliens.append("Lodestar.webp")
        if 'ben23' not in request.form:
            pass
        else:
            name = "NRG"
            best_power = "Intense Heat Generation"
            abilites = "Nucleokinesiss"
            user_selected_aliens.append("NRG.webp")
        if 'ben24' not in request.form:
            pass
        else:
            name = "Chromastone"
            best_power = "Energy Beams"
            abilites = "Energy Conversion"
            user_selected_aliens.append("croma.webp")
        if 'ben25' not in request.form:
            pass
        else:
            name = "Clockword"
            best_power = "Time Reduction"
            abilites = "Time Travel"
            user_selected_aliens.append("clockword.webp")
        if 'ben26' not in request.form:
            pass
        else:
            name = "XLR8"
            best_power = "Vortex Creation"
            abilites = "Super Speed"
            user_selected_aliens.append("xlr8.png")
        if 'ben27' not in request.form:
            pass
        else:
            name = "Juryigg"
            best_power = "Unknown"
            abilites = "Technological Modification"
            user_selected_aliens.append("juryigg.webp")
        if 'ben28' not in request.form:
            pass
        else:
            name = "Grey Matter"
            best_power = "Unknown"
            abilites = "Unknown"
            user_selected_aliens.append("grey.webp")
        if 'ben29' not in request.form:
            pass
        else:
            name = "Stink Fly"
            best_power = "Herbicide Projection"
            abilites = "360° Vision"
            user_selected_aliens.append("stink.webp")
        if 'ben30' not in request.form:
            pass
        else:
            name = "Alien X"
            best_power = "Unknown"
            abilites = "Unknown"
            user_selected_aliens.append("alienx.jpg")
        if 'ben31' not in request.form:
            pass
        else:
            name = "Shocksquatch"
            best_power = "Force Field Generation"
            abilites = "Electrical Telekinesis"
            user_selected_aliens.append("Sk.webp")
        if 'ben32' not in request.form:
            pass
        else:
            name = "Eye Guy"
            best_power = "Energy Beams"
            abilites = "Movable Eyes"
            user_selected_aliens.append("eye.webp")
        if 'ben33' not in request.form:
            pass
        else:
            name = "Four Arms"
            best_power = "Earthquake Generation"
            abilites = "Enhanced Acrobatics"
            user_selected_aliens.append("4arms.webp")
        if 'ben34' not in request.form:
            pass
        else:
            name = "Armodrillo"
            best_power = "Earthquake Generation"
            abilites = "Jackhammer Arms"
            user_selected_aliens.append("ar.webp")
        if 'ben35' not in request.form:
            pass
        else:
            name = "Chamalien"
            best_power = "Unknown"
            abilites = "Invisible"
            user_selected_aliens.append("cm.webp")
        if 'ben36' not in request.form:
            pass
        else:
            name = "Ripjaws"
            best_power = "Underwater Vortex Generation"
            abilites = "Underwater Breathing"
            user_selected_aliens.append("Rip.webp")
        if 'ben37' not in request.form:
            pass
        else:
            name = "Buzzshock"
            best_power = "Electric Redirection"
            abilites = "Teleportation"
            user_selected_aliens.append("Buzzshock.webp")
        
        if len(request.form['user_name']) == 0:
                return redirect("/error-message")
        elif (len(user_selected_aliens) != 0) and (len(user_selected_aliens) == 1) and 'user_name' in request.form:
            computer_selected_aliens = ["villan2.webp", "villan3.jpg", 'agro.webp', "villan3.webp", 'xlr8.png', 'wildmutt.jpg', 'waybig.webp', 'water.jpg', 'vilan.png', 'uwildmutt.webp', 'usp.jpg', 'US.webp', 'uhew.webp', 'uecho.webp', 'ucannon.webp', 'ubigchill.webp', 'swam.jpg', 'stink.webp', 'spin.webp', 'sp.webp', 'Sk.webp', 'Rip.webp', 'rath.webp', 'NRG.webp', 'Lodestar.webp', 'kevin.webp', 'juryigg.webp', 'hew.webp', 'heat.webp', 'grey.webp', 'goom.webp', 'eye.webp', 'ele.webp', 'echo.webp', 'eatle.webp', 'dimond head.jpg', 'croma.webp', 'cm.webp', 'clockword.webp', 'cannon.webp', 'Buzzshock.webp', 'Bloxx.webp', 'bigchill.webp', 'ar.webp', 'alienx.jpg', 'agrog.webp', '4arms.webp', 'brain.webp', "Hex.webp", "Vilgax.webp"]
            pc_aliens = random.choice(computer_selected_aliens)
            pc_names = ["Local Computer", "Cool Boy", "I Am Buddy", "Famous Man", "Lucky Boy", "Princess", "Park Sin", "Tom Park", "Robby"]
            pc_name = random.choice(pc_names)
            user_name = (request.form['user_name']).capitalize()
            Today = date.today()
            for i in (user_selected_aliens):
                my_aliens = i
                time.sleep(2)
            return render_template("Gamepage.html", my_aliens=my_aliens, pc_aliens=pc_aliens, name=name, best_power=best_power, abilites=abilites, user_name=user_name, pc_name=pc_name, Today=Today)
        
    no_of_aliens = len(user_selected_aliens)
    return render_template("selectpage.html", no_of_aliens=no_of_aliens)
    
if __name__ == "__main__":
    app.run(debug=False, port=9090)