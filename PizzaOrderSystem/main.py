import csv
import datetime
import pandas as pd
import bcrypt

with open("Menu.txt", "w", encoding='utf-8') as file:
    file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n* ve "
               "seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* "
               "Teşekkür ederiz!")


class Pizza:
    """
    Pizzaların üst sınıfıdır. Pizza çeşitleri bu sınıfdan türetilir

    Parametreler
        description:
            Pizza hakkındaki bilgidir.String türünde veri girilmelidir. Kısa bir açıklama sağlar\n
        cost:
            Pizzanın fiyat bilgisidir. Float türünde veri girilmelidir. 0'dan küçük sayılar girilmemelidir\n
        quantity:
            Pizzanın miktarı, adedi hakkındaki bilgidir. İnteger türünde veri girilmelidir.
            0'dan büyük bir sayı girilmelidir

    --------------------------------------

    Methotlar
        def get_description(self) -> str:
            Pizza sınıfının descripton(açıklama) değerini almaya yarayan methottur

        def set_descripton(self, descripton: str) -> str:
            Pizza sınıfının descripton(açıklama) değerini değiştirmeye ona değer atamaya yarayan methottur

        def get_cost(self) -> float:
            Pizza sınıfının cost(fiyat) değerini almaya yarayan methottur.

        def set_cost(self, cost: float) -> float:
            Pizza sınıfının cost(fiyat) değerini değiştirmeye, ona değer atamaya yarayan methottur.

        def quantity(self):
            Pizza sınıfının quantity(miktar) değerini almaya yarar. Read-only methottur. Atama işlemi yapılamaz

    """

    def __init__(self, description: str, cost: float, quantity: int = 1):
        assert quantity >= 0, f"Quantity(Miktar) değeri sıfır veya sıfırdan küçük değer girilemez ancak {quantity} girilmiş"
        assert cost > 0, f"Cost(Fiyat) değeri sıfırdan küçük olamaz ancak {cost} girilmiş"
        self.__descriptions = description
        self.__costs = cost
        self.__quantity = quantity

    def get_description(self) -> str:
        """
        Pizza sınıfının descripton(açıklama) değerini almaya yarayan methottur
        :return: string değerinde veri döndürmesi beklenir
        """
        return self.__descriptions

    def set_descripton(self, descripton: str) -> str:
        """
        Pizza sınıfının descripton(açıklama) değerini değiştirmeye ona değer atamaya yarayan methottur

        :param descripton: Girilmek istenen açıklama string veri türünde yazılmalıdır.
                           Girilen değer sınıfın açıklaması halinde gelir
        :return: String türünde yeni description verisini geri döndürmesi beklenir
        """
        self.__descriptions = descripton
        return self.__descriptions

    def get_cost(self) -> float:
        """
        Pizza sınıfının cost(fiyat) değerini almaya yarayan methottur

        :return: Float türünde cost verisini geri döndürmesi beklenir
        """
        return self.__costs

    def set_cost(self, cost: float) -> float:
        """
        Pizza sınıfının cost(fiyat) değerini değiştirmeye, ona değer atamaya yarayan methottur.

        :param cost: Değiştirilmek istenen fiyat değeri float tipinde girilmelidir. 0'dan küçük değerler girilmemelidir
        :return: Float türünde yeni cost verisini geri döndürmesi beklenir
        """
        assert cost > 0, f"Cost(Fiyat) değeri sıfırdan küçük olamaz ancak {cost} girilmiş"
        self.__costs = cost
        return self.__costs

    # Read-Only quantity
    @property
    def quantity(self):
        """
        Pizza sınıfının quantity(miktar) değerini almaya yarar. Read-only methottur. Atama işlemi yapılamaz

        :return: Oluşturulurken girilen miktar verisini geri döndürür
        """
        return self.__quantity


class Margherita(Pizza):
    """
    Pizza sınıfında türetilen bir alt sınıftır.

    Parametreler
        description:
            Pizza hakkında kısa açıklamasıdır. Varsayılan olarak sınıfının ismi belirlenmiştir.
        cost:
            Pizzanın fiyatıdır. Varsayılan olarak 99.0 belirlenmiştir. 0'dan küçük sayılar girilmemelidir\n
        quantity:
            Pizzanın adet bilgisidir. Varsayılan olarak 1 belirlenmiştir
    """

    def __init__(self, description="Margherita", cost=99.0, quantity: int = 1):
        super().__init__(description, cost, quantity)


