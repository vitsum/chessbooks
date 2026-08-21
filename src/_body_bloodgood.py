# Сгенерировано src/pgn2body.py из «The Tactical Grob» (PGN).
# Комментарии — авторские, на английском: это прямая речь Бладгуда и Гроба.

C1 = "Часть 1. Гамбит принят: 2…Bxg4 3.c4"
C2 = "Часть 2. Большая диагональ: 3.c4 dxc4 4.b3"
C3 = "Часть 3. Открытая защита"
C4 = "Часть 4. Прочее после 1…d5"
C5 = "Часть 5. 1…e5"
C6 = "Часть 6. 1…e5 2.d3"
C7 = "Часть 7. Разное"

add("a_3_c6_4_cxd5", C1, "Вариант A · 3…c6 4.cxd5!", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 Bxg4 c4 c6 cxd5 Nf6 Qb3 Qc7 Nc3 e6 h3 Bh5 dxe6 fxe6 Qxe6+",
 {
  "2...Bxg4": "<b>Bxg4!?</b>",
  "4.cxd5": "<b>cxd5!</b>",
  "5...Qc7": "'See Bloodgood-Shepard, Variation \"B\", for 5... Qd7.'",
  "7.h3": "<b>h3!</b>",
  "9.Qxe6+": "White has much the better of this."})

add("b_3_nf6_4_cxd5_nxd5", C1, "Вариант B · 3…Nf6!? 4.cxd5 Nxd5", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 Bxg4 c4 Nf6 cxd5 Nxd5 Qb3 c6 Qxb7 Nd7 Bxd5 Rb8 Bxf7+ Kxf7 Qxa7 g6 b3 Bg7 Nc3 Rf8 Bb2 Kg8 Qa4 Ne5 Nd1 Ra8 Qe4 Bf5 Qg2 Qc7 Nc3 Rfb8 Rc1 Nc4 Ba1 Bxc3 Bxc3 Nd6",
 {
  "2...Bxg4": "<b>Bxg4!?</b>",
  "3...Nf6": "<b>Nf6!?</b> — This seemingly logical line of defense leads to complications almost immediately. There is much to be explored here, but from what has been played, White obtains an advantage in this variation.",
  "14...Ra8": "The black defenses are tied to a very precariously situated Knight, but White has to be careful because Black commands most of the board. C. Bloodgood- K. Stevens, 1960, continued"})

add("c_3_e6_4_qb3_qc8", C1, "Вариант C · 3…e6 4.Qb3 Qc8", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 Bxg4 c4 e6 Qb3 Qc8 cxd5 c6 dxc6 Nxc6 Qa4 Nf6 Bxc6+ bxc6 d3 Bh5 Bd2 Bc5 Nc3 O-O Ne4 Bb6 Rc1 Nxe4 dxe4 c5 Be3 f5 b4 Be8 Qb3 f4 Bxc5",
 {
  "2...Bxg4": "<b>Bxg4!?</b>",
  "3...e6": "This variation differs from 3...c6 in that Black sacrifices some co-ordination of his pieces for more choice in which pawn he will return.",
  "15...f5": "<b>f5!?</b>",
  "18.Bxc5": "White has a clear advantage."})

add("d_3_e5_4_cxd5", C1, "Вариант D · 3…e5 4.cxd5", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 Bxg4 c4 e5 cxd5 c6 Qb3 Qc7 Nc3 Nf6 d3 Bc5 Be3 Bxe3 fxe3 O-O e4 Na6 Nf3 Nc5 Qc2 Rfd8 b4",
 {
  "2...Bxg4": "<b>Bxg4!?</b>",
  "3...e5": "Black's purpose in playing 3...e5 is to avoid the compications arising after any direct attempt to hold the gambit pawn; since the pawn cannot be held anyway, this would seem best, but has not proven successful in practice.",
  "10.e4": "White has two sets of connected doubled pawns, which are serious threats in the center, e.g. two connected passed would not be easy for Black to cope with.",
  "13.b4": "White has the better chances!"})

add("a1_3_c4_dxc4_4_b3", C2, "Вариант A1 · 3.c4!? dxc4 4.b3!?", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 c6 c4 dxc4 b3 cxb3 Qxb3 e5 Nc3 Qb6 Qc2 Bxg4 Rb1 Qc7 Nd5 Qc8 Ne3 Be6",
 {
  "1.g4": "This solid defensive line is an attempt by Black to move the game into positional situations rather than meet the tactical possiblilities resulting from 2...Bxg4!? White has several playable alternatives now: Variation \"A1\" covers the \"Double Gambit\" 3. c4; Variation \"B1\" covers the \"Short Spike' 3. h3; and Variation \"C1\" covers the \"Spike\" 3. g5.",
  "3.c4": "<b>c4!?</b>",
  "4.b3": "<b>b3!?</b> — This is a risky gambit for White to play, but it is far from simple for Black to refute.",
  "9.Nd5": "<b>Nd5!</b>",
  "10...Be6": "White has little for the two pawns."})

add("b1", C2, "Вариант B1", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 c6 h3 e5 d3 Bc5 Nf3 Qe7 d4 exd4 Nxd4",
 {
  "3.h3": "The \"Short Spike\" is a fluid system in which White has several interesting means of disrupting the black defenses. The obvious threat of g5 discourages development of the black Knight at f6, and any attempt to attack this pawn structure to neutralize the threat has the effect of simultaneously weakening the black defenses. Should Black not play aggressively, the are still gambit possibilities for White which render the long diagonal a melting pot of double-edged tactics."})

add("c1", C2, "Вариант C1", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 c6 g5 e5 h4 Bd6 d3 Ne7 e4 d4 Nd2 Bb4 a3 Ba5 b4 Bc7 Bh3 Ng6 Nf1 Nf4 Bxf4 exf4 Qf3 O-O Bxc8 Qxc8 Nh3 f5 Nd2 fxe4 Nxe4 Qf5 Kd2 Nd7 Rag1 Ne5 Nf6+ gxf6",
 {
  "3.g5": "The \"Spike\" is a system which disrupts Black's normal lines of development and creates immediate problems for him. White has an obvious kind-side attack and to counter this, Black must react aggressively or literally expect to be pushed off the board",
  "4.h4": "<b>h4!</b>",
  "6.e4": "The move is probably best, but a little exploration here is overdue.",
  "11...Nf4": "<b>Nf4?</b>"})

add("a2", C3, "Вариант A2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 e4 dxe4 Bxe4 Nf6 Bf3 e4 Be2 Nc6 h4 Bc5",
 {
  "3.e4": "<b>e4!?</b> — This is definitely not recommended!",
  "7...Bc5": "Black threatens 8...Qd4! This is obviously not good for White."})

add("b2", C3, "Вариант B2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 Be6 Qb3 Nd7 cxd5 Bxg4 Qxb7 Rb8 Qc6 Bc5 Nc3 Rb6 Qa4",
 {
  "3...Be6": "<b>Be6!?</b>",
  "4.Qb3": "<b>Qb3!</b>",
  "9.Qa4": "with White holding the pawn at the cost of the initiative."})

add("c2", C3, "Вариант C2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 d4 d3 c6 e4 Nd7 a3 a5 Nd2 Nc5 Nf1 h5 gxh5 Qh4 Bf3 Nf6 Ng3 Ng4 h3 Nf6 Qe2 a4 Nf5 Bxf5 exf5 Bd6 h6 gxh6",
 {
  "3...d4": "This is an awkward line for Black which creates more problems than it solves.",
  "8...h5": "<b>h5!?</b> — Perhaps Black does best with 8...N e7 to g6; however the text is the most aggressive move at Black's disposal.",
  "14.Nf5": "<b>Nf5?</b>",
  "16...gxh6": "(H. Erwin-D. Stroemer, 1972) with advantage to Black."})

add("d2", C3, "Вариант D2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 dxc4 Qc2",
 {
  "4.Qc2": "This is definitely not a gambit pawn, e. g."})

add("d2a", C3, "Вариант D2a", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 dxc4 Qc2 c6 Qxc4 Be6 Qc3 Bd6 Nf3 Qc7 h3 f6 d4 Nd7 Nbd2 Ne7 e4 Ng6 Nc4 O-O-O d5 Bf7 Nxd6+ Qxd6 dxc6 Nc5 cxb7+ Kb8 O-O Nxe4 Qa5 Qd5",
 {
  "5...Be6": "<b>Be6!</b> — This is the only aggressive reply.",
  "8...f6": "<b>f6!</b>",
  "11.e4": "<b>e4!</b>",
  "13.d5": "White has some advantage, but this is very minimal.",
  "15...Nc5": "<b>Nc5!</b>",
  "17.O-O": "<b>O-O!</b>",
  "18...Qd5": "with an unclear position. (Grob-B. Brechbuhler, corr. 1966)"})

