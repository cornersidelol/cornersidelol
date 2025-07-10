from tkinter import *

from ShiftCipherDecrypter import *

# QPEG WRQP C VKOG KP C XKDTCPV HQTGUV, C ITQWR QH CPKOCNU NKXGF JCTOQPKQWUNA. VJG UWP UJQPG DTKIJVNA GCEJ FCA, ECUVKPI YCTO NKIJV QXGT VJG ITGGPGTA. VJG DKTFU UCPI DGCWVKHWN OGNQFKGU, YJKNG VJG USWKTTGNU RNCAGF COQPI VJG VTGGU. QPG FCA, C AQWPI TCDDKV PCOGF OCZ FGEKFGF VQ GZRNQTG C PGY RCTV QH VJG HQTGUV. JG JQRRGF CNQPI, EWTKQWU CDQWV YJCV JG OKIJV HKPF. CU JG TQWPFGF C EQTPGT, JG ECOG CETQUU C INKUVGPKPI UVTGCO. VJG YCVGT HNQYGF ENGCTNA, TGHNGEVKPI VJG DNWG UMA CDQXG. OCZ FTCPM UQOG YCVGT, HGGNKPI TGHTGUJGF. UWFFGPNA, JG JGCTF C PQKUG DGJKPF JKO. VWTPKPI CTQWPF, JG UCY C HTKGPFNA FGGT PCOGF NKNC. UJG UOKNGF CPF LQKPGF OCZ CV VJG UVTGCO. VQIGVJGT, VJGA UJCTGF UVQTKGU QH VJGKT CFXGPVWTGU CPF NCWIJGF CU VJGA YCVEJGF VJG UWP DGIKP VQ UGV. VJG UMA VWTPGF C DGCWVKHWN QTCPIG CPF RKPM, ETGCVKPI C URGEVCEWNCT DCEMFTQR HQT VJGKT PGY HTKGPFUJKR. HTQO VJCV FCA QP, OCZ CPF NKNC GZRNQTGF VJG HQTGUV VQIGVJGT, FKUEQXGTKPI PGY RNCEGU CPF OCMKPI WPHQTIGVVCDNG OGOQTKGU.

# WORK HARD, PLAY HARD!
# EWZS PIZL, XTIG PIZL! -> 8

def decrypt(_sentence):
    
    check_sentence = _sentence
    avaible_k = []
    time = 0

    true_sentences = []
    true_count = count_letter(check_sentence)
    true_upper = str(check_uppercase(check_sentence))

    mode, max = count_most(remove_space(_sentence))

    if check_uppercase(remove_space(remove_symbols(_sentence))) == False:
        run = False
        return run, true_sentences, true_count, true_upper, avaible_k, mode, max

    while time <27:
        if check(check_sentence):
            avaible_k = avaible_k + [time]
            true_sentences += [check_sentence]
            time += 1
            check_sentence = decrypt_shift(_sentence, time)
        else:
            time += 1
            check_sentence = decrypt_shift(_sentence, time)
    
    

    run = True

    return run, true_sentences, true_count, true_upper, avaible_k, mode, max


root = Tk()
root.title("Shift Cipher Decrypter")
root.geometry("400x400")

label = label1 = label2 = label3 = label4 = g1 = g2 = g3 = None

def clear():
    global label, label1, label2, label3, label4, g1, g2, g3
    if label: label.destroy()
    if label1: label1.destroy()
    if label2: label2.destroy()
    if label3: label3.destroy()
    if label4: label4.destroy()
    if g1: g1.destroy()
    if g2: g2.destroy()
    if g3: g3.destroy()
    


def click():
    global label, label1, label2, label3, label4, g1, g2, g3

    

    run, sentence, count, upper, avaible_k, mode, max = decrypt(e.get())

    print(run)

    if run:
        clear()

        label2 = Label(root, text="Letter frequencies of the cipher text:")
        label2.pack()

        g1 = Label(root, text= str(count), wraplength=250)
        g1.pack()

        label3 = Label(root, text="Is all the letter in uppercase?: " + str(upper))
        label3.pack()

        for y in range (len(sentence)):
            label1 = Label(root, text="the original text is: ")
            label1.pack()

            g2 = Label(root, text= str(sentence[y]), wraplength=250)
            g2.pack()

            label4 = Label(root, text=str("possible value(s) of k: " + str(avaible_k[y])))
            label4.pack()
        
        g3 = Label(root, text= "Most appeared letter in Cipher text is " + str(mode) + " with " + str(max) + "times", wraplength=250)
        g3.pack()
    else:
        clear()
        label = Label(root, text="Please enter text with uppercase please")
        label.pack()


e = Entry(root, width = 150)
e.pack()


button = Button(root, text="Enter your cipher text", command=click)
button.pack()


root.mainloop()

