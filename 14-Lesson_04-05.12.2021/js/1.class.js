//----------------------------------------------------- object kullanımı
class Arac{
    #id  // python karşılığı iki alt çizgi __id
    #marka
    #model

    constructor(id,marka,model){ // python daki karşılığı __init__ , pythondaki self keywordunun karşılığı burada this
            this.#id = id;
            this.#marka = marka;
            this.#model = model;
    }

    get id(){  // python karşılığı @property
        return this.#id;
    }

    set id(value){ // python karşılı @.....setter
        this.#id = value;
    }

    get marka(){  // python karşılığı @property
        return this.#marka;
    }

    set marka(value){ // python karşılı @.....setter
        this.#marka = value;
    }

    get model(){  // python karşılığı @property
        return this.#model;
    }

    set model(value){ // python karşılı @.....setter
        this.#model = value;
    }

    aracBilgilieriniGetir(){
        return this.#id + " " + this.#marka + " " + this.#model;
    }

}

const divArac = document.getElementById("divArac");

var arac = new Arac(1,"ford","focus");



divArac.innerHTML =arac.aracBilgilieriniGetir();

// class inheritance 

// class kamyonet extends Arac {

// }


// interitance python karşılığı

// class Kamyonet(Arac):
//     pass


//---------------------------------------------------------- object kullanımı --- en çok kullanılan teknik

var arac2 = {
    id : 1,
    marka : "ford",
    model : "focus",
    aracBilgilieriniGetir : function(){
        return this.id + " " + this.marka + " " + this.model;
    }
}

const divArac2 = document.getElementById("divArac2");

divArac2.innerHTML =arac2.aracBilgilieriniGetir();

// arac2.fiyat = 20;




//------------------------------------------------------ function ile kullanım


var arac3 =function(){
   id = 1;

   marka =  "ford";

    model = "focus";

   aracBilgilieriniGetir = function(){
        return this.id + " " + this.marka + " " + this.model;
   }
}


// funciton extend - inheritance

arac3.ptototype.fiyat = 20;