add("d2b", C3, "Вариант D2b", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 dxc4 Qc2 Qd4 Nf3 Qxg4 Rg1 Qe6 Ng5 Qf5 Qxc4 c6 Bh3",
 {
  "7.Ng5": "White has a strong attack!",
  "7...Qf5": "<b>Qf5!?</b>",
  "8.Qxc4": "<b>Qxc4!</b>",
  "9.Bh3": "<b>Bh3!</b> — (Bloodgood- R. Traylor, 1973) Winning a piece."})

add("e", C3, "Вариант E", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 Be6 Qxb7 Nbc6 Nb5 Rc8 Nf3 a6 Qxa6 Nb4 Nd6+ Kd7 Nxe5+ Kc7 Nb5+ Kb8 Qa7#",
 {
  "3...c6": "This is the key line in Grob's Attack, and the tactical aspects of the position are unlimited.",
  "6.Nc3": "While there are several lines which are playable for Black at this point, there are also several which appear playable, but which lose. Clearly bad are:",
  "6...Be6": "<b>Be6?</b>",
  "10...Nb4": "<b>Nb4?</b>",
  "14.Qa7#": "(Braune-Rupprecht, 1956) The playable lines to be considered are: Variation \"E1\" 6...d5, Variation \"E2\" 6... Nc6, and Variation \"E3\" 6... e5!?"})

add("e1", C3, "Вариант E1", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 d4 Nd5 Nbc6 Nxe7 Qxe7 h3 g6 a3 Be6 Bd5 Bxd5 Qxd5 Rd8 Qe4 Bg7 d3 O-O g5 f5 gxf6 Qxf6 Nf3 Qf7 Bg5 Bf6 h4 Rc8 h5 Bxg5",
 {
  "8.Nxe7": "<b>Nxe7!</b>",
  "11.Bd5": "' This position is not at all clear, but the maze of complications have been reduced to a managable level. '",
  "15...f5": "'!?'",
  "20.h5": "'!?'"})

add("e2", C3, "Вариант E2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 Nbc6 Nxd5 Nd4 Qc4 Nxd5 Bxd5 b5 Bxf7+ Ke7 Qd5 Nc2+ Kd1 Nxa1 Qxa8 Qc7 Qe4 Kxf7 f3 Be6 Qb1 Be7 Qxa1 Rc8",
 {
  "7...Nd4": "<b>Nd4!</b>",
  "13...Qc7": "<b>Qc7!</b>",
  "14.Qe4": "<b>Qe4!</b>"})

add("e3", C3, "Вариант E3", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3 exd3 Bf4 dxe2 Ngxe2 Ng6 Bxd5 Qd7 Bg3 Nc6 O-O-O Bc5 Ne4 Bb6 Bxf7+",
 {
  "6...e4": "<b>e4!?</b> — While this line of play is very complicated, it is also probably Black's best.",
  "8.Bf4": "<b>Bf4!</b> — From the diagram position shown, the following are not good:",
  "8...dxe2": "<b>dxe2?</b>",
  "13.Ne4": "with a solid advantage for White.",
  "14.Bxf7+": "(Grob- W. Kast, /corr 1965) The playable lines are: Variation \"E3a\" 8...Ng6!?; Variation \"E3b\" 8...a6; Variation \"E3c\" 8... d2+!?"})

add("e3a", C3, "Вариант E3a", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3 exd3 Bf4 Ng6 Bxd5 Nxf4 Qa4+ Nd7 Qxf4 Nf6 Bf3 d2+ Kf1 Qb6 Rd1 Qxb2 Qe3+ Be6 Rxd2",
 {
  "8...Ng6": "<b>Ng6!?</b> — This line is the weakest of the three for Black.",
  "10.Qa4+": "10. Bxf7 is not good.",
  "12.Bf3": "<b>Bf3!</b>",
  "15.Qe3+": "White hs the better of this, and possibly enough to discourage this line for Black altogether.",
  "16.Rxd2": "(Grob-W. Blatti, corr 1964) with a solid advantage for White."})

add("e3b", C3, "Вариант E3b", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3 exd3 Bf4 a6 Rd1 d4 Rxd3 Nbc6 e3 Ng6 Bxc6+ bxc6 Rxd4 Qa5 Re4+ Be6 Rxe6+ fxe6 Qxe6+ Ne7 Ne2 Rd8 Nd4 Qb6 O-O Qxb2 Ne4 Rxd4",
 {
  "6...e4": "<b>e4!?</b>",
  "8...a6": "This is safe, but offers Black no more than equality if he avoids the balance of the traps in his path.",
  "10...Nbc6": "White has a clear advantage, but Black may be able to gradually off-set this with good play.",
  "11...Ng6": "<b>Ng6!</b>",
  "14...Be6": "<b>Be6!?</b>",
  "15.Rxe6+": "<b>Rxe6+!</b>",
  "19...Qxb2": "<b>Qxb2?</b>"})

add("e3c", C3, "Вариант E3c", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3 exd3 Bf4 d2+ Kf1 Nbc6 Bg3",
 {
  "6...e4": "<b>e4!?</b>",
  "8.Bf4": "<b>Bf4!</b>",
  "8...d2+": "<b>d2+!?</b> — This line of play has proven very double-edged, and may well be Black's best."})

add("a3", C4, "Вариант A3", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e6 d3 Bc5 h4 Nc6 Nc3 Bd7 e4 d4 Nce2 e5 Ng3 Nge7 Nf5 Nxf5 gxf5 f6 Qh5+ Ke7 a3 Qe8 Qxe8+ Raxe8 h5 h6 Nf3 Reg8 Nh4 Be8 Bf3",
 {
  "1...d5": "After",
  "2.Bg2": ", Black has a number of playable alternatives which for the most part have not been examined in any detail. While Part 4 will serve s a general guide for play against several of these, it is by no means definitive. Variation A3 covers 2...e6 and Variation B3 covers other second moves for Black.",
  "2...e6": "This passive defense is tempting, and the aggressive player may well wish to attempt to break it open quickly, but it is not weak by any means and should be treated with respect.",
  "5.Nc3": "White's king's side pressure is obvious, and must be countered. To allow White a free hand on the king's side invites disaster.",
  "5...Bd7": "<b>Bd7!?</b>",
  "17.Bf3": "(H. Grob-Weidemeier, corr, 1965) with mounting pressure."})

add("b3", C4, "Вариант B3", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 b5 e4 dxe4 Bxe4 c6 h3 Nf6 Bg2 Be6 Nc3 b4 Ne4 Nxe4 Bxe4 Bd5 Qf3 e5 d3 Nd7 Bxd5 cxd5 Qxd5",
 {
  "2...b5": "Of the remaining alternative for Black at move two, this is the line with the most possibilities. Others are playable.",
  "11...Nd7": "<b>Nd7?</b>",
  "13.Qxd5": "with advantage to White. H. Grob-G. Pinter, corr."})

add("a4", C5, "Вариант A4", "÷", "÷ по Бладгуду",
 "g4 e5 Bg2 h5 gxh5 Rxh5 e3 Rh8 c4 f5 Qc2 g6 Nc3 c6 Nge2 Nf6 d4 d6 Bd2 Be6 d5 cxd5 cxd5 Bf7 Qa4+ Nbd7 Rc1 a6 Ng3 Be7 O-O b5 Qb3 Nc5 Qc2 e4 f3 exf3 Bxf3 b4",
 {
  "2.Bg2": "While 2 Bg2 d5 transposes to Part III, this defence generally brings about a radical difference in the basic motifs of attack. Several lines not recommended for White include:",
  "4...Rh8": "<b>Rh8!</b>"})

add("a5", C6, "Вариант A5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 h6 e4 Nc6 Nc3 Nge7 h4 d5 Bg2 d4 Nd5 Be6 g5 hxg5 hxg5 Rxh1 Bxh1 Ng6 Qh5 Nf4 Nxf4 exf4 Bxf4 Qd7 Nf3 O-O-O Ne5 Nxe5 Bxe5 Bd6 Bxg7 Bg4 Qh6 Bf4 Bf6 Rg8 f3 Be6",
 {
  "11...Nf4": "<b>Nf4?</b>",
  "16...Bd6": "<b>Bd6?</b>",
  "17.Bxg7": "<b>Bxg7!</b>"})

