public_toilet= "PB" #Global varible

def home():
    private_toilet="PT"
    print(private_toilet)
    public_toilet="PBL" # Local variable same name as Global variable here preference will be give to local variable
    print(public_toilet)

home()