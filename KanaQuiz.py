import turtle
import random
def HiraQuizzer():
    HiraArray = ["あ","い","う","え","お",
            "か","き","く","け","こ",
            "が","ぎ","ぐ","げ","ご",
            "さ","し","す","せ","そ",
            "ざ","じ","ず","ぜ","ぞ",
            "た","ち","つ","て","と",
            "だ","ぢ","づ","で","ど",
            "な","に","ぬ","ね","の",
            "は","ひ","ふ","へ","ほ",
            "ば","び","ぶ","べ","ぼ",
            "ぱ","ぴ","ぷ","ぺ","ぽ",
            "ま","み","む","め","も",
            "や","ゆ","よ",
            "ら","り","る","れ","ろ",
            "わ","を"]
    EngArray = ["a", "i", "u", "e", "o",
            "ka","ki","ku","ke","ko",
            "ga","gi","gu","ge","go",
            "sa","shi","su","se","so",
            "zi","ji","zu","ze","zo",
            "ta","chi","tsu","te","to",
            "da","di","du","de","do",
            "na","ni","nu","ne","no",
            "ha","hi","hu","he","ho",
            "ba","bi","bu","be","bo",
            "pa","pi","pu","pe","po",
            "ma","mi","mu","me","mo",
            "ya","yu","yo",
            "ra","ri","ru","re","ro",
            "wa","oo"]
    tim = turtle.Turtle()
    screen = turtle.Screen()
    inputV = "";
    correctCount = 0
    incorrectCount = 0
    attempts = 0
    while(inputV != "0"):
        tim.color("blue")  
        tim.pensize(5)
        tim.up()
        randomNum = random.randint(-1,45)
        tim.setpos(-150,-150)
        tim.ht()
        screen.clear()
        tim.write(HiraArray[randomNum], font=("Arial", 200, "normal"))
        inputV = screen.textinput("Hiragana", "What is the Hiragana?\n(type 'menu' to go back to menu)")

        if(inputV == "menu"):
            screen.clear()
            from KanaQuiz import main
            
        if(inputV == EngArray[randomNum]):
            tim.setpos(0,0)
            tim.color("green")
            tim.write("Correct", font=("Arial", 50, "normal"), align="center")
            print("Correct! "+HiraArray[randomNum]+" = "+inputV)
            correctCount+=1
            attempts+=1
            print("Score: ",correctCount,"/",attempts)
        
        else:
            tim.setpos(0,0)
            tim.color("red")
            tim.write("InCorrect", font=("Arial",50, "normal"), align="center")
            print("Incorrect... "+HiraArray[randomNum]+" != "+inputV)
            incorrectCount+=1
            attempts+=1
            print("Score: ",correctCount,"/",attempts)

def KataQuizzer():
    KataArray = ["ア","イ","ウ","エ","オ",
            "カ","キ","ク","ケ","コ",
            "ガ","ギ","グ","ゲ","ゴ",
            "サ","シ","ス","セ","ソ",
            "ザ","ジ","ズ","ゼ","ゾ",
            "タ","チ","ツ","テ","ト",
            "ダ","ヂ","ヅ","デ","ド",
            "ナ","ニ","ヌ","ネ","ノ",
            "ハ","ヒ","フ","ヘ","ホ",
            "バ","ビ","ブ","ベ","ボ",
            "パ","ピ","プ","ペ","ポ",
            "マ","ミ","ム","メ","モ",
            "ヤ","ユ","ヨ",
            "ラ","リ","ル","レ","ロ",
            "ワ","ヲ"]
    			    
    EngArray = ["a", "i", "u", "e", "o",
            "ka","ki","ku","ke","ko",
            "ga","gi","gu","ge","go",
            "sa","shi","su","se","so",
            "zi","ji","zu","ze","zo",
            "ta","chi","tsu","te","to",
            "da","di","du","de","do",
            "na","ni","nu","ne","no",
            "ha","hi","hu","he","ho",
            "ba","bi","bu","be","bo",
            "pa","pi","pu","pe","po",
            "ma","mi","mu","me","mo",
            "ya","yu","yo",
            "ra","ri","ru","re","ro",
            "wa","oo"]
    tim = turtle.Turtle()
    screen = turtle.Screen()
    inputV = "";
    correctCount = 0
    incorrectCount = 0
    attempts = 0
    while(inputV != "0"):
        tim.color("blue")  
        tim.pensize(5)
        tim.up()
        randomNum = random.randint(-1,45)
        tim.setpos(-150,-150)
        tim.ht()
        screen.clear()
        tim.write(KataArray[randomNum], font=("Arial", 200, "normal"))
        inputV = screen.textinput("Katakana", "What is the Katakana?\n(type 'menu' to go back to menu)")

        if(inputV == "menu"):
            screen.clear()
            from KanaQuiz import main
            
        if(inputV == EngArray[randomNum]):
            tim.setpos(0,0)
            tim.color("green")
            tim.write("Correct", font=("Arial", 50, "normal"), align="center")
            print("Correct! "+KataArray[randomNum]+" = "+inputV)
            correctCount+=1
            attempts+=1
            print("Score: ",correctCount,"/",attempts)
        
        else:
            tim.setpos(0,0)
            tim.color("red")
            tim.write("InCorrect", font=("Arial",50, "normal"), align="center")
            print("Incorrect... "+KataArray[randomNum]+" != "+inputV)
            incorrectCount+=1
            attempts+=1
            print("Score: ",correctCount,"/",attempts)




def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.ht()
    t.up()
    t.write("KanaQuiz",font=("Arial", 150, "normal"), align = "center")
    t.setpos(0,-150)
    t.write("Press 1: Hiragana Quiz",font=("Arial", 25, "normal"), align = "center")
    t.setpos(0,-225)
    t.write("Press 2: Katakana Quiz",font=("Arial", 25, "normal"), align = "center")
    inputU = screen.textinput("", "")
    print(inputU)
    if(inputU == "1"):
        HiraQuizzer()
    if(inputU == "2"):
        KataQuizzer()

main()