add("b5", C6, "Вариант B5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 h5 g5 h4 Bh3 d6 Bxc8 Qxc8 h3",
 {
  "2.d3": "<b>d3!</b>",
  "2...h5": "This line of play lacks sting! White should get an advantage with proper play.",
  "6.h3": "White has the better of this in several ways. First, the Black KRP is a problem for the second player to defend. Add to this the delays Black faces in developing his King-side because of the \"Spike\" pawn while White can free his pieces easily."})

add("c5", C6, "Вариант C5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 Nc6 c4 d6 e4 h6 Nc3 Nge7 h4 Ng6 Bh3 Nf4 Be3 Nb4 Bxf4 exf4 Qa4+ Nc6 Nf3 Bd7 Qb3 b6 O-O-O Be7 Nd5 Be6 Qb5 Bd7 g5 Bxh3 Rxh3 Qd7 Nxe7 Nxe7 Qxd7+ Kxd7 Re1 Ng6",
 {
  "2...Nc6": "This seemingly logical development does little to counter-act White's basic King-side threats.",
  "7.Bh3": "Black is virtually committed to exchanging his King-Knight, after which White has a strong attack on the King-side."})

add("d5", C6, "Вариант D5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 Be7 Nf3 d6 h3 f5 g5 f4 h4 Bg4 Nbd2 h6 Bg2 hxg5 hxg5 Rxh1+ Bxh1 Nc6 Ne4 Bxf3 Bxf3 Bxg5 Bh5+ Kd7 e3 Bh6 Qg4+ Ke7 exf4 Nd4 fxe5 Nxc2+ Kd1 Nxa1 Bxh6 gxh6 Qg7+",
 {
  "2.d3": "<b>d3!</b>",
  "2...Be7": "This counters the threat of g5 very effectively, and although this line has not been explored in any detail, the potential is definitely there.",
  "5.g5": "The position is certainly far from clear, but it is equally apparent that Black will encounter some difficulty on the King-side.",
  "10...Nc6": "<b>Nc6!?</b>",
  "20.Qg7+": "Bloodgood-H. Fuller, 1973 Black resigned"})

add("e5", C6, "Вариант E5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 Bc5 h4 d5 g5 Bg4 c4 Ne7 Bg2 Be6 Qb3 Bb6 Nc3 dxc4 Qb5+ Nbc6 dxc4 a6 Qa4 O-O Bh3 Bxh3 Nxh3 f5 c5 Ba7 Qc4+ Kh8 h5 Nd4 Nd1 Qe8 h6 g6 f4 Rd8 fxe5 Nec6",
 {
  "2...Bc5": "This is Black's most aggressive reply and must be treated with respect. Several lines of play are good for White at this point.",
  "5.c4": "<b>c4!</b>",
  "7...Bb6": "White clearly has the initiative, but there are complications.",
  "8...dxc4": "<b>dxc4?</b>"})

add("f5", C6, "Вариант F5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 d6 e4 Nc6 h3 g6 Bg2 h5 g5 Nge7 Nc3 Be6 Nd5 Bg7 c3",
 {
  "2...d6": "This passive line should offer White no problems. Grob suggests:",
  "9.c3": "with White standing better.."})

add("g5", C6, "Вариант G5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 d5 Bg2 c6 e4 Bc5 Qe2 d4 g5 Be6 f4 exf4 Bxf4 Ne7 Nd2 Bb4 a3 Ba5 b4 Bb6 Bh3 Bxh3 Nxh3 O-O Nc4 Bc7 O-O-O Bxf4+ Nxf4 Ng6 Rdf1 Nxf4 Rxf4 Nd7 Rhf1 Qe7 Qg4 Ne5",
 {
  "2...d5": "This effectively hinders the White thrust e4, while also directly countering White's initiative on the King-side. Not to be overlooked is the possiblility of Black developing a Queen-side attack.",
  "4...Bc5": "<b>Bc5!</b>",
  "5...d4": "White has a very minimal edge, and the position is quite double-edged."})

add("a6", C7, "Вариант A6", "÷", "÷ по Бладгуду",
 "g4 Nf6 g5 Nd5 d4 e6 a3 Be7 e4 Nb6 f4",
 {
  "1...Nf6": "<b>Nf6!?</b> — This is not very effective, and is not recommeded.",
  "6.f4": "White clearly has the better chances."})

add("b6", C7, "Вариант B6", "÷", "÷ по Бладгуду",
 "g4 h5 g5 h4 d4 d6 Qd3 g6 Bg2 Nc6 c3 Bd7 Na3",
 {
  "1...h5": "An immediate challenge to White's K-side ambition which is very double-edged .",
  "2.g5": "Of doubtful value is 2.gxh5!? which does nothing for White and merely opens the Rook-file for Black.",
  "7.Na3": "White has an advantage."})

add("c6", C7, "Вариант C6", "÷", "÷ по Бладгуду",
 "g4 g5 h4 e6 Nf3 Be7 hxg5 Bxg5 Nxg5 Qxg5 e4 Nf6 d4",
 {
  "1...g5": "<b>g5!?</b> — This allows White to hold the initiative for a long time.",
  "2.h4": "<b>h4!</b>",
  "3.Nf3": "<b>Nf3!</b>",
  "6...Nf6": "This move seems sharper than it is; Grob.",
  "7.d4": "Black now has an awkwardly placed Queen and nothing is seriously threatened."})

add("d6", C7, "Вариант D6", "÷", "÷ по Бладгуду",
 "g4 g6 Bg2 h6 e4 Bg7 d4 e6 Nf3 d5 Nbd2 dxe4 Nxe4 Nf6 Nxf6+ Bxf6",
 {
  "1...g6": "Should the Grob become a popular opening, this defense will undoubtedly become a major line, but for the present it is still among the seldom played variations.",
  "8...Bxf6": "The position is not clear."})

add("e6", C7, "Вариант E6", "÷", "÷ по Бладгуду",
 "g4 b5 Bg2 c6 a4 d5 axb5 Nf6 c4",
 {
  "1...b5": "<b>b5!?</b> — This counter play on the long diagonal is hardly good for Black.",
  "3.a4": "<b>a4!</b>",
  "5.c4": "<b>c4!</b> — White has much the better of this!"})

add("f6", C7, "Вариант F6", "÷", "÷ по Бладгуду",
 "g4 c5 Bg2 Nc6 e4 e5 d3 Nge7 h4 d5 Nc3",
 {
  "1...c5": "This line can transpose into a sicilian Defense, but it not likely to create the same problems for White."})

add("g6", C7, "Вариант G6", "÷", "÷ по Бладгуду",
 "g4 c6 c4 d5 Qb3 Qc7 cxd5 cxd5 Nc3 e6 d4",
 {
  "1...c6": "This is decidedly inferior to 1...d5.",
  "6.d4": "White has some advantage, and somewhat more freedom for his pieces."})

add("h6", C7, "Вариант H6", "÷", "÷ по Бладгуду",
 "g4 d6 Bg2 e5 d3 c6 e4 d5 h3 d4 Nf3 f6 Nh4 g5 Nf5 Ne7 h4 Ng6 hxg5 fxg5 Rh5 Nf4 Bxf4 exf4 Nd2 Bxf5 exf5 h6 Qe2+",
 {
  "1...d6": "This is passive and while not exactly bad, it hardly poses any major threats.",
  "5.h3": "Black has lost a tempo",
  "5...d4": "<b>d4!?</b>",
  "7...g5": "<b>g5?</b>",
  "14...h6": "<b>h6?</b>",
  "15.Qe2+": "with a solid advantage to White. Grob-Suhner, Corr."})

add("i6", C7, "Вариант I6", "÷", "÷ по Бладгуду",
 "g4 e6 d3 d5 Bg2 c5 c4 d4 Qb3 Qc7 Nd2 Nc6 Ne4 Nf6 g5 Nxe4 Bxe4 Be7 h4 h6 Nh3 hxg5 hxg5 e5 Bg2 g6 Bd2 Qb6 O-O-O Qxb3 axb3 a5 f4 Bxh3 Rxh3 Rxh3 Bxh3 exf4 Bxf4 a4",
 {
  "1...e6": "This apparently Innocent defense is not simple for White to handle, and several pitfalls must be examined.",
  "4.c4": "White has the initiative and potential threats on both flanks!",
  "14...Qb6": "<b>Qb6!?</b>",
  "17...Bxh3": "<b>Bxh3?</b>"})