class Classic(Pizza):
    """
    Pizza sınıfında türetilen bir alt sınıftır.

    Parametreler
        description:
            Pizza hakkında kısa açıklamasıdır. Varsayılan olarak sınıfının ismi belirlenmiştir.
        cost:
            Pizzanın fiyatıdır. Varsayılan olarak 90.0 belirlenmiştir. 0'dan küçük sayılar girilmemelidir\n
        quantity:
            Pizzanın adet bilgisidir. Varsayılan olarak 1 belirlenmiştir
    """

    def __init__(self, description="Klasik Pizza", cost=90, quantity=1):
        super().__init__(description, cost, quantity)


class TurkishPizza(Pizza):
    """
        Pizza sınıfında türetilen bir alt sınıftır.

        Parametreler
            description:
                Pizza hakkında kısa açıklamasıdır. Varsayılan olarak sınıfının ismi belirlenmiştir.
            cost:
                Pizzanın fiyatıdır. Varsayılan olarak 105.0 belirlenmiştir. 0'dan küçük sayılar girilmemelidir\n
            quantity:
                Pizzanın adet bilgisidir. Varsayılan olarak 1 belirlenmiştir. 0'dan büyük bir sayı girilmelidir
    """

    def __init__(self, description="Türk Pizzası", cost=105.0, quantity=1):
        super().__init__(description, cost, quantity)


class DominosPizza(Pizza):
    """
        Pizza sınıfında türetilen bir alt sınıftır.

        Parametreler
            description:
                Pizza hakkında kısa açıklamasıdır. Varsayılan olarak sınıfının ismi belirlenmiştir.

            cost:
                Pizzanın fiyatıdır. Varsayılan olarak 108.0 belirlenmiştir. 0'dan küçük sayılar girilmemelidir\n

            quantity:
                Pizzanın adet bilgisidir. Varsayılan olarak 1 belirlenmiştir. 0'dan büyük bir sayı girilmelidir
    """

    def __init__(self, description="Dominos Pizza", cost=108.0, quantity=1):
        super().__init__(description, cost, quantity)


class PlainPizza(Pizza):
    """
        Pizza sınıfında türetilen bir alt sınıftır.

        Parametreler
            description:
                Pizza hakkında kısa açıklamasıdır. Varsayılan olarak sınıfının ismi belirlenmiştir.

            cost:
                Pizzanın fiyatıdır. Varsayılan olarak 85.0 belirlenmiştir. 0'dan küçük sayılar girilmemelidir\n

            quantity:
                Pizzanın adet bilgisidir. Varsayılan olarak 1 belirlenmiştir. 0'dan büyük bir sayı girilmelidir
    """

    def __init__(self, description="Sade Pizza", cost=85, quantity=1):
        super().__init__(description, cost, quantity)


# deneme = Margherita("pizza", 10)
# deneme.get_description()


class Ingredient:
    """
    Mazemelerin(Ingredient) üst sınıfıdır.

    Parametreler
        description:
            Malzemenin kısa açıklamasıdır. String türünde verirdir
        cost:
            Malzemenin fiyatı bilgisidir. Float türündeki veridir, 0'dan küçük girilmemelidir
    """

    def __init__(self, description: str, cost: float):
        assert cost > 0, f"Cost(Fiyat) değeri sıfırdan küçük olamaz ancak {cost} girilmiş"
        self.__descriptions = description
        self.__costs = cost

    def get_descripton(self):
        return self.__descriptions

    def get_cost(self):
        return self.__costs


class Onion(Ingredient):
    """
    Malzemeler üst sınıfından türetilmiştir

    Parametreler
        description:
            Malzemenin kısa açıklamasıdır. String türünde verirdir. Varsayılan olarak "Ekstra Soğanlı" verilmiştir
        cost:
            Malzemenin fiyatı bilgisidir. Float türündeki veridir, 0'dan küçük girilmemelidir. Varsayılan olarak
            3 girilmiştir
    """

    def __init__(self, description="Ekstra Soğanlı", cost=3):
        super().__init__(description, cost)


class Olive(Ingredient):
    """
    Malzemeler üst sınıfından türetilmiştir

    Parametreler
        description:
            Malzemenin kısa açıklamasıdır. String türünde verirdir. Varsayılan olarak "Ekstra Zeytinli" verilmiştir
        cost:
            Malzemenin fiyatı bilgisidir. Float türündeki veridir, 0'dan küçük girilmemelidir. Varsayılan olarak
            6 girilmiştir
    """

    def __init__(self, description="Ekstra Zeytinli", cost=6):
        super().__init__(description, cost)


