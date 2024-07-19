from utils import listener
from Crypto.Random.random import randint

FLAG = b"crypto{???????????????????????????????????}"

# N is a product of safe primes
N = 56135841374488684373258694423292882709478511628224823806418810596720294684253418942704418179091997825551647866062286502441190115027708222460662070779175994701788428003909010382045613207284532791741873673703066633119446610400693458529100429608337219231960657953091738271259191554117313396642763210860060639141073846574854063639566514714132858435468712515314075072939175199679898398182825994936320483610198366472677612791756619011108922142762239138617449089169337289850195216113264566855267751924532728815955224322883877527042705441652709430700299472818705784229370198468215837020914928178388248878021890768324401897370624585349884198333555859109919450686780542004499282760223378846810870449633398616669951505955844529109916358388422428604135236531474213891506793466625402941248015834590154103947822771207939622459156386080305634677080506350249632630514863938445888806223951124355094468682539815309458151531117637927820629042605402188751144912274644498695897277
phi = 56135841374488684373258694423292882709478511628224823806413974550086974518248002462797814062141189227167574137989180030483816863197632033192968896065500768938801786598807509315219962138010136188406833851300860971268861927441791178122071599752664078796430411769850033154303492519678490546174370674967628006608839214466433919286766123091889446305984360469651656535210598491300297553925477655348454404698555949086705347702081589881912691966015661120478477658546912972227759596328813124229023736041312940514530600515818452405627696302497023443025538858283667214796256764291946208723335591637425256171690058543567732003198060253836008672492455078544449442472712365127628629283773126365094146350156810594082935996208856669620333251443999075757034938614748482073575647862178964169142739719302502938881912008485968506720505975584527371889195388169228947911184166286132699532715673539451471005969465570624431658644322366653686517908000327238974943675848531974674382848
g = 986762276114520220801525811758560961667498483061127810099097

def get_bit(i):
    if FLAG[i // 8] & (1 << (i % 8)):
        return pow(g, randint(2, phi - 1), N)
    else:
        return randint(1, N - 1)

class Challenge():
    def __init__(self):
        self.before_input = "Is this real life, or is it just overly complicated math?\n"

    def challenge(self, your_input):
        if "option" not in your_input:
            return {"error": "Your input should contain an option"}
        if your_input["option"] == "get_bit":
            if "i" not in your_input:
                return {"error": "Open your eyes, look up to the skies and see: there's no bit index here."}
            i = int(your_input["i"])
            if not 0 <= i < 8*len(FLAG):
                return {"error": "This bit is a little high or a little low."}
            return {"bit": hex(get_bit(i))}
        else:
            return {"error": "I'm just a poor boy from a poor fantasy, I don't know how to do that."}


listener.start_server(port=13398)