SUBS = {
 "a_3_c6_4_cxd5": {
  "4.cxd5": [   [    "вместо cxd5",
    "Qb3 Qc7 cxd5 cxd5 Nc3 d4 Nb5 Qb6 Bxb7 Be6",
    "before"
   ]
  ],
  "4...Nf6": [   [    "вместо Nf6",
    "Qc7 Nc3 Nf6 h3 Bd7 e4 e6 dxe6 Bxe6 d4",
    "before"
   ],
   [    "вместо Nf6",
    "Qb6 Nc3 e5 Qc2 Nf6 a4 a5 d3 cxd5 Nxd5",
    "before"
   ],
   [    "вместо Nf6",
    "cxd5 Qb3 Nf6 Nc3 e6 Qxb7 Nbd7 d4 Rb8 Qxa7",
    "before"
   ],
   [    "вместо Nf6",
    "Qa5 Qb3 Qb6 Qg3 Nf6 Nc3 Bd7 e4 Na6 Nge2",
    "before"
   ]
  ],
  "5.Qb3": [   [    "вместо Qb3",
    "Nc3 Bd7 Qb3 Qc8 d4 e6 e4 exd5 exd5 Be7",
    "before"
   ]
  ],
  "5...Qc7": [   [    "вместо Qc7",
    "Qb6 dxc6 Nxc6 Qxb6 axb6 Nc3 e5 b3 Nd4 Kd1",
    "before"
   ],
   [    "вместо Qc7",
    "Qc8 Nc3 e6 h3 Bh5 dxe6 fxe6 Na4 b6 d4",
    "before"
   ]
  ],
  "6...e6": [   [    "вместо e6",
    "Nxd5 Nxd5 cxd5 Bxd5 Bc8 Bxf7+ Kd8 Nf3 Nc6 Bg8",
    "before"
   ]
  ],
  "7.h3": [   [    "вместо h3",
    "dxc6 Nxc6 d3 a6 Be3 Be7 Bb6 Qd7 Nh3 e5",
    "before"
   ]
  ],
  "7...Bh5": [   [    "вместо Bh5",
    "Bf5 e4 Bg6 dxe6 fxe6 Qxe6+",
    "before"
   ]
  ]
 },
 "b_3_nf6_4_cxd5_nxd5": {
  "4.cxd5": [   [    "вместо cxd5",
    "Qb3 e6 Qxb7 Nbd7 cxd5 exd5 Qb3 Nc5 Qc2 Qd7",
    "before"
   ]
  ],
  "4...Nxd5": [   [    "вместо Nxd5",
    "Qd7 Qb3 c6 Nc3 e6 h3 Bh5 dxe6 fxe6 Nf3",
    "before"
   ]
  ],
  "5...c6": [   [    "вместо c6",
    "e6 Qa4+",
    "before"
   ]
  ],
  "6...Nd7": [   [    "вместо Nd7",
    "Nb6 Bxc6+ Bd7 Bxd7+ Qxd7 Qxd7+ N8xd7 b3 e6 Bb2",
    "before"
   ],
   [    "вместо Nd7",
    "Qc7 Qxa8 Nb6 Bxc6+ Bd7 Qb7 Qxc6 Qxc6",
    "before"
   ]
  ],
  "7.Bxd5": [   [    "вместо Bxd5",
    "Qxc6 Rc8",
    "before"
   ]
  ],
  "7...Rb8": [   [    "вместо Rb8",
    "cxd5 Qxd5 Nb6 Qg2 Rc8 Nc3 Bd7 b3 Bc6 Nf3",
    "before"
   ]
  ],
  "8.Bxf7+": [   [    "вместо Bxf7+",
    "Qxc6 Rc8",
    "before"
   ]
  ],
  "9...g6": [   [    "вместо g6",
    "e5 f3 Bc5 Qa4 Bd4 Nc3 Qf6 Ne4 Qf4 d3",
    "before"
   ]
  ],
  "11...Rf8": [   [    "вместо Rf8",
    "Nb6 Bb2 Ra8 Qb7 Bd7 a4 Nd5 Nf3 Rf8 e4",
    "before"
   ]
  ],
  "12...Kg8": [   [    "вместо Kg8",
    "Bh5",
    "before"
   ]
  ]
 },
 "c_3_e6_4_qb3_qc8": {
  "4.Qb3": [   [    "вместо Qb3",
    "cxd5 exd5 Qb3 Qc8 Bxd5 Nc6 Bxf7+ Ke7 Bxg8 Rxg8",
    "before"
   ]
  ],
  "4...Qc8": [   [    "вместо Qc8",
    "Nf6 Qxb7 Nbd7 cxd5 Rb8 Qc6 Rb6 Qa4 exd5 Bxd5",
    "before"
   ],
   [    "вместо Qc8",
    "Nd7 cxd5 Nc5 Qe3 Be7 Nc3 Nf6 d4 Ncd7 h3",
    "before"
   ]
  ],
  "7.Qa4": [   [    "вместо Qa4",
    "Nc3 Nf6 d3 Bb4 Bd2 e5 Rc1",
    "before"
   ]
  ],
  "8...bxc6": [   [    "вместо bxc6",
    "Qxc6 Qxc6+ bxc6 b3 Bc5 Bb2 O-O Nc3 Nd5 O-O-O",
    "before"
   ]
  ],
  "10...Bc5": [   [    "вместо Bc5",
    "Be7 Nc3 Nd5 O-O-O O-O Ne4 c5 Kb1 Bg6 Rc1",
    "before"
   ]
  ],
  "13...Nxe4": [   [    "вместо Nxe4",
    "Ng4 Rxc6 Qd7 Rc4 Qxa4 Rxa4 f5 f3 fxe4 fxg4",
    "before"
   ]
  ],
  "15...f5": [   [    "вместо f5",
    "a5 Qb5 Qc7 Bxc5 Bxc5 Rxc5 Qe7 Rxh5",
    "before"
   ]
  ]
 },
 "d_3_e5_4_cxd5": {
  "2...Bxg4": [   [    "вместо Bxg4",
    "e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3",
    "before"
   ]
  ],
  "4.cxd5": [   [    "вместо cxd5",
    "Qb3 Qc8 Nc3 c6 cxd5 Nf6 d3 Bc5 Bg5 Qf5",
    "before"
   ]
  ],
  "4...c6": [   [    "вместо c6",
    "Nf6 Qb3 Qc8 Nc3 Na6 d6 c6 Nb5 cxb5 Qxb5+",
    "before"
   ]
  ],
  "5...Qc7": [   [    "вместо Qc7",
    "Qb6 dxc6 Nxc6 Qxb6 axb6 Nc3 Nd4 Kd1 Bb4 Nd5",
    "before"
   ]
  ],
  "7...Bc5": [   [    "вместо Bc5",
    "Na6 dxc6 Nc5 Qb5 a6 cxb7+ axb5 bxa8=Q+",
    "before"
   ],
   [    "вместо Bc5",
    "Nxd5 Nxd5 cxd5 Bxd5 Bc8 Bd2 Nc6 Rc1 Bd6 Ba5",
    "before"
   ]
  ],
  "9...O-O": [   [    "вместо O-O",
    "Nxd5 Nxd5 cxd5 Bxd5 Bc8 Nf3",
    "before"
   ]
  ],
  "10.e4": [   [    "вместо e4",
    "dxc6 Nxc6 Nb5 Qb6 Nd6 Qxb3 axb3 Bc8",
    "before"
   ]
  ],
  "11...Nc5": [   [    "вместо Nc5",
    "Bxf3 Bxf3",
    "before"
   ]
  ]
 },
 "a1_3_c4_dxc4_4_b3": {
  "3...dxc4": [   [    "вместо dxc4",
    "Bxg4",
    "before"
   ]
  ],
  "4.b3": [   [    "вместо b3",
    "Na3 Bxg4 Nxc4 Nd7 d4 e5 dxe5 Bb4+ Kf1 Nxe5",
    "before"
   ],
   [    "вместо b3",
    "h3 h5 g5 e5 h4 Be6 Qc2 Nd7 g6 f5",
    "before"
   ]
  ],
  "4...cxb3": [   [    "вместо cxb3",
    "Bxg4 bxc4 e6 Qb3 Qc7 h3 Bf5 e4 Bg6 d4",
    "before"
   ],
   [    "вместо cxb3",
    "Qd4 Nc3 Bxg4 Rb1 Nf6 bxc4 Qd7 Qb3 b6 c5",
    "before"
   ]
  ],
  "5...e5": [   [    "вместо e5",
    "Qd4 Nc3 Qb6 Qa4 Na6 Rb1 Qc7 d4",
    "before"
   ]
  ],
  "6.Nc3": [   [    "вместо Nc3",
    "Bb2 Bd6 Nf3 Nd7 d4 exd4 Bxd4 Ngf6 h3 Qe7",
    "before"
   ]
  ],
  "6...Qb6": [   [    "вместо Qb6",
    "h5 Nf3 Bd6 Ne4 hxg4 Nfg5 Nh6 Nxd6+ Qxd6 Ne4",
    "before"
   ],
   [    "вместо Qb6",
    "Nf6 g5 Nfd7 Nf3 Nc5 Qc2 Bd6 Ne4 Nxe4 Qxe4",
    "before"
   ],
   [    "вместо Qb6",
    "f6 g5 Nd7 gxf6 Ngxf6 Nf3 Bd6 Ng5 Qe7 d4",
    "before"
   ]
  ],
  "8...Qc7": [   [    "вместо Qc7",
    "Qa6 Qe4 Be6 Qxe5",
    "before"
   ]
  ]
 },
 "b1": {
  "3...e5": [   [    "вместо e5",
    "h5 g5 e5 h4 f5 d3 g6 b3 Rh7 Bb2",
    "before"
   ],
   [    "вместо e5",
    "g5 Nf3 h5 gxh5 Rxh5 d3 Bg7 Nbd2 f5 d4",
    "before"
   ],
   [    "вместо e5",
    "e6 d3 Bd6 Nf3 Nd7 Nbd2 h5 g5 f6 h4",
    "before"
   ],
   [    "вместо e5",
    "f5 g5 e5 d3 h6 h4 f4 e4 hxg5 h5",
    "before"
   ],
   [    "вместо e5",
    "Nf6 c4 dxc4 Na3 Be6 Qa4 Bd5 f3 b5 Qc2",
    "before"
   ]
  ],
  "4.d3": [   [    "вместо d3",
    "e4 Ne7 d3 Ng6 exd5 Nh4 Kf1 Nxg2 Kxg2 cxd5",
    "before"
   ]
  ],
  "4...Bc5": [   [    "вместо Bc5",
    "Ne7 Nf3 Ng6 Nc3 Be7 e4 d4 Ne2 Nh4 Nxh4",
    "before"
   ],
   [    "вместо Bc5",
    "h6 Nd2 Nf6 c4 Be6 Qb3 Nbd7 Ngf3 Qc7 Qc2",
    "before"
   ]
  ],
  "5.Nf3": [   [    "вместо Nf3",
    "Nc3 Be6 e4 Ne7 Nf3 Ng6 exd5 cxd5 d4 exd4",
    "before"
   ]
  ],
  "5...Qe7": [   [    "вместо Qe7",
    "Nd7 e4 Ngf6 Qe2 Qc7 exd5 cxd5 d4 Bd6 dxe5",
    "before"
   ],
   [    "вместо Qe7",
    "Qb6 O-O Nd7 Nbd2 Ne7 e4 Ng6 exd5 cxd5 Qe1",
    "before"
   ],
   [    "вместо Qe7",
    "Qf6 Bg5 Qg6 Qd2 f6 Bh4 Be6 g5 fxg5 Nxg5",
    "before"
   ]
  ]
 },
 "c1": {
  "3...e5": [   [    "вместо e5",
    "g6 d3 Nd7 e4 Nc5 Nc3 Bg7 Nge2 dxe4 Nxe4",
    "before"
   ],
   [    "вместо e5",
    "Bf5 d3 Nd7 e4 dxe4 dxe4 Bg6 h4 h5 f4",
    "before"
   ]
  ],
  "4.h4": [   [    "вместо h4",
    "d3 Bg4 h3 Bh5 Bf3 Bxf3",
    "before"
   ]
  ],
  "4...Bd6": [   [    "вместо Bd6",
    "Bc5 d3 d4 Nf3 Qd6 Nbd2 Be6 Ne4 Qd5 Nfd2",
    "before"
   ],
   [    "вместо Bd6",
    "Be6 d3 Bd6 e4 Ne7 Nc3 Nd7 Bh3 Bxh3 Nxh3",
    "before"
   ],
   [    "вместо Bd6",
    "g6 d3 Bg7 h5 gxh5 Rxh5 Bg4 Rh4 Bf5 e4",
    "before"
   ],
   [    "вместо Bd6",
    "f5 d3 Bc5 e3 Bb6 b3 Be6 Bb2 Nd7 Qe2",
    "before"
   ]
  ],
  "5.d3": [   [    "вместо d3",
    "e4 dxe4 Nc3 f5 gxf6 Nxf6 Nxe4 O-O d3 Nxe4",
    "before"
   ]
  ],
  "5...Ne7": [   [    "вместо Ne7",
    "Be6 e4 Ne7 Nd2 O-O Bh3 Bxh3 Nxh3 f5 gxf6",
    "before"
   ],
   [    "вместо Ne7",
    "Bg4 Nd2 f5 f3 Bh5 e4 fxe4 dxe4 dxe4 Nxe4",
    "before"
   ]
  ],
  "6...d4": [   [    "вместо d4",
    "Be6 h5 Nd7 Nc3 Qb6 Qf3 O-O Bh3 Bxh3 Qxh3",
    "before"
   ],
   [    "вместо d4",
    "O-O Nc3 d4 Nce2 f5 gxf6 Rxf6 h5 Qf8 f3",
    "before"
   ],
   [    "вместо d4",
    "O-O Nc3 Be6 Bh3 Bxh3 Nxh3 d4 Ne2 f5 gxf6",
    "before"
   ],
   [    "вместо d4",
    "O-O Nc3 Be6 Bd2 Nd7 h5 d4 Nce2 c5 Bh3",
    "before"
   ]
  ],
  "7.Nd2": [   [    "вместо Nd2",
    "Bh3 Bxh3 Nxh3 O-O Qg4 Qd7 Qg3",
    "before"
   ]
  ],
  "10...Ng6": [   [    "вместо Ng6",
    "Bxh3 Nxh3 O-O f4 exf4 Qg4 f5 gxf6 Rxf6 Nf3",
    "before"
   ]
  ],
  "11...Nf4": [   [    "вместо Nf4",
    "Bxh3",
    "before"
   ]
  ]
 },
 "a2": {
  "5.Bf3": [   [    "вместо Bf3",
    "f3 Nxe4 fxe4 Qh4+",
    "before"
   ]
  ]
 },
 "b2": {
  "3...Be6": [   [    "вместо Be6",
    "Bxg4 Qb3 Bc8 cxd5",
    "before"
   ]
  ],
  "4...Nd7": [   [    "вместо Nd7",
    "b6 cxd5 Bxg4 Qg3 Nf6 Qxe5+",
    "before"
   ]
  ],
  "7.Qc6": [   [    "вместо Qc6",
    "Qxa7 Bc5",
    "before"
   ]
  ]
 },
 "c2": {
  "4.d3": [   [    "вместо d3",
    "b4 c6 h3 Be6 Qb3 b5 d3 Be7 a4 bxc4",
    "before"
   ]
  ],
  "5.e4": [   [    "вместо e4",
    "h3 Be6 Nf3 Nd7 Ng5 Qe7 a3 f6 Nxe6 Qxe6",
    "before"
   ]
  ],
  "5...Nd7": [   [    "вместо Nd7",
    "dxe3 Bxe3 f5 gxf5 Bxf5 Nf3 Bb4+ Nbd2 Qa5 Qb3",
    "before"
   ]
  ],
  "6.a3": [   [    "вместо a3",
    "Nd2 Ne7 Nf1 Ng6 Nf3 Bb4+ Ke2 Nf6 h3 h6",
    "before"
   ]
  ],
  "7...Nc5": [   [    "вместо Nc5",
    "Qb6 h3 Bd6 Nf1 Ne7 Ne2 Ng6 h4 h5 g5",
    "before"
   ]
  ],
  "9.gxh5": [   [    "вместо gxh5",
    "g5 h4 Bh3 Be7 Bxc8 Qxc8 Qf3 f6 g6 Nh6",
    "before"
   ]
  ]
 },
 "d2": {
  "4.Qc2": [   [    "вместо Qc2",
    "Qa4+ c6 Qxc4",
    "before"
   ],
   [    "вместо Qc2",
    "b3 Qd4 Nc3 Qxg4 Bh3 Qg6 Bxc8 Qg2",
    "before"
   ]
  ]
 },
 "d2a": {
  "6.Qc3": [   [    "вместо Qc3",
    "Qa4 Bd5 Nf3 e4 Nd4 Qh4 h3 Qg5 Nc3 Nf6",
    "before"
   ],
   [    "вместо Qc3",
    "Qe4 Nd7",
    "before"
   ]
  ],
  "6...Bd6": [   [    "вместо Bd6",
    "Nd7 h3 Ngf6 a3 a5 Qg3 Bd6 Nc3 Nc5 Qh4",
    "before"
   ]
  ],
  "7.Nf3": [   [    "вместо Nf3",
    "h3 f6 a3 Qb6 b4 a5 Nf3 axb4 axb4 Rxa1",
    "before"
   ]
  ],
  "7...Qc7": [   [    "вместо Qc7",
    "f6 h3 Ne7 e4 Ng6 d3 Nd7 Be3 Nf4 Bf1",
    "before"
   ],
   [    "вместо Qc7",
    "Nd7 h3 Ne7 Na3 O-O Nc4 Bc7 Ncxe5 Nxe5 Nxe5",
    "before"
   ]
  ],
  "8...f6": [   [    "вместо f6",
    "Nd7 Ng5 Nc5 b4 Nd7 Nxe6 fxe6 Qb3",
    "before"
   ],
   [    "вместо f6",
    "Na6 Ng5 Qd7 Nxe6 Qxe6 Bxc6+ Ke7 Bxb7",
    "before"
   ]
  ],
  "10.Nbd2": [   [    "вместо Nbd2",
    "Be3 Ne7",
    "before"
   ]
  ],
  "11...Ng6": [   [    "вместо Ng6",
    "O-O Nc4 Ng6 Nxd6 Qxd6 Be3 Rac8 Rd1 Qb8 O-O",
    "before"
   ],
   [    "вместо Ng6",
    "a5 a3 b5 d5 Bf7 O-O O-O dxc6 Nxc6 Qe3",
    "before"
   ],
   [    "вместо Ng6",
    "O-O-O",
    "before"
   ]
  ],
  "13...Bf7": [   [    "вместо Bf7",
    "cxd5 Nxd6+",
    "before"
   ]
  ],
  "15.dxc6": [   [    "вместо dxc6",
    "Be3",
    "before"
   ]
  ]
 },
 "d2b": {
  "5...Qxg4": [   [    "вместо Qxg4",
    "Qc5 Na3 Be6 Ng5 Bd5 e4 Bc6 Qxc4",
    "before"
   ]
  ],
  "6...Qe6": [   [    "вместо Qe6",
    "f6 d3 cxd3 exd3 c6 Be3 Bb4+ Nc3 Qe6 Nd2",
    "before"
   ]
  ]
 },
 "e": {
  "4...cxd5": [   [    "вместо cxd5",
    "h5 dxc6 Nxc6 gxh5 Nh6 d3 Bc5 Nc3 Ng4 Bxc6+",
    "before"
   ]
  ],
  "5...Ne7": [   [    "вместо Ne7",
    "Be6 Nc3 Nd7 Bxd5 Nc5 Qb5+ Qd7 Bxe6 Nxe6 Qxe5",
    "before"
   ],
   [    "вместо Ne7",
    "e4 Nc3 Ne7 d3 f5 gxf5 Nxf5 dxe4 dxe4 Bxe4",
    "before"
   ],
   [    "вместо Ne7",
    "Qc7 Nc3 d4 Nd5 Qd7 d3 Nc6 Bd2 b6 Rc1",
    "before"
   ],
   [    "вместо Ne7",
    "Nf6 g5 Ne4 Nc3 Qxg5 Bxe4 dxe4 Nxe4 Qg2 Qb5+",
    "before"
   ]
  ],
  "6...Be6": [   [    "вместо Be6",
    "Qd7 Nxd5 Nxd5 Bxd5 Nc6 Nf3 Rb8 Rg1 Bd6 Ng5",
    "before"
   ],
   [    "вместо Be6",
    "Bxg4 Qxb7 Nbc6 Nxd5 Rc8 Nxe7 Nxe7 Qxa7",
    "before"
   ]
  ]
 },
 "e1": {
  "7.Nd5": [   [    "вместо Nd5",
    "Bxb7 Bxb7 Qxb7 Nbc6 Nb5 Rb8 Qa6 Rb6 Qa4 Qb8",
    "before"
   ]
  ],
  "7...Nbc6": [   [    "вместо Nbc6",
    "Be6 Qb5+ Nbc6 Nxe7 Qxe7 Bxc6+ bxc6 Qxc6+",
    "before"
   ],
   [    "вместо Nbc6",
    "Nxd5 Bxd5 Qc7 Nf3 Bd6 Ng5 O-O Qd3 g6 Qh3",
    "before"
   ]
  ],
  "8.Nxe7": [   [    "вместо Nxe7",
    "d3 Na5 Qa4+ Bd7",
    "before"
   ]
  ],
  "8...Qxe7": [   [    "вместо Qxe7",
    "Bxe7",
    "before"
   ]
  ],
  "9.h3": [   [    "вместо h3",
    "Qf3",
    "before"
   ]
  ],
  "10.a3": [   [    "вместо a3",
    "e3",
    "before"
   ]
  ]
 },
 "e2": {
  "7.Nxd5": [   [    "вместо Nxd5",
    "Nf3 e4 Ng5 f6 d3 fxg5 Bxg5 Qb6 Qxb6 axb6",
    "before"
   ],
   [    "вместо Nxd5",
    "e3 Be6 Qxb7 Rb8 Qa6 Nb4 Qa4+ Bd7 Qd1 d4",
    "before"
   ],
   [    "вместо Nxd5",
    "h3 Nd4 Qd1 a6 e3 Ndc6 d4 g6 dxe5 Nxe5",
    "before"
   ]
  ],
  "7...Nd4": [   [    "вместо Nd4",
    "Nxd5 Bxd5 Nd4 Qc4 b5",
    "before"
   ]
  ],
  "8...Nxd5": [   [    "вместо Nxd5",
    "b5 Nc7+ Kd7 Nxb5 Ba6 a4 Qc8 Qxc8+ Rxc8 Nxd4",
    "before"
   ]
  ],
  "9...b5": [   [    "вместо b5",
    "Be6 Bxe6 fxe6 Kf1 Rc8 Qd3 Qd5 Nf3",
    "before"
   ]
  ],
  "12.Kd1": [   [    "вместо Kd1",
    "Kf1 Nxa1 Qxa8 Qc7",
    "before"
   ]
  ],
  "14.Qe4": [   [    "вместо Qe4",
    "Bb3 Bb7 Qxa7 Kd8 Nf3 Bc5 Ng5 Bxa7 Ne6+ Kd7",
    "before"
   ]
  ],
  "14...Kxf7": [   [    "вместо Kxf7",
    "Bb7 Qf5 Bc8 Qb1 Kxf7 Nf3 Bxg4 Ng5+",
    "before"
   ]
  ],
  "15.f3": [   [    "вместо f3",
    "Nf3 Bb7 Qf5+ Ke8 Qb1 Bxf3 exf3 Qc6 Qe4 Qxe4",
    "before"
   ],
   [    "вместо f3",
    "Qf5+",
    "before"
   ],
   [    "вместо f3",
    "Qf3+ Ke8 Qc3",
    "before"
   ]
  ]
 },
 "e3": {
  "7...exd3": [   [    "вместо exd3",
    "Nbc6 dxe4 Na5 Qb5+ Bd7 Qd3 dxe4 Bxe4 Bc6 Nf3",
    "before"
   ]
  ],
  "8.Bf4": [   [    "вместо Bf4",
    "Nxd5 Nxd5 Bxd5 Bb4+",
    "before"
   ]
  ],
  "8...dxe2": [   [    "вместо dxe2",
    "d4 Nb5 d2+ Kf1 Be6 Qa4 Nec6 Nc7+ Kd7 Nxa8",
    "before"
   ],
   [    "вместо dxe2",
    "Nbc6 Nb5 d2+ Kf1 Na5 Qa4 Ng6 Nc7+ Ke7 Nxd5+",
    "before"
   ],
   [    "вместо dxe2",
    "Na6 O-O-O Ng6 Bxd5 Qf6 Be3 Bb4 Rxd3 Ne5 Rd4",
    "before"
   ]
  ],
  "11...Nc6": [   [    "вместо Nc6",
    "Bd6 Bxd6 Qxd6 Bxf7+",
    "before"
   ]
  ],
  "12.O-O-O": [   [    "вместо O-O-O",
    "Nb5 Nge5",
    "before"
   ]
  ]
 },
 "e3a": {
  "10...Nd7": [   [    "вместо Nd7",
    "Qd7 Qxf4 dxe2 Ngxe2 Bd6 Bxf7+",
    "before"
   ]
  ],
  "12.Bf3": [   [    "вместо Bf3",
    "Qe5+ Qe7 Qxe7+ Bxe7 g5 Nxd5 Nxd5 Bd8 e4 Be6",
    "before"
   ]
  ],
  "13...Qb6": [   [    "вместо Qb6",
    "Bd6 Qxd2 O-O g5 Ne8 Rd1 Qe7 Nb5 Bb8 Qd8",
    "before"
   ]
  ]
 },
 "e3b": {
  "9.Rd1": [   [    "вместо Rd1",
    "O-O-O Nec6 Rxd3 d4 Bxb8 Nb4 Rd2 Rxb8 Nf3 Be6",
    "before"
   ],
   [    "вместо Rd1",
    "Nxd5 Nxd5 Bxd5 Bb4+ Kf1 O-O Rd1 Qe7 Rxd3 Nc6",
    "before"
   ]
  ],
  "9...d4": [   [    "вместо d4",
    "dxe2 Ngxe2 Nbc6 Bxd5 Nxd5 Nxd5 Na5 Qe3+ Be6 Nc7+",
    "before"
   ],
   [    "вместо d4",
    "Nbc6 Rxd3 Na5 Qd1 Be6 Nxd5 Nxd5 Bxd5 Bb4+ Kf1",
    "before"
   ]
  ],
  "11.e3": [   [    "вместо e3",
    "Bxc6+ Nxc6 Nf3 Bc5",
    "before"
   ]
  ],
  "11...Ng6": [   [    "вместо Ng6",
    "h6 Nge2 Ng6 Bxc6+ bxc6 Rxd4",
    "before"
   ]
  ],
  "14...Be6": [   [    "вместо Be6",
    "Be7 Bd6",
    "before"
   ]
  ]
 },
 "e3c": {
  "9...Nbc6": [   [    "вместо Nbc6",
    "Qb6 Nb5 Na6 Nd6+ Kd7 Nxf7 Qxb3 axb3 Rg8 Bxd2",
    "before"
   ],
   [    "вместо Nbc6",
    "Ng6 Bxd5 Nxf4 Qa4+ Nd7 Qxf4 Nf6 Bf3 Bd6 Qxd2",
    "before"
   ],
   [    "вместо Nbc6",
    "d4 Nb5 Na6 Nd6+ Kd7 Qb5+ Ke6 Qe5+ Kd7 Nxf7",
    "before"
   ]
  ]
 },
 "a3": {
  "2.Bg2": [   [    "вместо Bg2",
    "g5 e5 h4 Bc5 c3 Nc6 b4 Bd6 Bg2 Nge7",
    "before"
   ],
   [    "вместо Bg2",
    "h3 f5 g5 e5",
    "before"
   ],
   [    "вместо Bg2",
    "f3 e6 h4 Bd6 Rh3 Qxh4+ Rxh4 Bg3#",
    "before"
   ]
  ],
  "3.d3": [   [    "вместо d3",
    "c4 dxc4 b3 cxb3 Qxb3 c6 Bb2 f6 d4 Qb6",
    "before"
   ]
  ],
  "3...Bc5": [   [    "вместо Bc5",
    "b6 c4 c6 Qa4 Bd7 Nc3",
    "before"
   ],
   [    "вместо Bc5",
    "Be7 Nf3 c6 Nc3 Qb6 e4 d4 Ne2 c5 Ne5",
    "before"
   ]
  ],
  "5...Bd7": [   [    "вместо Bd7",
    "Nge7 e4 dxe4 Nxe4 Bb6 Nh3 Ng6 Nf4 e5 Nh5",
    "before"
   ]
  ]
 },
 "b3": {
  "2...b5": [   [    "вместо b5",
    "Nc6 c4 e6 Qb3 Na5 Qa4+ c6 cxd5 exd5 Nc3",
    "before"
   ],
   [    "вместо b5",
    "c5 g5 e5 d3 Nc6 Nc3 Be6 h4 f6 e4",
    "before"
   ],
   [    "вместо b5",
    "Nf6 g5 Ne4 d3 Nxf2 Kxf2 e5 c3 c6 h4",
    "before"
   ],
   [    "вместо b5",
    "Na6 c4 e6 cxd5 exd5 Qb3 Be6 Qxb7 Nb4 Na3",
    "before"
   ],
   [    "вместо b5",
    "Nd7 d3 e6 e4 c6 Nc3 Nb6 h4 Bb4 Bd2",
    "before"
   ]
  ],
  "10...e5": [   [    "вместо e5",
    "Bxe4 Qxe4 Qd5",
    "before"
   ]
  ],
  "11...Nd7": [   [    "вместо Nd7",
    "Be7",
    "before"
   ]
  ]
 },
 "a4": {
  "2.Bg2": [   [    "вместо Bg2",
    "c4 h5 d4 hxg4 dxe5 Nc6 Qd5 Rh5 f4 Qh4+",
    "before"
   ],
   [    "вместо Bg2",
    "e4 d5 Qf3 dxe4 Qxe4 Bd6 h3 Nc6 c3 f5",
    "before"
   ],
   [    "вместо Bg2",
    "d4 e4 c4 Qh4 h3 Bb4+ Nc3 Bxc3+ bxc3 Qe7",
    "before"
   ]
  ],
  "2...h5": [   [    "вместо h5",
    "Bc5 e3 Nc6 c3 d5 d4 exd4 exd4 Qe7+ Be3",
    "before"
   ],
   [    "вместо h5",
    "Nc6 c4 Bc5 e3 d6 a3 a5 Nc3 Bd7 h3",
    "before"
   ]
  ],
  "4...Rh8": [   [    "вместо Rh8",
    "Nf6 c4 c6 Nc3 d5 cxd5 Rg5 Bf3 cxd5 Qa4+",
    "before"
   ]
  ],
  "5...f5": [   [    "вместо f5",
    "c6 Nc3 Bb4 Nge2 Qg5 Ng3 f5 d4 Bxc3+ bxc3",
    "before"
   ]
  ]
 },
 "a5": {
  "2...h6": [   [    "вместо h6",
    "g6 e4 h6 Nc3 Bg7 Be3 c6 Bg2 Ne7 h3",
    "before"
   ]
  ],
  "3.e4": [   [    "вместо e4",
    "h4 d5 e3 Nf6 Be2 a6 Nd2 Nc6 Nf1 Bc5",
    "before"
   ],
   [    "вместо e4",
    "Bg2 Nf6 h3 c6 e4 d5 Nd2 d4 Nc4 Nbd7",
    "before"
   ]
  ],
  "4.Nc3": [   [    "вместо Nc3",
    "h4 d5 Bg2 d4 g5 hxg5 hxg5 Rxh1 Bxh1 f6",
    "before"
   ]
  ],
  "4...Nge7": [   [    "вместо Nge7",
    "Nf6 h4 d5 Bg2 d4 Nd5 Nxg4",
    "before"
   ]
  ],
  "5.h4": [   [    "вместо h4",
    "Bg2 Ng6 Nf3 d6 h3 Be7 Be3",
    "before"
   ]
  ],
  "5...d5": [   [    "вместо d5",
    "g6 Bg2 Nd4 f4 d6 Be3 Nec6 Nd5 Bxg4",
    "before"
   ]
  ],
  "11...Nf4": [   [    "вместо Nf4",
    "Qd7",
    "before"
   ]
  ],
  "16...Bd6": [   [    "вместо Bd6",
    "Bg4",
    "before"
   ]
  ],
  "17.Bxg7": [   [    "вместо Bxg7",
    "Bxd6 Qxd6",
    "before"
   ]
  ]
 },
 "b5": {
  "3...h4": [   [    "вместо h4",
    "Be7 h4 d5 Bg2 Bg4 Nd2 c6 Ngf3 Nd7 e4",
    "before"
   ]
  ],
  "4.Bh3": [   [    "вместо Bh3",
    "f4 exf4 Bxf4 d5 Bg2 c6 e4 Be6 Nc3 d4",
    "before"
   ]
  ]
 },
 "c5": {
  "3...d6": [   [    "вместо d6",
    "d5 Bg2 dxc4 Bxc6+ bxc6 Qa4",
    "before"
   ]
  ],
  "4...h6": [   [    "вместо h6",
    "g5 Be3 Nh6 f3 Nd4 Nc3 c6 Qd2 f6 h4",
    "before"
   ]
  ]
 },
 "d5": {
  "3.Nf3": [   [    "вместо Nf3",
    "e4 d5 Qe2 d4 h3 Bg5 Nd2 Be6 Ngf3 Bf4",
    "before"
   ]
  ],
  "4.h3": [   [    "вместо h3",
    "g5 h6",
    "before"
   ]
  ],
  "4...f5": [   [    "вместо f5",
    "h5 g5",
    "before"
   ]
  ],
  "10...Nc6": [   [    "вместо Nc6",
    "Bxg5 Nxg5 Qxg5 Ne4 Qh5 Kd2 Nc6",
    "before"
   ]
  ]
 },
 "e5": {
  "1...e5": [   [    "вместо e5",
    "e6 d4 d5 Nf3 Nf6 Rg1 h6 h4 Nc6 c3",
    "before"
   ]
  ],
  "3.h4": [   [    "вместо h4",
    "e3 d5 Bg2 Be6 h4 Nc6 Nd2 Nge7 c4 dxc4",
    "before"
   ],
   [    "вместо h4",
    "Nf3 Nc6 e4 Nf6 g5 Ng4 d4 exd4 h3 Nge5",
    "before"
   ],
   [    "вместо h4",
    "e3 d5 Bg2 Ne7 c4 O-O cxd5 Nxd5 a3 c6",
    "before"
   ]
  ],
  "4.g5": [   [    "вместо g5",
    "e3 f5 gxf5 Bxf5 Qh5+ g6 Qe2 Nc6 a3 Qd7",
    "before"
   ]
  ],
  "5...Ne7": [   [    "вместо Ne7",
    "dxc4 Qa4+ Bd7 Qxc4 Bb6 Bg2 Bc6 Nf3 Nd7 Bd2",
    "before"
   ]
  ]
 },
 "g5": {
  "3.Bg2": [   [    "вместо Bg2",
    "g5 Be7 h4 h6",
    "before"
   ]
  ],
  "3...c6": [   [    "вместо c6",
    "a5 e4 dxe4 Bxe4 Nf6 Bf3 Be7 Nc3 c6 h3",
    "before"
   ],
   [    "вместо c6",
    "Bc5 g5 Nc6 Nc3 Be6 e4 Nge7 h4 Qd7 a3",
    "before"
   ],
   [    "вместо c6",
    "Bxg4 c4 Bb4+ Nd2 c6 cxd5 Ne7 dxc6 Nbxc6 a3",
    "before"
   ]
  ],
  "4.e4": [   [    "вместо e4",
    "h3 Ne7 Nf3 Ng6 Nc3 h6 e3 Bd6 e4",
    "before"
   ]
  ],
  "4...Bc5": [   [    "вместо Bc5",
    "dxe4 Bxe4 Nf6 Bf3 h6 Nc3",
    "before"
   ]
  ],
  "5.Qe2": [   [    "вместо Qe2",
    "h4 dxe4 Bxe4 Nf6 Bf3 Qd4 Qe2 Bxg4",
    "before"
   ]
  ]
 },
 "a6": {
  "2...Nd5": [   [    "вместо Nd5",
    "Ne4 d3 Nd6 Bg2 g6 c4 c5 Nc3 Bg7 e4",
    "before"
   ],
   [    "вместо Nd5",
    "Nh5 d3 e5 e4 g6 Be2 Ng7 Nf3 d6 d4",
    "before"
   ]
  ]
 },
 "b6": {
  "2...h4": [   [    "вместо h4",
    "e5 d4 exd4 Qxd4 Nc6 Qe4+ Qe7 Bg2 d6 Nc3",
    "before"
   ]
  ],
  "3...d6": [   [    "вместо d6",
    "c5 d5 g6 e4 d6 h3 f5 f3 e5 dxe6",
    "before"
   ]
  ],
  "5...Nc6": [   [    "вместо Nc6",
    "Bg7 h3 Nc6 c3 e5 d5 Nce7 e4 f5 gxf6",
    "before"
   ]
  ]
 },
 "c6": {
  "2...e6": [   [    "вместо e6",
    "f6 d4 Bh6 Nf3",
    "before"
   ]
  ],
  "3.Nf3": [   [    "вместо Nf3",
    "hxg5 Qxg5 e4 d6 d3 Qe7 g5 d5 Bg2 d4",
    "before"
   ]
  ],
  "3...Be7": [   [    "вместо Be7",
    "gxh4 Rxh4",
    "before"
   ]
  ]
 },
 "d6": {
  "2...h6": [   [    "вместо h6",
    "Bg7 c4 d6 Nc3 Nf6 h3 O-O d4 c6 Be3",
    "before"
   ]
  ],
  "5...d5": [   [    "вместо d5",
    "Nf6 Ne5 d6 Nd3",
    "before"
   ]
  ],
  "7...Nf6": [   [    "вместо Nf6",
    "f5 gxf5 gxf5 Nc5 Nc6 c3 b6 Nh4 Qd6 Nd3",
    "before"
   ]
  ]
 },
 "e6": {
  "3...d5": [   [    "вместо d5",
    "Qb6 axb5 Qxb5 Nc3",
    "before"
   ],
   [    "вместо d5",
    "Qa5 b3",
    "before"
   ]
  ]
 },
 "g6": {
  "2.c4": [   [    "вместо c4",
    "Bg2 e6 d3 Nf6 g5 Ng4 d4 c5 h3",
    "before"
   ],
   [    "вместо c4",
    "Bg2 d5",
    "before"
   ]
  ],
  "2...d5": [   [    "вместо d5",
    "g5 d4 h6 e4 e6 d5 b6 Qd4 f6 d6",
    "before"
   ]
  ],
  "3.Qb3": [   [    "вместо Qb3",
    "cxd5 Qxd5",
    "before"
   ]
  ],
  "3...Qc7": [   [    "вместо Qc7",
    "dxc4 Qxc4",
    "before"
   ]
  ],
  "5.Nc3": [   [    "вместо Nc3",
    "Bg2 Qxc1+",
    "before"
   ]
  ]
 },
 "h6": {
  "2...e5": [   [    "вместо e5",
    "a6 h3 h5 g5 e5 d3 f6 gxf6 Nxf6 Nf3",
    "before"
   ],
   [    "вместо e5",
    "c6 h3 h6 c4 e5 Nc3 Be6 b3 Be7 Nf3",
    "before"
   ],
   [    "вместо e5",
    "Nc6 h3 g6 d4 Bg7 c3 e6 e4 Nge7 Ne2",
    "before"
   ]
  ],
  "3.d3": [   [    "вместо d3",
    "c4 c6 h3 f5 e3 g6 Nc3 Be6 Qb3",
    "before"
   ]
  ],
  "5...d4": [   [    "вместо d4",
    "g6",
    "before"
   ]
  ],
  "7...g5": [   [    "вместо g5",
    "g6",
    "before"
   ]
  ],
  "13...Bxf5": [   [    "вместо Bxf5",
    "Be6",
    "before"
   ]
  ],
  "14...h6": [   [    "вместо h6",
    "Bb4",
    "before"
   ]
  ]
 },
 "i6": {
  "2.d3": [   [    "вместо d3",
    "Bg2 h5 h3 hxg4 hxg4 Rxh1 Bxh1 Qh4 Bf3 Nf6",
    "before"
   ],
   [    "вместо d3",
    "d4 d5 Nf3 Nf6 Rg1 h6 h4 Nc6 c3 Be7",
    "before"
   ]
  ],
  "3.Bg2": [   [    "вместо Bg2",
    "Nc3 c5 e4 Nc6",
    "before"
   ]
  ]
 }
}