class Mushroom(Ingredient):
    """
    Malzemeler üst sınıfından türetilmiştir

    Parametreler
        description:
            Malzemenin kısa açıklamasıdır. String türünde verirdir. Varsayılan olarak "Ekstra Mantarlı" verilmiştir
        cost:
            Malzemenin fiyatı bilgisidir. Float türündeki veridir, 0'dan küçük girilmemelidir. Varsayılan olarak
            5 girilmiştir
    """

    def __init__(self, description="Ekstra Mantarlı", cost=5):
        super().__init__(description, cost)


class GoatCheese(Ingredient):
    """
    Malzemeler üst sınıfından türetilmiştir

    Parametreler
        description:
            Malzemenin kısa açıklamasıdır. String türünde verirdir. Varsayılan olarak "Ekstra Keçi Peynirli" verilmiştir
        cost:
            Malzemenin fiyatı bilgisidir. Float türündeki veridir, 0'dan küçük girilmemelidir. Varsayılan olarak
            7 girilmiştir
    """

    def __init__(self, description="Ekstra Keçi Peynirli", cost=7):
        super().__init__(description, cost)


class Meat(Ingredient):
    """
    Malzemeler üst sınıfından türetilmiştir

    Parametreler
        description:
            Malzemenin kısa açıklamasıdır. String türünde verirdir. Varsayılan olarak "Ekstra Etli" verilmiştir
        cost:
            Malzemenin fiyatı bilgisidir. Float türündeki veridir, 0'dan küçük girilmemelidir. Varsayılan olarak
            10 girilmiştir
    """

    def __init__(self, description="Ekstra Etli", cost=10):
        super().__init__(description, cost)


class Corn(Ingredient):
    """
    Malzemeler üst sınıfından türetilmiştir

    Parametreler
        description:
            Malzemenin kısa açıklamasıdır. String türünde verirdir. Varsayılan olarak "Ekstra Mısırlı" verilmiştir
        cost:
            Malzemenin fiyatı bilgisidir. Float türündeki veridir, 0'dan küçük girilmemelidir. Varsayılan olarak
            4 girilmiştir
    """

    def __init__(self, description="Ekstra Mısırlı", cost=4):
        super().__init__(description, cost)


class PizzaFactory:
    def __init__(self, base_pizza: Pizza):
        self.pizza = base_pizza
        self.cost = self.pizza.get_cost()
        self.extra = []
        self.extras_description = ""

    def __call__(self, *extras: Ingredient):
        for e in extras:
            self.extra.append(e)
        return self.extra

    def get_cost(self):
        for e in self.extra:
            self.cost += e.get_cost()
        return self.cost

    def get_description(self):
        for d in self.extra:
            if d == self.extra[-1]:
                self.extras_description += d.get_descripton()
            else:
                self.extras_description += d.get_descripton() + ", "
        return f"{self.extras_description} {self.pizza.get_description()}"


def display_header(msg="Pizza Sipariş Sistemine Hoşgeldiniz"):
    print(msg)


def display_goodbye(msg="Pizza sipaiş sistemini kullandığınız için teşekkür ederiz"):
    print(msg)


def user_data():
    while True:
        user_name = input("Lütfen adınızı giriniz")
        if not user_name.isalpha():
            print("Lütfen metinsel ifadeler(örneğin Ahmet gibi) giriniz")
        else:
            break
    while True:
        user_id = input("Lütfen TC kimlik numaranızı giriniz")
        if len(user_id) != 11 or not user_id.isdigit() or user_id.isspace():
            print("Geçersiz giriş! Lütfen 11 haneli TC kimlik numaranızı giriniz")
        else:
            break

    while True:
        user_card_information = input("Lütfen kredi kart numaranızı giriniz")
        if len(user_card_information) != 16 or not user_card_information.isdigit() or user_card_information.isspace():
            print("Geçersiz giriş! Lütfen 16 haneli kredi kart numaranızı giriniz")
        else:
            break

    print("Şifreyi girerken aşağıdaki kuralları unutmayınız")
    print("Şifrenin uzunluğu 6'dan küçük 12'den büyük olmamalıdır")
    print("Şifrede boşluk bulunmamalıdır")
    print("Şifrede bir adet sayı bulunmalıdır.")
    print("Şifrede bir adet harf bulunmalıdır.")
    print("Şifrede bir adet küçük harf bulunmalıdır")
    print("Şifrede bir adet büyük harf bulunmalıdır")
    while True:
        user_card_password = input("Lütfen kart şifrenizi giriniz")
        if check_strong(user_card_password):
            break
    pwd_byte = user_card_password.encode('utf-8')
    salt = bcrypt.gensalt()
    pwd_hash = bcrypt.hashpw(pwd_byte, salt)
    order_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    return user_name, user_id, user_card_information, pwd_hash, order_time


