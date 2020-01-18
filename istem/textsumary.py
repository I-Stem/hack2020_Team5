import os
import sys
import re
import spacy

text = """The Indian Space Research Organisation (ISRO, /ˈɪsroʊ/) (Hindi; IAST: bhārtīya antrikṣ anusandhān saṅgṭhan) is the space agency of the Government of India and has its headquarters in the city of Bengaluru. Its vision is to "harness space technology for national development while pursuing space science research & planetary exploration".[8] The Indian National Committee for Space Research (INCOSPAR) was established in the tenure of Jawaharlal Nehru[9][10][11][12][13] under the Department of Atomic Energy (DAE) in 1962, with the urging of scientist Vikram Sarabhai recognizing the need in space research. INCOSPAR grew and became ISRO in 1969,[14] also under the DAE.[15][16] In 1972, Government of India had setup a Space Commission and the Department of Space (DOS),[17] bringing ISRO under the DOS. The establishment of ISRO thus institutionalized space research activities in India.[18] It is managed by the DOS, which reports to the prime minister of India.[19]

ISRO built India's first satellite, Aryabhata, which was launched by the Soviet Union on 19 April 1975.[20] It was named after the mathematician Aryabhata. In 1980, Rohini became the first satellite to be placed in orbit by an Indian-made launch vehicle, SLV-3. ISRO subsequently developed two other rockets: the Polar Satellite Launch Vehicle (PSLV) for launching satellites into polar orbits and the Geosynchronous Satellite Launch Vehicle (GSLV) for placing satellites into geostationary orbits. These rockets have launched numerous communications satellites and Earth observation satellites. Satellite navigation systems like GAGAN and IRNSS have been deployed. In January 2014, ISRO used an indigenous cryogenic engine in a GSLV-D5 launch of the GSAT-14.[21][22]

ISRO sent a lunar orbiter, Chandrayaan-1, on 22 October 2008, which discovered lunar water in the form of ice,[23] and the Mars Orbiter Mission, on 5 November 2013, which entered Mars orbit on 24 September 2014, making India the first nation to succeed on its maiden attempt to Mars, as well as the first space agency in Asia to reach Mars orbit.[24] On 18 June 2016, ISRO launched twenty satellites in a single vehicle,[25] and on 15 February 2017, ISRO launched one hundred and four satellites in a single rocket (PSLV-C37), a world record.[26][27] ISRO launched its heaviest rocket, Geosynchronous Satellite Launch Vehicle-Mark III (GSLV-Mk III), on 5 June 2017 and placed a communications satellite GSAT-19 in orbit. With this launch, ISRO became capable of launching 4-ton heavy satellites into GTO. On 22 July 2019, ISRO launched its second lunar mission Chandrayaan-2 to study the lunar geology and the distribution of lunar water.

Future plans include development of the Unified Launch Vehicle, Small Satellite Launch Vehicle, development of a reusable launch vehicle, human spaceflight, a space station, interplanetary probes, and a solar spacecraft mission.[28]
"""

#Text Preprocessing

#text = text.lower()


def textsummary(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ',text)
    #txt_words = text.split(" ")
    nlp = spacy.load("en_core_web_sm")
    pretext = nlp(text)

    xents = pretext.ents

    nounchunks = [i for i in pretext.noun_chunks]

    print(xents)

    print("\n\n\n")


    print(nounchunks)
    print(str(len(xents))+"   "+str(len(nounchunks)))

    for i in xents:
        print(str(i) + str(i.label_) + spacy.explain(i.label_))
