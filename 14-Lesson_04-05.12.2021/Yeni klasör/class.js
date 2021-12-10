class arac {
    #id // # işareti private anlamına gelir python karşılığı iki alt çizgi "__id"
    #marka
    #model

    constructor(id, marka, model) {//pythondaki init yerine constructor geçer. __init__ pythondaki self keyword unun karşılığı burada this
        this.#id = id;
        this.#marka = marka;
        this.#model = model;
    }

    get id() { // python karşılığı @property
        return this.#id;
    }

    set id(value) {// python karşılığı @setter
        this.#id = value;
    }

    get id() { // python karşılığı @property
        return this.#id;
    }

    set id(value) {// python karşılığı @setter
        this.#id = value;
    }

    get id() { // python karşılığı @property
        return this.#id;
    }

    set id(value) {// python karşılığı @setter
        this.#id = value;
    }

    aracBilgileriniGetir() {
        return this.#id + " " + this.#marka + " " + this.#model;
    }
}

const divArac = document.getElementById("divArac");
var arac = new Arac(1, "toyota", "corolla");
divArac.innerHTML = arac.aracBilgileriniGetir()

//-------------------------------------inheritance kullanımı

//class kamyonet extends arac() ---- python karşılığı class Kamyonet(Arac)

//-------------------------------------object kullanımı

var arac2 = {
    id: 1,
    marka: "ford",
    model: "focus",
    aracBilgileriniGetir: function () {
        return this.id + " " + this.marka + " " + this.model;
    }

}

const divArac2 = document.getElementById("divArac2");

divArac2.innerHTML = arac2.aracBilgileriniGetir()

//arac2.fiyat = 20;

//--------------------------------------