def check_strong(password) -> True:
    if not (6 <= len(password) <= 12):
        print("Şifrenin uzunluğu 6'dan küçük 12'den büyük olmamalıdır")
        return False
    if any(char.isspace() for char in password):
        print("Şifrede boşluk bulunmamalıdır")
        return False
    if password.isdigit():
        print("Şifrede bir adet harf bulunmalıdır.")
        return False
    if password.isalpha():
        print("Şifrede bir adet sayı bulunmalıdır.")
        return False
    if password.islower():
        print("Şifrede bir adet büyük harf bulunmalıdır")
        return False
    if password.isupper():
        print("Şifrede bir adet küçük harf bulunmalıdır")
        return False

    return True


Pizzas = {1: Classic(), 2: Margherita(), 3: TurkishPizza(), 4: PlainPizza(), 5: Mushroom()}

Ingredients = {11: Olive(), 12: Mushroom(), 13: GoatCheese(), 14: Meat(), 15: Onion(), 16: Corn()}


class Choice:
    extra_choices = []
    display_header()
    with open("Menu.txt", "r", encoding='utf-8') as file:
        menu = file.read()
        print(menu)

    @classmethod
    def pizza_choice(cls):
        while True:
            try:
                cls.choice = int(input("Lütfen seçmek istediğniz pizzanın numarasını giriniz. \n"))
                if cls.choice in Pizzas.keys():
                    cls.pizza = PizzaFactory(Pizzas[cls.choice])
                    return cls.pizza
                else:
                    print("Seçiminiz listede yoktur. Lütfen listede olan pizzanın numarasını tamsayı olarak giriniz.\n")
            except ValueError:
                print("Lütfen tamsayı bir değer(örneğin 1 gibi) giriniz. \n")

    @classmethod
    def extra_choice(cls):
        while True:
            try:
                extra_choice = int(input(
                    "Lütfen seçmek istediğiniz sosun(ekstra malzeme) numarasını giriniz. İşlemi sonlandırmak için 0'ı girebilirsiniz.\n"))
                if extra_choice == 0:
                    break
                elif extra_choice not in Ingredients.keys():
                    print("Seçiminiz listede yoktur. Lütfen listede olan sosun numarasını tamsayı olarak giriniz.\n")
                elif Ingredients[extra_choice] in cls.extra_choices:
                    print("bu seçimi zaten yapmıştınız")
                elif extra_choice in Ingredients.keys():
                    cls.extra_choices.append(Ingredients[extra_choice])

            except ValueError:
                print("Lütfen tamsayı bir değer(örneğin 1 gibi) giriniz. \n")

            except Exception:
                print("Hatalı seçim")

        return cls.extra_choices


class Main:
    def __init__(self):
        self.pizza_data = Choice.pizza_choice()
        self.extra_data = Choice.extra_choice()

    def is_valid(self, msg="İşlemi onaylıyor musunuz: Y/N"):
        self.pizza_data(*self.extra_data)
        description = self.pizza_data.get_description()
        cost = f"{self.pizza_data.get_cost()}TL"
        print(description)
        print(cost)
        validation = input(msg)
        if validation.upper() == "Y":
            user_name, user_id, card_info, password, order_time = user_data()
            user_dict = [{'Kullanıcı Adı': user_name,
                          'Kullanıcı Kimliği': user_id,
                          'Kredi Kartı Bilgileri': card_info,
                          'Sipariş Açıklaması': description,
                          'Sipariş Fiyatı': cost,
                          'Sipariş Zamanı': order_time,
                          'Kredi Kartı Şifresi(şifreli)': password}]
            print(user_dict)
            user_df = pd.DataFrame(user_dict)
            user_df.to_csv("Orders_Database.csv", index=True, encoding='utf-8', mode='a')
            display_goodbye()
        else:
            display_goodbye()


if __name__ == "__main__":
    Main().is_valid()
