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
  "4.cxd5": "<b>cxd5!</b> — <div class=\"alts\"><span class=\"cap\">вместо cxd5</span><div class=\"alt\"><b>4.Qb3</b>b3 Qc7 5.cxd5 (5…e6 6.h3! Bf5 7.e4 Bg6 8.dxe6! fxe6 9.Qxe6+ etc.) cxd5 6.Nc3 and now: (6…e6? 7.Qa4+ with 8. QxB next) (6…Nc6! 7.Nxd5 Qd7 8.Qa4 Rc8 9.d3 (9…e6 10.Qxg4 exd5 11.Qxd7+ Kxd7 12.Bh3+ with White winning a R for B)) e5 10.Bd2 Nd4 (11.Qxa7? Nc2+) 11.Qxd7+ Bxd7 12.Kd1 with equal chances-H. Grob.) d4? 7.Nb5 Qb6 8.Bxb7 (8…Qxb7? 9.Nd6+ exd6 10.Qxb7 Black Resigned; C. Bloodgood- J. Boothe, 1972) Be6 9.Qf3 Qxb5 10.Bxa8 Nf6 11.Qb7 with an easy win- H. Grob.</div></div>",
  "4...Nf6": "<div class=\"alts\"><span class=\"cap\">вместо Nf6</span><div class=\"alt\"><b>4…Qc7</b>5.Nc3 Nf6 (6.Qb3!? and if e6 , 7.h3!) 6.h3 Bd7 7.e4 e6 8.dxe6 Bxe6 9.d4 Nbd7 10.Nge2 g6 11.Be3 Bg7 12.O-O O-O 13.Rc1 (13…Qa5 14.Bd2 Qb6) Bc4 14.b3 Bxe2 15.Qxe2 Qa5 16.e5 Ne8 17.Ne4 (17…Qd8 with ...Nb6- Nd5 following) Nc7!? 18.Nd6! Rab8 19.Nxb7 <i>1-0 Grob,H-Chevalier,D/corr 1964 (19) with an easy win.</i></div><div class=\"alt\"><b>4…Qb6</b>5.Nc3 e5 6.Qc2 Nf6 7.a4 a5 8.d3 cxd5 9.Nxd5 Nxd5 10.Bxd5 Bc5 (11.Qc4? Qb4+ relieves some of the pressure on Black) 11.Be3 Bxe3 12.fxe3 (12…Qxe3? 13.Qc4 Qd4 14.Bxf7+ Kd8 15.Qb3 with advantage to White) Bd7 13.Nf3 <i>1-0 Bloodgood,C-Clark,J/corr Zugzwang 1975 (23) with some advantage to White.</i></div><div class=\"alt\"><b>4…cxd5</b>5.Qb3 come several lines of interest (5…Qc7 6.Nc3 Nf6 7.Nxd5 Nxd5 8.Bxd5 Nc6 9.Bxf7+ Kd8 (compare this with the position after 9... Kd8 in Bloodgood-Ebright below) 10.Nf3 Qd7 11.Ng5 Nd4 12.Qd3 Bxe2 13.Qxd4! <i>1-0 Bloodgood,C-Christy,W/ Norfolk Open 1957 (13) (if 13... Qxd4 14. Ne6+)</i>) (5…e6? 6.Qa4+ <i>1-0 Bloodgood,C-Bowlby,R/corr 1974 (6) Black resigned.</i>) Nf6 6.Nc3 e6 7.Qxb7 Nbd7 8.d4 (8…a5! 9.Bf4 Rc8 10.h3 Bf5 11.Qb3 Rc4 12.Nb5? a4! 13.Qxc4 dxc4 14.Nc7+ Ke7 15.d5 e5 16.O-O-O Qxc7 17.d6+ Qxd6 18.Rxd6 Kxd6 19.Bd2 Be7 20.Nf3 h6 21.Rd1 Ke6 22.Bc3 Ne4 23.Be1 a3 24.e3 Ndc5 25.bxa3 Nd3+ White resigned 0-1 Grob,H-Gubler,E./corr) Rb8 9.Qxa7 Bd6 10.Qa6 Rb6 11.Qd3 <i>1-0 Grob,H-Wegmueller,A/corr 1963 (11) with advantage to White.</i></div><div class=\"alt\"><b>4…Qa5</b>5.Qb3 Qb6 (6.dxc6! and the white queen cannot be taken because of (6…Nxc6 7.Qxb6 axb6 8.Na3 with advantage to White.) Qxb3 7.cxb7!) 6.Qg3 Nf6 7.Nc3 Bd7 8.e4 Na6 9.Nge2 Rd8 10.O-O cxd5 11.exd5 g6 12.d3 Nb4 13.Be3 Qa6 14.d4 Bf5 15.Nf4 h5 16.h4 Bh6 17.Rfd1 Nc2 18.Rac1 Nxe3 19.fxe3 g5! 20.hxg5 Rg8 21.e4 Rxg5 22.Qe3 Bh7 23.Rf1 Kf8 24.Kh1 Kg8 25.e5 Ng4 26.Qd2 Kh8 with equal chances.</div></div>",
  "5.Qb3": "<div class=\"alts\"><span class=\"cap\">вместо Qb3</span><div class=\"alt\"><b>5.Nc3</b>c3 is not as good as the text because it allows Bd7 A line of note continues 6.Qb3 Qc8 7.d4 e6 8.e4 exd5 9.exd5 Be7 10.Bf4! cxd5 11.Nxd5 Nxd5 12.Bxd5 with White standing much the better; analysis by H. Grob. Black has better moves in this line.</div></div>",
  "5...Qc7": "'See Bloodgood-Shepard, Variation \"B\", for 5... Qd7.' — <div class=\"alts\"><span class=\"cap\">вместо Qc7</span><div class=\"alt\"><b>5…Qb6</b>6.dxc6! (6…Qxb3? 7.cxb7 Qxb7 8.Bxb7 with material advantage; C. Bloodgood-J. Turenchalk, IPC EKO-1),) Nxc6 7.Qxb6 axb6 8.Nc3 (8…Nd4!? is Black's best chance) e5? 9.b3 Nd4 10.Kd1 (10…Nxb3 11.Rb1 Nxc1 12.Rxc1 Bc5 or 12... Bc8) Bb4? 11.Bxb7 Ra7 12.Nd5 Nxd5 13.Bxd5 O-O 14.Bb2 <i>1-0 Bloodgood,C-Hassan,B/corr APCT 1974 (14) with Black having nothing for the pawn.</i></div><div class=\"alt\"><b>5…Qc8</b>6.Nc3 e6 7.h3! Bh5 8.dxe6 fxe6 9.Na4 b6 10.d4 Nd5 11.e4 Nf6 12.Bf4 Bf7 13.Bg3 e5!? 14.d5 cxd5? 15.exd5 Bd6 16.Ne2 O-O 17.O-O Nbd7 18.Rac1 Qb7 19.Nd4 exd4 20.Bxd6 Rfe8 21.Rc7 Qa6 22.Qd1 Rad8 23.Qxd4 Nc5 24.Bxc5 bxc5 25.Nxc5 Qd6 26.Rxf7 Kxf7 27.Nb7 Qd7 28.Nxd8+ Rxd8 29.Rd1 <i>1-0 Bloodgood,C-Moore/Virginia 1972 (29) with an easy endgame win for White.</i></div></div>",
  "6...e6": "<div class=\"alts\"><span class=\"cap\">вместо e6</span><div class=\"alt\"><b>6…Nxd5</b>7.Nxd5 cxd5 8.Bxd5 Bc8 9.Bxf7+ Kd8 10.Nf3 Nc6 11.Bg8! Bd7? 12.Qf7 <i>1-0 Bloodgood,C-Ebright,D/corr APCT 1975 (15) with a material advantage.</i></div></div>",
  "7.h3": "<b>h3!</b> — <div class=\"alts\"><span class=\"cap\">вместо h3</span><div class=\"alt\"><b>7.dxc6</b>c6 Nxc6 8.d3 a6 9.Be3 Be7 10.Bb6 Qd7 11.Nh3 e5 12.Ng5 O-O (13.Nf3 with about equal chances) 13.Nce4? Nxe4 14.Nxe4 Be6 15.Qc2 Bd5! <i>0-1 Bloodgood,C-Buntin,L/IPC IST-2 1975 (25) with advantage to Black.</i></div></div>",
  "7...Bh5": "<div class=\"alts\"><span class=\"cap\">вместо Bh5</span><div class=\"alt\"><b>7…Bf5</b>8.e4 Bg6 9.dxe6! fxe6 10.Qxe6+ favors White also.</div></div>",
  "9.Qxe6+": "White has much the better of this."})

add("b_3_nf6_4_cxd5_nxd5", C1, "Вариант B · 3…Nf6!? 4.cxd5 Nxd5", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 Bxg4 c4 Nf6 cxd5 Nxd5 Qb3 c6 Qxb7 Nd7 Bxd5 Rb8 Bxf7+ Kxf7 Qxa7 g6 b3 Bg7 Nc3 Rf8 Bb2 Kg8 Qa4 Ne5 Nd1 Ra8 Qe4 Bf5 Qg2 Qc7 Nc3 Rfb8 Rc1 Nc4 Ba1 Bxc3 Bxc3 Nd6 h4 h5 Be5 Rb6 Nh3 Rxa2 Nf4 Kf7 Rg1 Ke8 Nd5 Qb7 Nxb6 Qxb6 Qxc6+ Qxc6 Rxc6 Kd7 Rc1",
 {
  "2...Bxg4": "<b>Bxg4!?</b>",
  "3...Nf6": "<b>Nf6!?</b> — This seemingly logical line of defense leads to complications almost immediately. There is much to be explored here, but from what has been played, White obtains an advantage in this variation.",
  "4.cxd5": "<div class=\"alts\"><span class=\"cap\">вместо cxd5</span><div class=\"alt\"><b>4.Qb3</b>b3 e6 5.Qxb7 Nbd7 6.cxd5 (6…Rb8 transposes into Variation \"C\") exd5 (7.Nc3? Nc5! and the white Queen is trapped, e.g. if (8.Qc6+ Bd7) (8.Qb5+ c6 9.Qxc6+ Bd7 - H. Grob) 8.Qb4 Nd3+) 7.Qb3 Black now gets good counterplay with Nc5 8.Qc2 Qd7 9.Nc3 Bf5 etc.</div></div>",
  "4...Nxd5": "<div class=\"alts\"><span class=\"cap\">вместо Nxd5</span><div class=\"alt\"><b>4…Qd7?</b>5.Qb3 c6 6.Nc3 (6…Nxd5 7.Nxd5 cxd5 8.Bxd5 with threats against both Black's b7 pawn and f7 pawn) e6 7.h3! (7…Bf5 8.e4 Bg6 9.dxe6! fxe6 10.d4 White has a distinct advantage) Bh5 8.dxe6! (8…Qxe6? 9.Qxb7 wins) fxe6 9.Nf3 Nd5 10.Ne5 Qc7 11.d4 (11…Nxc3 12.Qxe6+ is better for White) Nd7 12.e4 (12…Nxc3 13.Qxe6+!) Nxe5 (13.Bf4? Nd3+!) (13.exd5!? Nd3+ with Black getting some counterplay) 13.dxe5 (13…Nxc3 14.Qxe6+ Be7 15.bxc3 Bf7 16.Qf5 O-O 17.e6 Bg6 18.Qg4 Qa5 19.Bd2 Rad8 is unclear.) Nb4 14.Qxe6+ Be7 15.O-O (15…Bf7!?) Nc2 16.Rb1 Nd4 17.Qc4 (17…Qxe5!? 18.f4 Qc5 19.Qxc5 Bxc5 20.Kh1 O-O-O is better for Black) Nf3+ 18.Bxf3 Bxf3 19.Bf4 O-O-O 20.Rbc1 (20…g5! 21.Bg3 h5) a6? 21.Nd5! (21…Qd7? 22.Nb6+) Rxd5 22.exd5 <i>1-0 Bloodgood,C-Shepard/corr 1975 (22) with advantage to White.</i></div></div>",
  "5...c6": "<div class=\"alts\"><span class=\"cap\">вместо c6</span><div class=\"alt\"><b>5…e6?</b>6.Qa4+ wins.</div></div>",
  "6...Nd7": "<div class=\"alts\"><span class=\"cap\">вместо Nd7</span><div class=\"alt\"><b>6…Nb6?</b>7.Bxc6+ (7…N8d7 is no better) Bd7 8.Bxd7+ (8…N8xd7!? avoiding the queen trade would have been better) Qxd7 9.Qxd7+ N8xd7 10.b3 e6 11.Bb2 delaying Blacks KB development Nf6 12.Nf3 Nbd5 13.Rg1 Rc8 14.Nc3 (14…Nf4 followed by ...Ng6 and ...Be6) Nb4? 15.Rc1 a6 16.a3 Nbd5 17.Nxd5 Rxc1+ 18.Bxc1 Nxd5 19.Bb2 f6 20.Rg4 Kf7 21.Ra4 <i>1/2-1/2 Bloodgood,C-Carpenter,H/corr. 1975/ Megacorr (33) with an easy engame win.</i></div><div class=\"alt\"><b>6…Qc7?</b>7.Qxa8 Nb6 8.Bxc6+ Bd7 (9.Bxd7+? Kxd7! and the White queen is lost or White is mated) 9.Qb7 Qxc6 (10.Qxb8+ Bc8 with Black threatening Qxc1 mate and Qxh1) with a material advantage-H. Grob.) 10.Qxc6</div></div>",
  "7.Bxd5": "<div class=\"alts\"><span class=\"cap\">вместо Bxd5</span><div class=\"alt\"><b>7.Qxc6?</b>6? Rc8 with mate threatened if the White queen moves.</div></div>",
  "7...Rb8": "<div class=\"alts\"><span class=\"cap\">вместо Rb8</span><div class=\"alt\"><b>7…cxd5</b>8.Qxd5 Nb6 9.Qg2 Rc8 10.Nc3 Bd7 11.b3 Bc6 12.Nf3 e6 13.Bb2 Bxf3 14.Qxf3 Be7 15.Ne4 O-O? Black can't afford this! 15...f6 was best, 16.Rg1 f6 17.Qg4 Rf7 18.Qxe6 Qd7 19.Qxd7 Nxd7 20.Rc1 Rxc1+ 21.Bxc1 Ne5 22.Bb2 Bb4 23.a3 Ba5 24.b4 Bb6 25.h4 Nc4 26.Bxf6 Nxa3 27.h5 Nb5 28.h6 g6 29.Bg7 Rc7 30.Kd1 a5 31.Nf6+ Kf7 32.Nd5 Rb7 33.Nxb6 Rxb6 34.bxa5 Ra6 35.Rg5 <i>1-0 Bloodgood,C-Halley,R/ Washington D.C. 1958 (35) Black resigned.</i></div></div>",
  "8.Bxf7+": "<div class=\"alts\"><span class=\"cap\">вместо Bxf7+</span><div class=\"alt\"><b>8.Qxc6?</b>6? Rc8 etc.</div></div>",
  "9...g6": "<div class=\"alts\"><span class=\"cap\">вместо g6</span><div class=\"alt\"><b>9…e5</b>10.f3 Bc5 11.Qa4 Bd4 12.Nc3 Qf6 13.Ne4 Qf4? 14.d3 is a queen trap of interest because it occurs in a line where Black appears to have good counterplay.</div></div>",
  "11...Rf8": "<div class=\"alts\"><span class=\"cap\">вместо Rf8</span><div class=\"alt\"><b>11…Nb6</b>12.Bb2 Ra8? 13.Qb7 Bd7 14.a4 Nd5 15.Nf3 Rf8 16.e4 Nxc3 17.Bxc3 Bxc3 18.dxc3 Kg8 19.Ne5 Be8 20.Nxc6 Qd7 21.Nxe7+ <i>1-0 Bloodgood,C-Acevedo,A/Norfolk 1958 (21)</i></div></div>",
  "12...Kg8": "<div class=\"alts\"><span class=\"cap\">вместо Kg8</span><div class=\"alt\"><b>12…Bh5</b></div></div>",
  "14...Ra8": "The black defenses are tied to a very precariously situated Knight, but White has to be careful because Black commands most of the board. C. Bloodgood- K. Stevens, 1960, continued",
  "30.Rc1": "Black Resigned."})

add("c_3_e6_4_qb3_qc8", C1, "Вариант C · 3…e6 4.Qb3 Qc8", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 Bxg4 c4 e6 Qb3 Qc8 cxd5 c6 dxc6 Nxc6 Qa4 Nf6 Bxc6+ bxc6 d3 Bh5 Bd2 Bc5 Nc3 O-O Ne4 Bb6 Rc1 Nxe4 dxe4 c5 Be3 f5 b4 Be8 Qb3 f4 Bxc5",
 {
  "2...Bxg4": "<b>Bxg4!?</b>",
  "3...e6": "This variation differs from 3...c6 in that Black sacrifices some co-ordination of his pieces for more choice in which pawn he will return.",
  "4.Qb3": "<div class=\"alts\"><span class=\"cap\">вместо Qb3</span><div class=\"alt\"><b>4.cxd5</b>d5 This frequently transposes to Variation \"A\". Several independent lines also are possible: exd5 5.Qb3 (5…c6 6.Qxb7 Nd7 (7.Qxc6? Rc8 and Black threatens mate if the queen moves) 7.Nc3 Qc8 8.Qxc8+ Rxc8 9.d4 Bb4 10.Bd2 Ngf6 11.a3 Bxc3 12.Bxc3 O-O 13.Nf3 c5 14.dxc5 Nxc5 15.Ne5 Be6 16.Bb4 Nb3 17.Rd1 (17…Rfe8 is better) Rfd8 18.Rg1 (18…Nd7 19.Nxd7 Rxd7 20.e3 Rdc7 21.Bc3 with White maintaining the pressure on Black's d-pawn,) Rc2? 19.Be7 Rdc8 20.Bxf6 gxf6 21.Be4+ Kh8 22.Bxc2 Rxc2 23.Nd3 Nd4 24.Nf4 Nb3 25.Nh5 Bf5 26.Nxf6 Bg6 27.f4 Kg7 28.Nxd5 Kf8 29.Ne3 Rxb2 30.f5 Bh5 31.Rg2 f6 32.Rd7 Rb1+ 33.Nd1 Nc1 34.Rxh7 Bf7 35.Rgg7 Bc4 36.Rxa7 Kg8 37.Rhc7 <i>1-0 Bloodgood,C-Casteen,D/ Norfolk 1960 (37)</i>) Qc8 6.Bxd5 Nc6 7.Bxf7+ Ke7 8.Bxg8 Rxg8 9.Qxg8 Nd4 10.Qc4 <i>1-0 Bloodgood,C-Waymire,W/Norfolk 1960 (10) Black resigned.</i></div></div>",
  "4...Qc8": "<div class=\"alts\"><span class=\"cap\">вместо Qc8</span><div class=\"alt\"><b>4…Nf6</b>5.Qxb7 Nbd7 6.cxd5 Rb8 7.Qc6 Rb6 8.Qa4 (8…Bc5! 9.a3 exd5 10.d4 Be7 11.Nc3 c6 with equal chances; Grob) exd5 9.Bxd5 Nxd5 10.Qxg4 N7f6 11.Qg3 Rc6 12.Nc3 Nxc3 13.dxc3 Qd5 14.Nf3 Rd6 15.Bg5 Ne4 16.Qh4 f6 17.Be3 g5 18.Qh5+ Kd8 19.O-O g4 20.Qxd5 Rxd5 21.Rfd1 Rxd1+ 22.Rxd1+ Kc8 23.Nd4 Bc5 24.Kg2 Rg8 25.f3 gxf3+ 26.Kxf3 Ng5+ 27.Bxg5 fxg5 28.h3 h5 29.e4 Rf8+ 30.Nf5 a5 31.Rd5 Bb6 32.Kg3 Rf7 33.Nd4 Rg7 34.Ne6 Rg8 35.Nxg5 c6 36.Rf5 Bd8 37.Kh4 Rh8 38.Kg3 Rg8 39.h4 Kd7 40.Kf4 Bc7+ 41.e5 Re8 42.Ne4 Ke6 43.Rf6+ Kd5 44.Nd6 Bxd6 45.Rxd6+ Kc5 46.Rd2 <i>1-0 Bloodgood,C-Branson,S/Norfolk 1959 (46)</i></div><div class=\"alt\"><b>4…Nd7</b>5.cxd5 Nc5 6.Qe3 Be7 7.Nc3 Nf6 8.d4 Ncd7 9.h3 Bf5 10.dxe6 Bxe6 11.Bxb7 favors White; Grob</div></div>",
  "7.Qa4": "<div class=\"alts\"><span class=\"cap\">вместо Qa4</span><div class=\"alt\"><b>7.Nc3</b>c3 Nf6 8.d3 Bb4 9.Bd2 e5 10.Rc1 <i>1-0 Bloodgood,C-Rhodes,C/corr APCT 1975 (10) with advantage to White.</i></div></div>",
  "8...bxc6": "<div class=\"alts\"><span class=\"cap\">вместо bxc6</span><div class=\"alt\"><b>8…Qxc6</b>9.Qxc6+ bxc6 10.b3 Bc5 11.Bb2 O-O 12.Nc3 Nd5 13.O-O-O a5 14.Na4 Ba7 15.f3 Bh5 16.h4 favors White.</div></div>",
  "10...Bc5": "<div class=\"alts\"><span class=\"cap\">вместо Bc5</span><div class=\"alt\"><b>10…Be7</b>11.Nc3 Nd5 12.O-O-O O-O 13.Ne4 c5 14.Kb1 Bg6 15.Rc1 Bxe4 16.dxe4 Nb6 17.Qc2 Rb8 with counter play.</div></div>",
  "13...Nxe4": "<div class=\"alts\"><span class=\"cap\">вместо Nxe4</span><div class=\"alt\"><b>13…Ng4?</b>14.Rxc6 Qd7 15.Rc4 Qxa4 16.Rxa4 f5 17.f3 fxe4 18.fxg4 Bxg4 19.Rxe4 Bf2+ 20.Kd1 Bf5 21.Rf4 Bg6 22.Nf3 with White a pawn up.</div></div>",
  "15...f5": "<b>f5!?</b> — <div class=\"alts\"><span class=\"cap\">вместо f5</span><div class=\"alt\"><b>15…a5</b>16.Qb5 Qc7 17.Bxc5 Bxc5 18.Rxc5 Qe7 19.Rxh5 <i>1-0 Bloodgood,C-Cacalano,A/Norfolk 1959 (19) Black resigned.</i></div></div>",
  "18.Bxc5": "White has a clear advantage."})

add("d_3_e5_4_cxd5", C1, "Вариант D · 3…e5 4.cxd5", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 Bxg4 c4 e5 cxd5 c6 Qb3 Qc7 Nc3 Nf6 d3 Bc5 Be3 Bxe3 fxe3 O-O e4 Na6 Nf3 Nc5 Qc2 Rfd8 b4",
 {
  "2...Bxg4": "<b>Bxg4!?</b> — <div class=\"alts\"><span class=\"cap\">вместо Bxg4</span><div class=\"alt\"><b>2…e5</b>3.c4 c6 4.cxd5 cxd5 5.Qb3 Ne7 6.Nc3 e4 7.d3 exd3 8.Bf4 Na6 9.O-O-O Nc5 10.Qb5+ Nc6 11.Nxd5 Qa5 12.Nc7+ <i>1-0 Bloodgood,C-Sanderson,T/corr 1973/Megacorr (12)</i></div></div>",
  "3...e5": "Black's purpose in playing 3...e5 is to avoid the compications arising after any direct attempt to hold the gambit pawn; since the pawn cannot be held anyway, this would seem best, but has not proven successful in practice.",
  "4.cxd5": "<div class=\"alts\"><span class=\"cap\">вместо cxd5</span><div class=\"alt\"><b>4.Qb3</b>b3 (4…Bc8 5.cxd5 Nf6 6.Nc3 c6 7.d3 (7…Qc7 is better,) Na6? 8.dxc6 Nc5 9.Qb5 a6 10.cxb7+ axb5 11.bxa8=Q <i>1-0 Stroemer, D-Patterson,P/corr 1972 (11) with a quick win for White.</i>) Qc8 5.Nc3 c6 6.cxd5 (6…cxd5? 7.Bxd5 and Black loses quickly,) Nf6 7.d3 (7…Nxd5? 8.Nxd5 Be6 9.e4! cxd5 10.exd5 gives White a pawn while doing nothing to ease Black's position) Bc5 8.Bg5 (8…Bxf2+ 9.Kxf2 Qf5+ 10.Nf3 Bxf3 11.Bxf3 Qxg5 12.Qxb7 wins for White-Grob,) Qf5 9.Be3 Bxe3 10.fxe3 (10…Qc8 is suggested by Grob,) Qd7 11.Nf3 Bxf3 12.Bxf3 O-O 13.Rg1 Na6? as cramped as Black's position was, this was no answer...an idea would be 13...a5 followed by Ra6, 14.dxc6! bxc6 15.Qc4 Nb8 16.O-O-O Re8 17.Rg3 Qe6 18.Qa4 Rc8 19.Ne4 Nbd7 20.Rdg1 Ne8 21.Ng5 Qd6 22.Qh4 h6 23.Ne4 (23…Qe6 was Black's only chance) Qf8? 24.Qxh6 g6 25.Rxg6+! fxg6 26.Rxg6+ Ng7 27.Ng5 Qc5+ 28.Kb1 <i>1-0 Grob,H-Spichtig/corr 1964 (28) Black resigned.</i></div></div>",
  "4...c6": "<div class=\"alts\"><span class=\"cap\">вместо c6</span><div class=\"alt\"><b>4…Nf6</b>5.Qb3 Qc8 6.Nc3 (6…c6 transposes to Grob-Spichtig,) Na6? 7.d6! c6 8.Nb5 cxb5 9.Qxb5+ Bd7 10.Qxe5+ Kd8 11.d4! with a strong attack. (11…Bc6? 12.d5 Bd7 13.Bg5 Nb4 14.Rc1 Nc2+ 15.Kd1 Ba4 16.Bxf6+ gxf6 17.Qxf6+ Ke8 18.b3 <i>1-0 Bloodgood,C-Stroemer,D/Virginia 1972 (18) Black resigned.</i>) Qc4 12.Bg5 Qb4+ 13.Kf1 Bxd6 14.Bxf6+ gxf6 15.Qxf6+ Kc7 16.Rc1+ Kb6 17.Rc3 Ka5 18.Rb3 Qc4 19.Qg5+ Bb5 20.Bd5 Qc2 21.Rxb5+ Kxb5 22.Bb3+ <i>1-0 Bloodgood,C-McKay,J/Norfolk USO Invitational 1961 (22) Black resigned.</i></div></div>",
  "5...Qc7": "<div class=\"alts\"><span class=\"cap\">вместо Qc7</span><div class=\"alt\"><b>5…Qb6!?</b>6.dxc6! appears to favor White (6…Qxb3 7.cxb7 Qxb7 8.Bxb7 <i>1-0 Bloodgood,C-Davis (8) Black resigned.</i>) Nxc6 7.Qxb6 axb6 8.Nc3 Nd4 9.Kd1 (9…Nf6 is better,) Bb4? 10.Nd5 Bd6 11.Nxb6 (11…Ra7 12.Nc4 Bc7 13.a4 Nf6 14.d3 with White having better endgame prospects,) Rb8 12.b3 Nf6 13.Bb2 O-O 14.Nc4 Bc7 15.f4 Nc6 16.fxe5 Nd7 17.d4 Rfd8 18.d5 Ncxe5 19.d6 Nxc4 20.dxc7 Nxb2+ 21.Ke1 <i>1-0 Bloodgood,C-Porter,R/ Norfolk 1959 (21) Black resigned.</i></div></div>",
  "7...Bc5": "<div class=\"alts\"><span class=\"cap\">вместо Bc5</span><div class=\"alt\"><b>7…Na6?</b>8.dxc6 Nc5 9.Qb5 a6 10.cxb7+ axb5 11.bxa8=Q+ with an easy win for White.</div><div class=\"alt\"><b>7…Nxd5</b>8.Nxd5 cxd5 9.Bxd5 Bc8 10.Bd2 Nc6 11.Rc1 Bd6 12.Ba5 Qd7 13.Bxc6 bxc6 14.Nf3 Rb8 15.Qc3 with Black losing a pawn in a pressure position.</div></div>",
  "9...O-O": "<div class=\"alts\"><span class=\"cap\">вместо O-O</span><div class=\"alt\"><b>9…Nxd5</b>10.Nxd5 cxd5 11.Bxd5 Bc8 12.Nf3 which definitely favors White.</div></div>",
  "10.e4": "White has two sets of connected doubled pawns, which are serious threats in the center, e.g. two connected passed would not be easy for Black to cope with. — <div class=\"alts\"><span class=\"cap\">вместо e4</span><div class=\"alt\"><b>10.dxc6</b>xc6 Nxc6 11.Nb5 Qb6 12.Nd6 Qxb3 13.axb3 Bc8 <i>1/2-1/2 Bloodgood, C-Sternberg,P/Norfolk 1958 (13) with Black equalizing.</i></div></div>",
  "11...Nc5": "<div class=\"alts\"><span class=\"cap\">вместо Nc5</span><div class=\"alt\"><b>11…Bxf3</b>12.Bxf3! with the e-pawn held to support White's center pawns.</div></div>",
  "13.b4": "White has the better chances!"})

add("a1_3_c4_dxc4_4_b3", C2, "Вариант A1 · 3.c4!? dxc4 4.b3!?", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 c6 c4 dxc4 b3 cxb3 Qxb3 e5 Nc3 Qb6 Qc2 Bxg4 Rb1 Qc7 Nd5 Qc8 Ne3 Be6",
 {
  "1.g4": "This solid defensive line is an attempt by Black to move the game into positional situations rather than meet the tactical possiblilities resulting from 2...Bxg4!? White has several playable alternatives now: Variation \"A1\" covers the \"Double Gambit\" 3. c4; Variation \"B1\" covers the \"Short Spike' 3. h3; and Variation \"C1\" covers the \"Spike\" 3. g5.",
  "3.c4": "<b>c4!?</b>",
  "3...dxc4": "<div class=\"alts\"><span class=\"cap\">вместо dxc4</span><div class=\"alt\"><b>3…Bxg4</b>transposes to Part 1.</div></div>",
  "4.b3": "<b>b3!?</b> — This is a risky gambit for White to play, but it is far from simple for Black to refute. — <div class=\"alts\"><span class=\"cap\">вместо b3</span><div class=\"alt\"><b>4.Na3</b>a3 Bxg4 5.Nxc4 Nd7 6.d4 (6…e6 7.Qb3 Qc7 8.e4 Ngf6 9.f3 Bh5 10.Ne2 with an unclear position; Sontheim) e5 (7.Nxe5 Nxe5 8.dxe5 Qa5+ 9.Bd2 Qxe5 10.Bf3! ; H. Grob) 7.dxe5 Bb4+!? (8.Bd2! is sharper, e.g. Qe7 9.f4 O-O-O with equal chances; H. Grob) 8.Kf1? Nxe5 9.Bd2 Nxc4 10.Bxb4 Qxd1+ 11.Rxd1 Bd7 12.b3 Nb6 13.Bc3 f6 14.e4 O-O-O <i>0-1 Grob,H-Wettstein,M/corr 1966 (14) With Black standing better.</i></div><div class=\"alt\"><b>4.h3</b>h3 h5 5.g5 e5 6.h4 Be6 7.Qc2 Nd7 (8.Bh3) 8.g6? f5! 9.e4 Qf6 <i>0-1 Grob,H-Stuber,F/corr 1965 (9) with Black having much the better of this.</i></div></div>",
  "4...cxb3": "<div class=\"alts\"><span class=\"cap\">вместо cxb3</span><div class=\"alt\"><b>4…Bxg4</b>(5.Bb2 cxb3 6.Qxb3 Qb6!) (5.Na3 cxb3 6.Qxb3 Qb6 7.Qg3 Bf5 8.Nf3! Nd7 9.O-O Ngf6 10.d3 Rc8 11.Rb1 where Black has 2 pawns, but a bad defensive position; and now:) 5.bxc4 (5…Qd4 (6.Qb3? Qxa1 7.Qxb7 Bd7 8.Nf3 Qxa2 9.Nc3 Qa1 10.O-O! with White regaining the rook,) 6.Nc3 Qxc4 7.Ba3 Nf6 (8.Rb1 is worth a try) 8.Rc1 Qa6 9.Qb3 Nbd7 10.d4 Be6 11.Qb2 g6 12.e4 Bg7 13.Nf3 Qb6 14.Qd2 Qd8 15.d5 Nxe4 16.Nxe4 Bxd5 17.Nc3 Bc4 <i>1/2-1/2 Grob,H-Kast/corr 1964 (54) and despite the draw result, Black stands decidedly better.</i>) e6 6.Qb3 Qc7 7.h3 Bf5 8.e4 Bg6 9.d4 Nd7 (10.Nc3? e5 11.d5 Nc5 <i>0-1 Grob,H-Gubler/corr 1964 (59) etc.</i>) 10.f4! Be7 11.h4 Ngf6 12.Nc3 Nh5 13.Nce2 f6 (14.e5!? fxe5 15.fxe5 b5 breaks the white pawn center to White's disadvantage) 14.Bd2 e5 15.f5 Bf7 16.d5 (16…g6 17.fxg6 hxg6 18.Nf3 Nc5 19.Qc2 Rd8 is unclear; H. Grob E. Gubler, Correspondence) Nc5 17.Qc2 g6 18.fxg6 hxg6 (19.Rc1! is better) 19.a4 Rd8 <i>1/2-1/2 Grob,H-Gulber/corr 1964 (71) with equal chances.</i></div><div class=\"alt\"><b>4…Qd4</b>is not as good for Black. 5.Nc3 (5…Qxg4? 6.Bh3 Qg6 7.Bxc8 Qg2 8.Bxb7 Qxh1 9.Kf1!) Bxg4 6.Rb1 (6…cxb3 7.Qxb3 b6 8.Nb5 Qd7 9.d3 with Bf5 next) Nf6 7.bxc4 Qd7 8.Qb3 b6 9.c5!</div></div>",
  "5...e5": "<div class=\"alts\"><span class=\"cap\">вместо e5</span><div class=\"alt\"><b>5…Qd4</b>6.Nc3 (6…Qxg4? 7.Bh3! as in previous note) Qb6! 7.Qa4 Na6 8.Rb1 Qc7 9.d4 with some attack for the pawn.</div></div>",
  "6.Nc3": "<div class=\"alts\"><span class=\"cap\">вместо Nc3</span><div class=\"alt\"><b>6.Bb2</b>b2 and now: Bd6 7.Nf3 Nd7 8.d4 exd4 9.Bxd4 Ngf6 10.h3 Qe7 11.O-O Nc5 12.Qc2 Ne6 13.e3 Nd5 14.Nc3 Nxd4 15.Nxd4 Nxc3 16.Qxc3 O-O 17.Qb3 h5 18.gxh5 Qe5 19.f4 <i>0-1 Grob,H-Freytag,D/corr 1966 (19)</i> Qxh5 20.Rf3 Be7 21.f5!</div></div>",
  "6...Qb6": "<div class=\"alts\"><span class=\"cap\">вместо Qb6</span><div class=\"alt\"><b>6…h5</b>7.Nf3 Bd6 8.Ne4 hxg4 9.Nfg5 Nh6 10.Nxd6+ Qxd6 11.Ne4 (11…Qd5? 12.Nf6+) Qc7 12.Ba3 Nf5 13.Qd3 Rh6 14.h3 g3 15.fxg3 b6 16.O-O Nd4 (17.Rxf7! with Rf1 following and a sharp attack) 17.Nd6+? Rxd6 18.Qh7 Be6! <i>0-1 Grob,H-Levi/corr 1964 (33) with Black winning in 33.</i></div><div class=\"alt\"><b>6…Nf6</b>7.g5 Nfd7 8.Nf3 Nc5 9.Qc2 Bd6 (10.h4 Qe7 11.Bb2 Nba6 12.Ne4 Nxe4 13.Qxe4 Be6 14.Qb1 f6 15.d4 Bd5 16.gxf6 gxf6 17.dxe5 Bxe5 18.Bxe5 Bxf3 19.Bxf3 Qxe5 20.Bh5+ Qxh5 21.Qxb7 Qa5+ 22.Kf1 Nc7 <i>0-1 Richter,K-Becker,A/Bad Oeynhausen 1938/HCL (52) and Black won</i>) 10.Ne4 Nxe4 11.Qxe4 Qe7 12.Bb2 (12…Nd7 13.d4 with attack) Be6 13.Qe3 f6 14.d4 Bd5 15.gxf6 gxf6 16.dxe5 Bxf3 17.Bxf3 Bxe5 18.Bh5+ Kd8 19.O-O-O+ Kc7 20.Ba3 Qe6 21.Bd6+ Kc8 22.Bxe5 fxe5 23.Rhg1 Qe7 24.f4 e4 25.Qc3 Qf8 26.Rg7 <i>1-0 Grob,H-Denecke,T/corr 1964 (26) Black resigned.</i></div><div class=\"alt\"><b>6…f6</b>7.g5 Nd7 threatening 8... Nc5 followed by 9... Be6 8.gxf6 Ngxf6 9.Nf3 (9…Nc5 10.Qc2) Bd6 10.Ng5 Qe7 11.d4 h6 (12.Ne6? Nb6) 12.Nf3 e4 (13.Nh4? Nf8!) 13.Nd2 Nb6 14.Nc4 Bf5 and White is down a pawn with problems.</div></div>",
  "8...Qc7": "<div class=\"alts\"><span class=\"cap\">вместо Qc7</span><div class=\"alt\"><b>8…Qa6?</b>9.Qe4 Be6 10.Qxe5</div></div>",
  "9.Nd5": "<b>Nd5!</b>",
  "10...Be6": "White has little for the two pawns."})

add("b1", C2, "Вариант B1", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 c6 h3 e5 d3 Bc5 Nf3 Qe7 d4 exd4 Nxd4",
 {
  "3.h3": "The \"Short Spike\" is a fluid system in which White has several interesting means of disrupting the black defenses. The obvious threat of g5 discourages development of the black Knight at f6, and any attempt to attack this pawn structure to neutralize the threat has the effect of simultaneously weakening the black defenses. Should Black not play aggressively, the are still gambit possibilities for White which render the long diagonal a melting pot of double-edged tactics.",
  "3...e5": "<div class=\"alts\"><span class=\"cap\">вместо e5</span><div class=\"alt\"><b>3…h5</b>(4.e4 dxe4 5.Nc3 hxg4 6.hxg4 Rxh1 7.Bxh1 Qc7 8.Bxe4 Qh2 9.Kf1 Nf6 10.f3 e5 11.Qe2 Qg3 12.Qg2 <i>1/2-1/2 Plattner-Grob,H/corr 1964 (12) With a drawish position;</i>) 4.g5 e5 5.h4 f5 6.d3 g6 7.b3 Rh7 8.Bb2 Qc7 9.Nd2 Be6 10.e3 Nd7 11.Ne2 Rf7 12.f4 Bd6 13.O-O Qb6 14.d4 e4 15.Rb1 c5 16.c4 Qc6 17.Rc1 Qb6 18.cxd5 Bxd5 19.Nc3 (19…Qc6 with counterchances; H. Grob) Bc6? 20.Nc4 Qc7 21.d5 <i>1-0 Grob,H-Nussle/corr 1966 (21) winning a piece.</i></div><div class=\"alt\"><b>3…g5</b>(4.d4!? h6 5.e3 Bg7 6.Nd2 Nd7 (7.e4 dxe4 8.Nxe4 Ndf6 in this line.) 7.Ne2 e5 8.c3 f5 9.Ng3 Ne7 10.gxf5 O-O! <i>1/2-1/2 Grob,H-Ottomann/corr 1966 (10) and Black has the advantage;</i>) 4.Nf3 (4…h6 5.d4 Nd7 6.Nc3 Bg7 7.e4 dxe4 8.Nxe4 Ngf6 9.Ng3 O-O 10.c3 Nb6 11.Qc2 Nbd5 12.Bd2 <i>1/2-1/2 Giertz,N-Burk,D/corr 1977 (12) favors White;</i>) h5! (5.Nxg5!? e5! 6.d3 f6 7.Nf3 hxg4 8.hxg4 Rxh1+ 9.Bxh1 Bxg4 Which is better for Black; H. Grob) 5.gxh5 Rxh5 6.d3 Bg7 (7.Nxg5? Rxg5 8.Bxg5 Bxb2!) 7.Nbd2 f5 8.d4 e5 9.e4 exd4 10.Nxd4 g4 11.Nxf5 Bxf5 12.exf5 Qe7+ 13.Kf1 Rxf5 14.hxg4 Rf7 15.Nf3 Nd7 16.Bg5 Ngf6 17.Nd4 O-O-O 18.Qd3 Re8 19.Rh3 Qb4 20.Bd2 Qxb2 21.Bc3 Qa3 22.Re3 Ref8 23.Rae1 Nc5 24.Qg6 Nfe4 25.Bxe4 Nxe4 26.Qe6+ Kb8 27.Nxc6+ Ka8 28.Qxd5 Rf4 29.Na5 Rb8 30.Bxg7 Ng3+ 31.Kg2 Qb4 32.Rd1 <i>1-0 Grob,H-Marti,H/corr 1966 (32) Black resigned.</i></div><div class=\"alt\"><b>3…e6</b>(4.e4 Nf6 5.e5 Nfd7 6.Nf3 c5 7.c3 Nc6 8.d4 f6 9.exf6 Nxf6 with counterplay; H. Grob) 4.d3 (4…Nf6!? 5.e4 dxe4 6.g5! with threats; H. Grob) Bd6 (5.Nd2? h5!) 5.Nf3 (5…Ne7 6.e4 is suggested by Grob,) Nd7 6.Nbd2 h5 7.g5 f6 8.h4 e5 9.e4 Qc7 10.exd5 cxd5 11.c3 Nc5 12.Qc2 Bg4 13.d4 e4 14.dxc5 exf3 15.cxd6 fxg2 16.Rg1 Qxd6 17.Qg6+ Kd8 18.f3 Qh2 19.Kf2 Qxh4+ 20.Kxg2 (20…Bh3+) Qxg5?? 21.Qxg5 fxg5 22.fxg4 h4 23.Nf3 <i>1-0 Bloodgood,C-Fuller,H/VAPEN Chess Game 1973 (23) Black resigned.</i></div><div class=\"alt\"><b>3…f5</b>(4.e3!? e5 5.Nf3 Bd6 6.Nh2 Nh6 7.b3 <i>1/2-1/2 Bloodgood,C-Kenney,E/corr RPCC 1975 (7) with double-edged complications;</i>) 4.g5 e5 5.d3 h6 6.h4 f4 7.e4 hxg5 8.h5 g4 9.exd5 f3 10.Bxf3 gxf3 11.dxc6 Nxc6 12.Qxf3 Qf6 13.Qg3 Bd6 14.Bg5 Qf5 15.Nc3 Qg4 16.Qxg4 Bxg4 17.Nb5 Bb8 18.Kd2 Rxh5 19.Rxh5 Bxh5 20.Re1 a6 21.Nc3 Nf6 22.f4 Ng4 23.Nf3 Bc7 24.Nd5 Ba5+ 25.c3 Kf7 26.Nxe5+ Ngxe5 27.fxe5 Re8 28.Bf4 Ke6 29.Ne3 b5 30.Kc2 Bg6 31.Rg1 Ne7 32.Bg5 Bh7 33.Kd2 b4 34.d4 bxc3+ 35.bxc3 Nc6 36.Nc4 Bc7 37.Re1 Kd5 38.Ne3+ Ke6 39.d5+ Kxe5 40.dxc6 Kd6 41.Nf5+ Bxf5 42.Rxe8 <i>1-0 Bloodgood,C-Bostic,L/Virginia 1964 (42) Black resigned.</i></div><div class=\"alt\"><b>3…Nf6</b>(4.g5 is best) 4.c4!? dxc4 5.Na3 Be6 (6.Qc2! Qd4 7.Nf3 Qe4 8.Qa4! with initiative) 6.Qa4!? (6…Qd4 7.d3! or) (6…b5 7.Nxb5 cxb5 8.Qxb5+ Qd7 9.Qb7 Nc6 10.Bxc6 etc.) Bd5! 7.f3 b5!? 8.Qc2 e5 (9.Qf5 is worth trying.) 9.b3 cxb3 10.axb3 Bd6 11.Bb2 O-O 12.e4 Be6 (13.h4!) 13.f4 exf4 (14.e5!) 14.Nxb5 cxb5 15.g5 Nh5 16.e5 Nd7 17.exd6 Rc8 18.Qd1 Re8 19.Kf2 Qxg5 20.Nf3 Qg3+ 21.Kf1 Nc5 22.Ne5 Nd3 23.Bd4 f3 <i>0-1 Bloodgood,C-Driscoll,P/corr. 1975 (23) with a solid advantage to Black.</i></div></div>",
  "4.d3": "<div class=\"alts\"><span class=\"cap\">вместо d3</span><div class=\"alt\"><b>4.e4</b>e4 Ne7 5.d3 Ng6 6.exd5 Nh4 7.Kf1 Nxg2 8.Kxg2 cxd5 (9.Nf3 Nc6 10.Re1 is suggested by Bloodgood) 9.Qf3!? Be6 10.Nc3 Nc6 11.a3 (11…Nd4 12.Qd1) Be7 12.Nge2 O-O 13.Ng3 Nd4 14.Qd1 (14…f5) Bh4 15.Nce2 f5 16.Nxd4 exd4 17.f3 Qd6 18.f4 fxg4 19.hxg4 Bxg3 20.Kxg3 g5 21.Qf3 gxf4+ 22.Bxf4 Qd7 23.Rh6 Rae8 24.Rah1 Rf7 25.R1h5 Rg7 26.Rg5 Rf8 27.Rxg7+ Kxg7 28.Be5+ Kg8 29.Rf6 Rf7 30.Qf4 b6 31.Qh6 Bxg4 32.Rg6+ <i>1-0 Grob,H-Richard/corr 1966 (32) Black resigned.</i></div></div>",
  "4...Bc5": "<div class=\"alts\"><span class=\"cap\">вместо Bc5</span><div class=\"alt\"><b>4…Ne7</b>5.Nf3 Ng6 6.Nc3 Be7 7.e4 (7…Be6!) d4 8.Ne2 (8…c5 9.Ng3 Nh4 10.Nxh4 Bxh4 11.Nf5 Bxf5 12.exf5 Nc6 13.O-O Be7 14.Qe2 Qc7 15.f4 with initiative; H. Grob-Unknown) Nh4 9.Nxh4 Bxh4 10.Ng3 (10…Bxg3 11.fxg3 with 0-0 next.) g6 11.Bd2 Na6 12.O-O Nc7 13.Ne2 f5 14.exf5 gxf5 15.gxf5 Bxf5 16.Ng3 Bg6 17.Qg4 Rf8 18.Rae1! <i>1-0 Grob,H-Schurch/corr 1964 (18) Black resigned.</i></div><div class=\"alt\"><b>4…h6</b>(5.Nf3 Qc7 6.c4 dxc4 7.dxc4 e4 8.Nd4 Qe5 9.a3 Nf6 10.Nc3 Bd6 11.Be3 a6 12.Nb3 Nbd7 13.Qd4! <i>1-0 Grob,H-Frankenstein/ corr 1966 (13) winning the d-pawn.</i>) (5.e4 Bd6 6.Nc3 d4 7.Nce2 b5!? 8.Ng3 Nf6 9.a3 g5 10.Nf5 Bxf5 11.exf5 Qc7 12.Ne2 Nbd7 13.Ng3 O-O-O 14.O-O Rhe8 15.Bd2 Nc5 16.Qe1 Rd7 17.b3 Rde7 18.Ne4 with White having some threats; H. Grob-M. Gafafer, correspondence) 5.Nd2 Nf6 6.c4 Be6 7.Qb3 Nbd7 (8.Qxb7? Nc5 9.Qxc6+ Bd7! with the Queen lost.) 8.Ngf3 Qc7 9.Qc2 Bd6 10.a3 a5 11.b3 Bc5 12.e3 Qb6 13.O-O d4? 14.exd4 Bxd4 15.Nxd4 (15…Qxd4 was better.) exd4 16.f4! Nf8 17.f5 Bd7 18.c5 Qc7 19.Nc4! <i>1-0 Grob,H-Gahwiller/corr 1966 (35) threatening Bf4 followed by Nd6+ and Re1 and White wins easily.</i></div></div>",
  "5.Nf3": "<div class=\"alts\"><span class=\"cap\">вместо Nf3</span><div class=\"alt\"><b>5.Nc3</b>c3 Be6 6.e4 (6…d4 7.Nce2) Ne7 7.Nf3 Ng6 8.exd5 cxd5 (9.Qe2 and the position is unclear; H. Grob) 9.d4 exd4 10.Nxd4 Bb4 11.Qe2 Bxc3+ 12.bxc3 Qc8 13.O-O O-O 14.Qd3 Nc6 15.f4 <i>1-0 Grob,H-Scholl/corr 1965 (15) with advantage to White.</i></div></div>",
  "5...Qe7": "<div class=\"alts\"><span class=\"cap\">вместо Qe7</span><div class=\"alt\"><b>5…Nd7</b>6.e4 Ngf6 7.Qe2 (7…Qe7!) Qc7 8.exd5 cxd5 9.d4 Bd6 10.dxe5 Bb4+ 11.c3 Ne4 (12.cxb4? Qxc1+!) 12.O-O Be7 13.Bf4 g5 14.Bh2 Qc6 15.Nbd2 (15…Nxd2 is better.) Ndc5 16.Nd4 Qg6 17.Nxe4 Nxe4 18.Qb5+ Kf8 19.Qxd5 <i>1-0 Grob,H-Sennhauser/corr 1966 (30) with an easy win for White.</i></div><div class=\"alt\"><b>5…Qb6!?</b>6.O-O (6…f6 is better.) Nd7 7.Nbd2 Ne7 8.e4 Ng6 9.exd5 cxd5 10.Qe1 O-O 11.Nb3 Bd6 12.d4 e4 13.Nfd2 Nf4 <i>1-0 Bloodgood,C-Sokel,S/Norfolk 1959 (13) , after which White won because of his opponent's blunder, but Black clearly has the best of this. Improvements on White's 10th and 12th moves are probable.</i></div><div class=\"alt\"><b>5…Qf6!?</b>6.Bg5 (6…Qe6) Qg6? 7.Qd2 f6 8.Bh4 Be6 9.g5 fxg5 10.Nxg5 h6? 11.Nxe6 Qxg2 12.Rf1 Bb6 13.Bg3 Qxh3 14.Nxg7+ Kf7 15.Bxe5 Nd7 16.Qf4+ (16…Ke7 17.Nf5+) Ngf6 17.Nf5 Nxe5 18.Qxe5 <i>1-0 Bloodgood,C-Winterfield,E/Norfolk 1957 (18) Black resigned.</i></div></div>"})

add("c1", C2, "Вариант C1", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 c6 g5 e5 h4 Bd6 d3 Ne7 e4 d4 Nd2 Bb4 a3 Ba5 b4 Bc7 Bh3 Ng6 Nf1 Nf4 Bxf4 exf4 Qf3 O-O Bxc8 Qxc8 Nh3 f5 Nd2 fxe4 Nxe4 Qf5 Kd2 Nd7 Rag1 Ne5 Nf6+ gxf6 gxf6+ Kh8 Qg2 Qg6 Qxg6 hxg6 Ng5 Rxf6 h5 Kg7 h6+ Kh8 Kc1 a5 Ne4 Re6 Nc5 Re7 Nxb7 axb4 axb4 Ra1+ Kb2 Rxg1 Rxg1 Kh7 Rh1 Ng4",
 {
  "3.g5": "The \"Spike\" is a system which disrupts Black's normal lines of development and creates immediate problems for him. White has an obvious kind-side attack and to counter this, Black must react aggressively or literally expect to be pushed off the board",
  "3...e5": "<div class=\"alts\"><span class=\"cap\">вместо e5</span><div class=\"alt\"><b>3…g6</b>4.d3 Nd7 5.e4 Nc5 6.Nc3 Bg7 7.Nge2 dxe4 8.Nxe4 Nxe4 9.Bxe4 h6 10.f4 e5 11.fxe5 Bxe5 12.d4 Bg7 with an unclear position; analysis by H. Grob.</div><div class=\"alt\"><b>3…Bf5</b>4.d3 (4…e6 (5.Nd2 Qb6 6.b3 Nd7 7.e4 dxe4 8.dxe4 Bg6 9.h4 Bc5!? 10.Qe2 f6? 11.h5 Bf7 12.g6 hxg6 13.hxg6 Rxh1 14.gxf7+ winning a piece; H. Grob-Unknown This trap is important since it can occur frequently in the Spike.) (5.h4 Nd7? 6.e4! dxe4 7.dxe4 Qa5+ 8.Nc3 Bg6 9.h5 is another example.) 5.Nf3 Nd7 6.Nbd2 (6…Nc5 7.b4! Nd7 8.Bb2 f6 9.gxf6 Ngxf6 10.a3 Bd6 11.h3 Qe7 12.c4 e5 13.cxd5 Nxd5 14.Nc4 Nf4 15.Nxd6+ Qxd6 16.Bc1 O-O-O 17.Qc2 h6 18.b5 Rhe8 with equal chances; H. Grob-A. Clausen, corr.) Bd6 7.e4 Bg4 8.Nb3 h6 9.h4 hxg5 10.hxg5 Rxh1+ 11.Bxh1 Ne5 12.d4 Ng6 13.e5 Be7 14.Qd2 c5 15.Nh2 Bf5 16.f4 c4 17.Nc5 Qc7 18.Na4 b5 19.Nc3 Qc6 <i>1/2-1/2 Kwiesielewicz,I-Grob,H/corr 1966 (54) with advantage to Black.</i>) (4…e5 (5.h4 Qb6 6.e4 dxe4 7.dxe4 Be6 8.Nd2 Bc5 9.Qe2 Ne7 10.Ngf3 Bg4 11.Nc4! Qc7 12.Be3 Bxe3 13.Qxe3 O-O 14.O-O-O f5!? 15.Qb3! fxe4? 16.Nfxe5! Bxd1 17.Nb6+ Nd5 18.Nxd5 cxd5 19.Qxd5+ Kh8 20.Rxd1 Nc6 21.Ng6+ hxg6 22.h5! Nb4 23.Qb3 Nxc2 24.Kb1 Qh2 25.Bxe4 Rxf2 26.Qxb7 Re8 27.h6 Rg8 28.Rh1 Nd4! 29.hxg7+ Rxg7 30.Rxh2+ Rxh2 31.Qb8+ Rg8 32.Qxh2+ <i>1-0 Bloodgood,C-Trefzer,G/Norfolk 1958 (32) Black resigned.</i>) 5.Nc3 (5…Nd7 6.e4 dxe4 7.dxe4 Be6 8.Be3 Qc7 9.Qf3 Ne7 10.Nge2 Ng6 11.h4 Bd6 12.h5 Nf4 13.O-O-O Nxg2 14.Qxg2 O-O-O with equal chances.) Bc5 6.e4 Be6 7.Qe2 Ne7 (8.exd5? cxd5 9.Qxe5 Nbc6 10.Qxg7? Bd4 11.Qh6 Nb4 12.Kd1? Bg4+ Any 13 Nb5 traps the Queen.) 8.h4 d4 9.Nd1 Bb4+ 10.c3 dxc3 11.bxc3 Ba5 12.Nf3 Nd7 13.h5 Qc7 14.Bd2 O-O-O 15.Bh3 (15…Bxh3!) g6 16.Bxe6 fxe6 17.h6 (17…Nc5!?) Rhf8 18.O-O Nc5 19.Nb2 Rf7 20.Ne1 Rdf8 21.f3 Bb6 22.Kg2 a6 23.Nc4 Ba7 24.Ne3 Bb8 25.Ng4 Nd7 26.Be3 Nd5? unsound! 27.exd5! e4 28.f4 Rxf4 29.Bxf4 Rxf4 30.Rxf4 Qxf4 31.Qxe4 Qg3+ 32.Kf1! exd5 33.Qg2 Qf4+ 34.Nf3 Nc5 35.Nf2 <i>1-0 Grob,H-Weber/corr 1966 (35) Black resigned.</i>) Nd7? 5.e4! dxe4 6.dxe4 Bg6 7.h4 h5 8.f4 e6 9.Be3 Qc7 10.Qf3 Bd6 11.Nd2 Qa5 12.c3 <i>1/2-1/2 Grob,H-Laux,T/corr 1965 (12) with White having much the better position.</i></div></div>",
  "4.h4": "<b>h4!</b> — <div class=\"alts\"><span class=\"cap\">вместо h4</span><div class=\"alt\"><b>4.d3</b>d3 (4…Be6 (5.h4 Bc5 6.Nf3 Nd7 7.e4 Qb6 8.Qe2 d4!? 9.Bh3 Ne7 10.Nbd2 Bxh3 11.Rxh3 Ng6 12.Nb3 Bb4+ 13.Kf1! O-O-O 14.a3 Be7 15.h5 Ngf8 16.Bd2 Qc7 favors White; H. Grob-Unknown) 5.Nc3 Bc5 6.e4 Ne7 7.h4 Nd7 8.Qe2 d4! 9.Nd1 Bd6 10.Bh3 Nf8 11.f4 exf4 12.Qf2 Qa5+ 13.Kf1 Qc5 14.a3 Bxh3+ 15.Rxh3 Ne6 16.b4 Qb6 17.Nb2 Qa6 18.Bd2 Ng6 19.Nf3 h6 20.e5 hxg5 21.Qg2! Be7 22.hxg5 O-O-O! <i>1/2-1/2 Grob,H-Bischoff/corr 1964 (31) with equality.</i>) (4…Ne7 5.h4! Ng6 (6.e4) 6.h5!? Nf4 7.Bxf4 exf4 8.g6 (8…Qg5? 9.gxf7+ Kxf7 10.Bf3!) hxg6 9.hxg6 Rxh1 10.gxf7+ Kxf7 11.Bxh1 Qh4 (12.Bf3? Qh2 13.Kf1 Bh3+!) 12.Bg2 Qh2 13.Kf1 Bg4! 14.Nd2 Bc5 15.Ndf3 Bxf3 16.Nxf3 Qh5 17.d4 Bd6 18.c3 Nd7 19.e3 Re8 20.Qd2 fxe3 21.fxe3 Bg3 22.Ke2 Nf6 23.Rf1 Ne4?! this is risky! 24.Qc1 Bh4 25.Rh1! Ng3+ 26.Kd2 Nxh1 27.Qxh1 <i>1-0 Bloodgood,C-Evans,H/Norfolk 1958 (27) with advantage to White.</i>) Bg4 5.h3 Bh5 6.Bf3 (6…Bg6 7.Nc3? Bb4! <i>1/2-1/2 Grob,H-Eggenberger,H/corr 1964 (7)</i>) Bxf3 <i>1/2-1/2 Grob,H-Denring/corr 1966 (14)</i></div></div>",
  "4...Bd6": "<div class=\"alts\"><span class=\"cap\">вместо Bd6</span><div class=\"alt\"><b>4…Bc5</b>5.d3 (5…Qb6 6.e3 Ne7 7.Ne2 Be6 8.Nd2 Nd7 9.a3 O-O 10.Bh3 Bxh3 11.Rxh3 f5 12.Nb3 Qc7 13.d4 Bd6 14.dxe5 Nxe5 15.Nf4 Qd7 16.Nd4 N5g6 17.Nfe6 Rf7 18.b4 with a solid advantage; H. Grob-Unknown) d4? 6.Nf3 Qd6 7.Nbd2 Be6 8.Ne4 (8…Qc7 9.Nxc5 Qa5+!) Qd5? 9.Nfd2 Ke7 (answering the threat 10 Nf6+) 10.Kf1 Bb6 11.Nc4 Nd7? (Black is trying to avoid a number of Queen traps and survive the attack. Something has to fall) 12.Ned6! <i>1-0 Grob,H-Sperling/London 1952 (12) Black resigned.</i></div><div class=\"alt\"><b>4…Be6</b>5.d3 Bd6 6.e4 Ne7 7.Nc3 Nd7 8.Bh3 Bxh3 9.Nxh3 d4 10.Ne2 f5 11.exf5 Nxf5 12.Ng3 (12…Nxh4? 13.Qh5+ Ng6 14.Ne4! with attack!) Nxg3 13.fxg3 Qe7 14.Qh5+ g6 15.Qg4 Rf8 16.Bd2 e4! <i>0-1 Grob,H-Roesler,M/corr 1964 (36) and Black stands better. White can improve this!</i></div><div class=\"alt\"><b>4…g6</b>5.d3 (5…h5 6.e4 d4 7.Ne2 c5 8.f4 exf4 9.Bxf4 Nc6 10.Nd2 Be6 favors White; H. Grob-Unknown) Bg7 6.h5! gxh5 7.Rxh5 Bg4 8.Rh4 Bf5 9.e4 dxe4 10.Bxe4 Bxe4 11.Rxe4 Nd7 12.Be3 f5 13.Qh5+ Kf8 14.Rh4 (14…f4) h6? 15.g6 f4 16.Qf5+ Ngf6 (17.Qe6? Qe7! 18.Qxe7+ Kxe7 19.Bd2 Rae8 <i>0-1 Bloodgood,C-Lundy,L/Virginia 1968 (19) favors Black.</i>) 17.Nc3 fxe3 18.fxe3 Qb6 19.O-O-O Qxe3+ 20.Kb1 Re8 21.Rf1 Nc5 22.Nf3 Kg8 23.Ne4 Ncxe4 24.Rxe4 Qc5 25.Rxe5 Rxe5 26.Nxe5 Qe7 27.Nf7 Nd5 28.Qc8+ Bf8 29.Nxh8 h5 30.a4 Qd6 31.Rf7 <i>1-0 Bloodgood,C-Lundy,L/New Castle Delaware 1968 (31) Black resigned.</i></div><div class=\"alt\"><b>4…f5</b>: Mani-H. Grob, corr., cont. (5.gxf6? Nxf6 (6.e3 is better) 6.d3 Bc5 (7.c3 Qb6!) 7.e3 Be6 8.Ne2 Nbd7 9.d4 Bb6 10.Nd2 Qe7 11.Nb3 O-O-O 12.dxe5 Nxe5 (13.Nbd4 was better) 13.Nf4 Bf5 14.Nd4 Bxd4 15.Qxd4 b6 16.Qa4 Kb7 17.Bd2 Be4 18.O-O-O Bxg2 19.Nxg2 Ne4 <i>0-1 Grob,H-Kast,H/corr 1966 (32) with advantage to Black.</i>) (5.d4 e4 6.Bf4 Bd6 7.Nh3 Ne7 8.h5 Be6 9.c3 Qc7 10.e3 Nd7 11.Nd2 c5 12.Rc1 b5 13.Bxd6 Qxd6 14.Nf4 c4 15.a3 a5 (16.O-O! with 17. f3 following) 16.Nf1? b4 17.axb4 axb4 18.Ng3 Nb6 19.Ra1 Rxa1 20.Qxa1 Bd7 21.O-O O-O <i>1/2-1/2 Grob,H-Blatti/Barcelona 1966 (44) with counterplay.</i>) 5.d3 Bc5 6.e3 Bb6 (7.d4 e4!) 7.b3 Be6 8.Bb2 Nd7 9.Qe2 (9…Qe7) Ne7? 10.f4! Qc7 11.Nd2 O-O 12.h5 Rfe8 13.Nh3 c5 14.fxe5 Nxe5 15.Nf4 Qd6 16.O-O-O with strong attack.</div></div>",
  "5.d3": "<div class=\"alts\"><span class=\"cap\">вместо d3</span><div class=\"alt\"><b>5.e4</b>e4 after which: H. Grob-E. Denring, corr., cont. (5…d4 6.d3 Be6 7.Ne2 Ne7 8.f4 g6 9.fxe5 Bxe5 10.Bf4 Nd7 11.Nd2 Qc7 12.Bxe5 Nxe5 13.Nxd4 Bg4 14.N4f3 Nxf3+ 15.Nxf3 Qg3+ 16.Kf1 O-O-O 17.Qe1 Qd6 18.Bh3 Bxh3+ 19.Rxh3 with advantage to White.) dxe4 6.Nc3 f5 (7.Nge2!?) 7.gxf6 Nxf6 8.Nxe4 O-O 9.d3 Nxe4 10.Bxe4 Nd7 11.Bg5 Nf6 with some initiative for White.</div></div>",
  "5...Ne7": "<div class=\"alts\"><span class=\"cap\">вместо Ne7</span><div class=\"alt\"><b>5…Be6</b>6.e4 Ne7 (7.Nc3 f5!? 8.gxf6 gxf6 9.Qh5+ favors White; H. Grop-Unknown) 7.Nd2 O-O!? 8.Bh3 Bxh3 9.Nxh3 (9…Nd7) f5!? 10.gxf6 Rxf6 11.exd5 (11…cxd5!) Nxd5? 12.Ne4 Rf7 13.Bg5 Be7 14.Qg4 Qa5+ 15.c3 Bxg5 16.Nhxg5 Rf8 17.Qe6+ Kh8 18.Nf7+ (18…Rxf7 19.Qe8+ Rf8 20.Qxf8#) Kg8 19.Nh6+ Kh8 20.Qg8+ Rxg8 21.Nf7# <i>1-0 Bloodgood,C-Evans,B/Norfolk 1961 (21)</i></div><div class=\"alt\"><b>5…Bg4!?</b>Grob gives this as best and cites the following variation (6.Bh3 Bh5 7.c4 dxc4 8.dxc4 Bb4+ 9.Bd2 Na6 10.Nc3 Qd4 11.Qb3 Rd8 12.Rd1 Bxc3 13.Bxc3 Qxd1+ 14.Qxd1 Rxd1+ 15.Kxd1 f6 16.f3 Ne7 with equality from his postal play) 6.Nd2 f5 7.f3 Bh5 8.e4 fxe4 9.dxe4 dxe4 10.Nxe4 Bb4+ 11.Bd2 Na6 12.c3 Ba5 13.Qb3! Nc5 14.Qc4 Nd3+ 15.Kf1 Nxb2 16.Qe6+ Qe7 17.Nd6+ Kf8 18.Qf5+ Bf7 19.Nxf7 Qxf7 20.Qxf7+ Kxf7 21.Rb1 Nc4 22.Rxb7+ Kf8 23.Be1 Ne7 24.Ne2 Bb6 25.Bf2 Ne3+ 26.Bxe3 Bxe3 27.Ng3 Bf4 28.Ne4 Kf7 29.Bh3 Rhd8 30.Ke2 a5 31.Rhb1 Kf8 32.c4 a4 33.Bd7 h6 34.Nc5 Kf7 35.Be6+ Ke8 36.Nd7 Ng6? Black is very cramped, but a waiting move was all that he could play. 37.h5! Nf8 38.Nf6+ gxf6 39.Bf7# <i>1-0 Bloodgood,C-Lewis,R/Norfolk 1961 (39)</i></div></div>",
  "6.e4": "The move is probably best, but a little exploration here is overdue.",
  "6...d4": "<div class=\"alts\"><span class=\"cap\">вместо d4</span><div class=\"alt\"><b>6…Be6</b>7.h5 Nd7 8.Nc3 Qb6!? 9.Qf3 O-O 10.Bh3 Bxh3 11.Qxh3 Qc7 12.Nf3 Nc5 13.Nh4 in White's favor.</div><div class=\"alt\"><b>6…O-O</b>7.Nc3 d4! 8.Nce2 f5 9.gxf6 Rxf6 10.h5 Qf8 11.f3 a5 12.Bg5 Rf7 (13.Ng3!) 13.a3? b5 14.Ng3 h6 15.Bd2 c5 in Black's favor.</div><div class=\"alt\"><b>6…O-O</b>7.Nc3 Be6 (8.h5 Nd7 9.Nf3 d4 10.Ne2 c5 11.Ng3 g6 12.Nh4 Qc8 13.b3 Rb8 14.Bh3 Bxh3 15.Rxh3 b5 16.Qg4!? Nb6! <i>0-1 Grob,H-Sempert/corr 1964 (36) with complications favoring Black</i>) 8.Bh3! Bxh3 9.Nxh3 d4 10.Ne2 f5!? 11.gxf6! Rxf6 12.Bg5 Rf7 13.Rg1 Nd7 14.Ng3 (14…Nf6!) Qf8 15.Qg4 Nf6 16.Qe6! Bb4+ 17.Ke2 Re8 18.Qc4 Bd6 19.Bxf6 Black resigned.</div><div class=\"alt\"><b>6…O-O</b>7.Nc3 Be6 8.Bd2 (8…b6!? 9.Nce2 Nd7 10.Ng3 g6? 11.h5! wins for White; H. Grob-Unknown, corr.) Nd7 9.h5 d4 10.Nce2 (10…Re8) c5!? 11.Bh3 Bxh3 12.Nxh3 b5 13.Ng3 f5 14.exf5 Nxf5 15.Qg4! wins for White.</div></div>",
  "7.Nd2": "<div class=\"alts\"><span class=\"cap\">вместо Nd2</span><div class=\"alt\"><b>7.Bh3</b>h3 Bxh3 8.Nxh3 O-O 9.Qg4 (9…Qc8!) Qd7? 10.Qg3 <i>1/2-1/2 Grob,H-David/corr 1965 (10) in White's favor.</i></div></div>",
  "10...Ng6": "<div class=\"alts\"><span class=\"cap\">вместо Ng6</span><div class=\"alt\"><b>10…Bxh3</b>11.Nxh3 O-O 12.f4 exf4 13.Qg4 f5 14.gxf6 Rxf6 (15.h5!) 15.Nf3!? Rg6 16.Nhg5 h6 17.h5 Rf6 18.Ne6 Black resigned.</div></div>",
  "11...Nf4": "<b>Nf4?</b> — <div class=\"alts\"><span class=\"cap\">вместо Nf4</span><div class=\"alt\"><b>11…Bxh3!</b></div></div>",
  "21...Kh8": "<div class=\"alts\"><span class=\"cap\">вместо Kh8</span><div class=\"alt\"><b>21…Ng6!?</b></div></div>",
  "34...Ng4": "0-1 Bloodgood,C-Meyerhofer,E/ Virginia 1967 (34) White resigned."})

add("a2", C3, "Вариант A2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 e4 dxe4 Bxe4 Nf6 Bf3 e4 Be2 Nc6 h4 Bc5",
 {
  "3.e4": "<b>e4!?</b> — This is definitely not recommended!",
  "5.Bf3": "<div class=\"alts\"><span class=\"cap\">вместо Bf3</span><div class=\"alt\"><b>5.f3?</b>3? Nxe4 6.fxe4 Qh4+ with a strong attack for Black.</div></div>",
  "7...Bc5": "Black threatens 8...Qd4! This is obviously not good for White."})

add("b2", C3, "Вариант B2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 Be6 Qb3 Nd7 cxd5 Bxg4 Qxb7 Rb8 Qc6 Bc5 Nc3 Rb6 Qa4",
 {
  "3...Be6": "<b>Be6!?</b> — <div class=\"alts\"><span class=\"cap\">вместо Be6</span><div class=\"alt\"><b>3…Bxg4!?</b>4.Qb3 Bc8 5.cxd5 Where White gains a solid advantage.</div></div>",
  "4.Qb3": "<b>Qb3!</b>",
  "4...Nd7": "<div class=\"alts\"><span class=\"cap\">вместо Nd7</span><div class=\"alt\"><b>4…b6</b>5.cxd5 Bxg4 6.Qg3 Nf6 7.Qxe5+</div></div>",
  "7.Qc6": "<div class=\"alts\"><span class=\"cap\">вместо Qc6</span><div class=\"alt\"><b>7.Qxa7?</b>7? Bc5 and Black has an attack.</div></div>",
  "9.Qa4": "with White holding the pawn at the cost of the initiative."})

add("c2", C3, "Вариант C2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 d4 d3 c6 e4 Nd7 a3 a5 Nd2 Nc5 Nf1 h5 gxh5 Qh4 Bf3 Nf6 Ng3 Ng4 h3 Nf6 Qe2 a4 Nf5 Bxf5 exf5 Bd6 h6 gxh6",
 {
  "3...d4": "This is an awkward line for Black which creates more problems than it solves.",
  "4.d3": "<div class=\"alts\"><span class=\"cap\">вместо d3</span><div class=\"alt\"><b>4.b4!?</b>!? c6 5.h3 (5…Bxb4!) Be6? 6.Qb3 (6…Qb6!) b5!? 7.d3 Be7 8.a4 bxc4 9.dxc4 Qb6 10.b5 <i>1-0 Bloodgood,C-Campbell,W/corr Zugzwang 1975 (10) where White's advantage is due to Black's weak play.</i></div></div>",
  "5.e4": "<div class=\"alts\"><span class=\"cap\">вместо e4</span><div class=\"alt\"><b>5.h3</b>h3 (5…h6 6.Nf3 Bd6 7.Nbd2 Nf6 8.a3 a5 9.g5 hxg5 10.Nxg5 Na6 11.Nde4 Nxe4 12.Nxe4 Be7 13.e3 f5 (14.Ng3 dxe3 15.fxe3 Bh4!) 14.Nd2 dxe3 15.Nf3 e4 16.dxe4 Qxd1+ 17.Kxd1 exf2 18.exf5 Bxf5 19.Ke2 <i>1-0 Grob,H-Wyss/corr 1965 (59) with White struggling to hold equality.</i>) (5…Ne7! 6.Nf3 Ng6 (7.e4 dxe3 8.Bxe3 f5! 9.gxf5 Bxf5 favors Black according to Grob.) 7.g5!? f5! 8.gxf6 Qxf6 9.Bg5 Qf5 10.Bd2 Bd6 <i>0-1 Bloodgood,C-Erwin,H/Virginia 1972 (10) with advantage to Black.</i>) Be6!? 6.Nf3 Nd7 7.Ng5 Qe7 8.a3 f6 9.Nxe6 Qxe6 10.e3 dxe3 11.Bxe3 Bc5 12.Nc3 a5 13.Ne4 Bd4 14.Bxd4 exd4 15.O-O <i>1/2-1/2 Grob, H-Brechbuhler/corr 1965 (15) with White having the better position.</i></div></div>",
  "5...Nd7": "<div class=\"alts\"><span class=\"cap\">вместо Nd7</span><div class=\"alt\"><b>5…dxe3</b>6.Bxe3 Bloodgood-H. Erwin, 1972, cont. f5 7.gxf5 Bxf5 (8.d4? Bxb1 9.Rxb1 Qa5+ ; Grob) 8.Nf3 (8…Bxd3 9.Nxe5 Qa5+ 10.Nc3 Qxe5 11.Qxd3 with a good position; Grob) Bb4+ 9.Nbd2 (9…Qxd3 10.Nxe5!) Qa5 (10.Qc2 with equality; Grob) 10.Qb3 Nd7 11.a3? Bxd2+? 12.Bxd2 Qc7 (13.Be3) 13.O-O-O?? Nc5! 14.Qc3 Nxd3+ and White resigned. This line is worth exploring for White.</div></div>",
  "6.a3": "<div class=\"alts\"><span class=\"cap\">вместо a3</span><div class=\"alt\"><b>6.Nd2</b>d2 (6…Nc5 7.Nb1!) Ne7 7.Nf1 Ng6 8.Nf3 Bb4+ 9.Ke2 Nf6 10.h3 h6 11.Ng3 Qa5 12.a3 Bd6 13.Nf5 Bxf5 14.exf5 Nf4+ 15.Kf1 (15…Nxg2!) Nd7 16.Bxf4 exf4 17.Qe1+ Qxe1+ 18.Rxe1+ <i>1-0 Grob,H-Wyss/corr 1967 (18)</i> Kd8 19.Nxd4 (19…Be5 20.Nc2 Bxb2 21.Rb1! Grob) Kc7 20.b4 with a solid advantage for White.</div></div>",
  "7...Nc5": "<div class=\"alts\"><span class=\"cap\">вместо Nc5</span><div class=\"alt\"><b>7…Qb6</b>8.h3 Bd6 9.Nf1 Ne7 10.Ne2 Ng6 11.h4 h5 12.g5 Nc5 13.Nfg3 Qb3 14.Qxb3 Nxb3 15.Rb1 Nc5 16.Kd2 Nf4 17.Nxf4 exf4 18.Ne2 with equality.</div></div>",
  "8...h5": "<b>h5!?</b> — Perhaps Black does best with 8...N e7 to g6; however the text is the most aggressive move at Black's disposal.",
  "9.gxh5": "<div class=\"alts\"><span class=\"cap\">вместо gxh5</span><div class=\"alt\"><b>9.g5!</b>5! h4! 10.Bh3 Be7 11.Bxc8 Qxc8 12.Qf3 f6 13.g6 Nh6 14.Nh3 (14…Nb3) f5? 15.Bxh6 Rxh6 16.exf5 Bf6 17.Nd2 b5!? 18.cxb5 cxb5 19.O-O Rb8 20.Rac1 b4 21.Ne4 <i>1-0 Bloodgood,C-Erwin,H/ Virginia 1972 (21) Black resigned.</i></div></div>",
  "14.Nf5": "<b>Nf5?</b>",
  "16...gxh6": "(H. Erwin-D. Stroemer, 1972) with advantage to Black."})

add("d2", C3, "Вариант D2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 dxc4 Qc2",
 {
  "4.Qc2": "This is definitely not a gambit pawn, e. g. — <div class=\"alts\"><span class=\"cap\">вместо Qc2</span><div class=\"alt\"><b>4.Qa4+</b>4+ c6 5.Qxc4 forcibly regains it immediately.</div><div class=\"alt\"><b>4.b3!?</b>!? is not good, e.g. Qd4! 5.Nc3 Qxg4 6.Bh3 Qg6 7.Bxc8 Qg2! with a winning advantage for Black. At this point, two important lines of defence are possible: Variation \"D2a\" 4...c6; and Variation \"D2b\" 4...Qd4.</div></div>"})

add("d2a", C3, "Вариант D2a", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 dxc4 Qc2 c6 Qxc4 Be6 Qc3 Bd6 Nf3 Qc7 h3 f6 d4 Nd7 Nbd2 Ne7 e4 Ng6 Nc4 O-O-O d5 Bf7 Nxd6+ Qxd6 dxc6 Nc5 cxb7+ Kb8 O-O Nxe4 Qa5 Qd5",
 {
  "5...Be6": "<b>Be6!</b> — This is the only aggressive reply.",
  "6.Qc3": "<div class=\"alts\"><span class=\"cap\">вместо Qc3</span><div class=\"alt\"><b>6.Qa4</b>a4 (6…Nd7! followed by) Bd5 7.Nf3 (7…h5!) e4!? 8.Nd4 Qh4 9.h3 Qg5 10.Nc3 Nf6 11.Nf5! Nbd7 12.d4 b5 13.Qd1! e3 14.Bxe3 Bxg2 15.Bxg5 Bxh1 16.f3 With a winning advantage for White.</div><div class=\"alt\"><b>6.Qe4</b>e4 when Black replies Nd7 with</div></div>",
  "6...Bd6": "<div class=\"alts\"><span class=\"cap\">вместо Bd6</span><div class=\"alt\"><b>6…Nd7</b>(7.d4 Qf6!) 7.h3 Grob-Dr. F. Veit, corr., continued Ngf6 8.a3 a5 (9.d3 Bb4 10.axb4 axb4 11.Rxa8 Qxa8 12.Qxb4 Qa1 wins for Black; Grob) 9.Qg3 Bd6 (10.d4? Qb6!) 10.Nc3 Nc5 (11.Rb1 Bb3!) 11.Qh4 (11…Qc7 12.d3 O-O 13.Be3 Ne8 14.Ne4 Nxe4 15.Bxe4 f5 16.gxf5 Bxf5 17.Bxf5 Rxf5 18.Qc4+ Kh8 19.Nf3 Be7? 20.Qe6! Rh5 21.Rg1 Nf6? 22.Ng5! h6 23.Nf7+ Kh7 24.Nxh6 Rxh6 25.Bxh6 Kxh6 26.Qf5! <i>1-0 Grob, H-Veit/corr 1966 (26)</i>) Nb3 12.Rb1 Nd4 13.d3 Qc7 14.Nf3 (14…Nxf3+!) Nc2+? 15.Kf1 with advantage for White.</div></div>",
  "7.Nf3": "<div class=\"alts\"><span class=\"cap\">вместо Nf3</span><div class=\"alt\"><b>7.h3</b>h3 f6 (8.Na3 Qb6 9.Nc4 Qb4 10.Nxd6+ Qxd6 11.a3 Nd7 12.b4 Ne7 13.d3 with an unclear position; Grob) 8.a3 (8…Ne7) Qb6!? (9.Nf3) 9.b4!? a5! 10.Nf3 axb4 11.axb4 Rxa1 12.Qxa1 (12…Bxb4? 13.Nxe5!) Qxb4! 13.Ba3 Qc4 14.Nc3 Bxa3 15.Qxa3 Na6 16.O-O Ne7 17.Rc1 Qb3 18.Qxb3 Bxb3 19.Rb1 Nc5 20.d4 exd4 21.Nxd4 Bc4 22.Nxc6 Nxc6 23.Bxc6+ (23…Kf7) bxc6? 24.Rb8+ Ke7 25.Rxh8 h6 26.f4 Ne6 27.e3 Nf8 28.h4 Kf7 29.Ne4 Bd5 30.Nd6+ Ke7 31.Nf5+ Kf7 32.h5 Ne6 33.Nxh6+ gxh6 34.Rxh6 c5 35.Rh8 c4 36.h6 Nf8 37.h7 <i>1-0 Bloodgood,C-Baker,E/ Virginia 1973 (37) Black resigned.</i></div></div>",
  "7...Qc7": "<div class=\"alts\"><span class=\"cap\">вместо Qc7</span><div class=\"alt\"><b>7…f6</b>8.h3 Ne7 9.e4 Ng6 10.d3 Nd7 11.Be3 Nf4 12.Bf1 Qe7 13.Nbd2 Bb4 14.Qc2 Qf7 15.b3 Ng6 16.Qc1 O-O 17.Be2 c5 18.Qb2 Rac8 19.Rg1 Ba5 20.h4 Bc7 21.Rc1 Bb8 22.a4 Rfd8 23.h5 Nf4 24.Nh4 b6 25.Nc4 Bxc4 26.dxc4 Nf8 27.g5 N8e6 28.g6 hxg6 29.hxg6 Qb7 30.f3 Nd4 31.Bf1 Nxf3+ 32.Nxf3 Qxe4 33.Kf2 Nxg6 34.Bh3 Rd3!? 35.Be6+ Kf8 36.Rce1 <i>1-0 Roesler,C-Grob,H/corr 1966 (36) with a winning advantage.</i></div><div class=\"alt\"><b>7…Nd7</b>(8.d4? Qb6!) 8.h3 Ne7 9.Na3 (9…Qb6 10.Nc4 Qb4) O-O!? 10.Nc4 Bc7 11.Ncxe5 Nxe5 12.Nxe5 Nd5 13.Qd4 Qf6 14.Nf3 Nf4 15.Qxf6 Nxg2+ 16.Kf1 gxf6 17.Kxg2 <i>1-0 Bloodgood,C-Brenneman,M/Virginia 1973 (17) with a winning advantage for White.</i></div></div>",
  "8...f6": "<b>f6!</b> — <div class=\"alts\"><span class=\"cap\">вместо f6</span><div class=\"alt\"><b>8…Nd7</b>9.Ng5! Nc5 10.b4 Nd7 11.Nxe6 fxe6 12.Qb3 <i>1-0 Grob,H-Ruegg/corr 1966 (45) with advantage to White.</i></div><div class=\"alt\"><b>8…Na6?</b>9.Ng5! Qd7!? 10.Nxe6 Qxe6 11.Bxc6+ Ke7 12.Bxb7 <i>1-0 Grob,H-N. N./corr 1966 (12) with an easy win for White.</i></div></div>",
  "10.Nbd2": "<div class=\"alts\"><span class=\"cap\">вместо Nbd2</span><div class=\"alt\"><b>10.Be3</b>Be3 Ne7!</div></div>",
  "11.e4": "<b>e4!</b>",
  "11...Ng6": "<div class=\"alts\"><span class=\"cap\">вместо Ng6</span><div class=\"alt\"><b>11…O-O</b>12.Nc4 Ng6 13.Nxd6 Qxd6 14.Be3 (14…Nb6 15.b3 Nc8 16.Rd1 Qc7 17.O-O Nd6 18.d5 Nxe4? 19.Qc2 <i>1-0 Grob,H-N. N./corr 1966 (19) winning a piece</i>) Rac8 15.Rd1 Qb8 16.O-O exd4 17.Nxd4 Bf7 18.f4 c5 19.Nf5 Nb6 20.h4 Nc4 21.h5 <i>1-0 Grob,H-Brechbuhler/corr 1966 (21) with a winning advantage.</i></div><div class=\"alt\"><b>11…a5</b>(12.Bf1 b5 13.a3 O-O 14.Qc2 b4 15.Bc4 favors White; Grob) 12.a3!? b5 13.d5 Bf7 14.O-O O-O 15.dxc6 (15…b4!) Nxc6 16.Qe3 Nd4? 17.Nxd4 Bc4? 18.Qc3? Bxf1 19.Qxc7 Bxc7 20.Bxf1 b4 21.Ne6 Rfc8 22.Nxc7 Rxc7 23.axb4 Rca7 24.b5 Rb8 25.Nb3 a4 26.Be3 Raa8 27.Bc4+ Kf8 28.Nc5 Nxc5 29.Bxc5+ Ke8 30.Bd5 Ra5 31.Bc6+ Kf7 32.Bd6 Rc8 33.Bb4 Ra7 34.Bc5 Rac7 35.Rxa4 <i>1-0 Bloodgood,C-Lawson,J/Virginia 1973 (35) Black resigned.</i></div><div class=\"alt\"><b>11…O-O-O</b>where Black can contest the king's side more actively.</div></div>",
  "13.d5": "White has some advantage, but this is very minimal.",
  "13...Bf7": "<div class=\"alts\"><span class=\"cap\">вместо Bf7</span><div class=\"alt\"><b>13…cxd5?</b>14.Nxd6+ is not particularly good for Black, so 13...Bf7 is forced; after which:</div></div>",
  "15.dxc6": "<div class=\"alts\"><span class=\"cap\">вместо dxc6</span><div class=\"alt\"><b>15.Be3</b>Be3 is sharper</div></div>",
  "15...Nc5": "<b>Nc5!</b>",
  "17.O-O": "<b>O-O!</b>",
  "18...Qd5": "with an unclear position. (Grob-B. Brechbuhler, corr. 1966)"})

add("d2b", C3, "Вариант D2b", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 dxc4 Qc2 Qd4 Nf3 Qxg4 Rg1 Qe6 Ng5 Qf5 Qxc4 c6 Bh3",
 {
  "5...Qxg4": "<div class=\"alts\"><span class=\"cap\">вместо Qxg4</span><div class=\"alt\"><b>5…Qc5</b>6.Na3 Be6 7.Ng5 Bd5 8.e4 Bc6 9.Qxc4 with an unclear position; Grob.</div></div>",
  "6...Qe6": "<div class=\"alts\"><span class=\"cap\">вместо Qe6</span><div class=\"alt\"><b>6…f6</b>(7.Nxe5 fxe5 8.Bc6+ Nxc6 9.Rxg4 Bxg4 is not good.) 7.d3 cxd3 (8.Qxc7? Nc6!) 8.exd3 c6 9.Be3 Bb4+ 10.Nc3 Qe6 11.Nd2 (11…Nd7!) f5!? 12.O-O-O Nf6 13.Kb1 O-O 14.Rde1 Bxc3 15.Qxc3 Nd5 16.Qa3 (16…Qf7) b5 17.Bd4! b4? 18.Rxe5 bxa3 19.Rxe6 Bxe6 20.Bxd5 Re8 21.Rxg7+ Kf8 22.Bxe6 Rxe6 23.Rxh7 Ke8 24.bxa3 Nd7 25.Kc2 a6 26.Nc4 Rb8 27.f4 Re2+ 28.Kc3 Rxa2 29.Be5 Nxe5 30.fxe5 Rb5 31.h4 f4 32.Nd6+ Kf8 33.Nxb5 axb5 34.e6 Ke8 35.Rf7 Rxa3+ 36.Kd4 Ra4+ 37.Kc5 f3 38.h5 Rh4 39.d4 b4 40.d5! <i>1-0 Grob,H-David/corr 1966 (40) Black resigned.</i></div></div>",
  "7.Ng5": "White has a strong attack!",
  "7...Qf5": "<b>Qf5!?</b>",
  "8.Qxc4": "<b>Qxc4!</b>",
  "9.Bh3": "<b>Bh3!</b> — (Bloodgood- R. Traylor, 1973) Winning a piece."})

add("e", C3, "Вариант E", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 Be6 Qxb7 Nbc6 Nb5 Rc8 Nf3 a6 Qxa6 Nb4 Nd6+ Kd7 Nxe5+ Kc7 Nb5+ Kb8 Qa7#",
 {
  "3...c6": "This is the key line in Grob's Attack, and the tactical aspects of the position are unlimited.",
  "4...cxd5": "<div class=\"alts\"><span class=\"cap\">вместо cxd5</span><div class=\"alt\"><b>4…h5!?</b>5.dxc6 Nxc6 6.gxh5 Nh6 7.d3 Bc5 8.Nc3 Ng4 9.Bxc6+ bxc6 10.Ne4 Qh4 11.Qa4! with advantage for White.</div></div>",
  "5...Ne7": "<div class=\"alts\"><span class=\"cap\">вместо Ne7</span><div class=\"alt\"><b>5…Be6?</b>(6.Qxb7? Nd7 7.Bxd5? Rb8 8.Qc6 Ne7 And White loses the Bishop) 6.Nc3! (6…d4? 7.Qxb7! wins for White) Nd7 7.Bxd5 Nc5 8.Qb5+ Qd7 9.Bxe6 Nxe6 10.Qxe5 Rc8 11.Nf3 Ne7 12.d3 Nc6 13.Qe4 Be7 14.Be3 O-O 15.d4 Na5 16.Nd2 Nc4 17.Nxc4 with a winning advantage for White. Rxc4 <i>1-0 Grob,H-Chevalier,D/corr 1967 (17)</i></div><div class=\"alt\"><b>5…e4</b>6.Nc3 Ne7 7.d3 (7…exd3 is the best) f5? 8.gxf5 Nxf5 9.dxe4 dxe4 10.Bxe4 Nc6 11.Nf3 Nfd4 12.Qc4 Bf5 13.Bxf5 Nxf5 14.Qe6+ Nfe7 15.Bf4 <i>1-0 Grob,H-Hasler/corr 1966 (23) with a pawn and the attack.</i></div><div class=\"alt\"><b>5…Qc7</b>6.Nc3 d4 7.Nd5 Qd7 8.d3 Nc6 9.Bd2 b6 10.Rc1 Bb7 11.Be4 Nge7 12.Nf3 f6 13.Nxe7 Nxe7 14.Bxb7 Qxb7 15.g5 Qd5 16.Qa4+ Qd7 17.Qa6 Nf5 18.Rg1 Bd6 19.gxf6 gxf6 20.Qc4 Qf7 21.Qc6+ Ke7 22.Qe4 Qh5 23.Ng5 fxg5 24.Qxf5 h6 25.Rxg5 Qf7 26.Qh3 Rag8 27.Rxe5+ Bxe5 28.Bb4+ Kf6 29.Rc6+ Kg7 30.Qg4+ Kh7 31.Qe4+ Rg6 32.h4 Qe8 33.Rxg6 Qxg6 34.Qxe5 Rc8 35.Kd2 Qg4 36.f3 Qd7 37.Bd6 Rd8 38.Qe4+ (38…Kg7!) Kg8? 39.Be7! <i>1-0 Grob,H-Lenherr/corr 1966 (39) Black resigned.</i></div><div class=\"alt\"><b>5…Nf6</b>6.g5 Ne4 7.Nc3 (7…Nxc3!) Qxg5!? (8.Kf1! Nxc3 9.dxc3 Qg6!? 10.Bxd5 Nc6 11.Nf3 f6 12.Rg1 Qh5 13.Qb5! Kd7 14.Bg5 fxg5 15.Nxe5+ (15…Kd8 16.Nxc6+) Ke7 16.Nxc6+ Kf6 17.Ne5 Bh3+ 18.Ke1 Rd8 19.Bf7 Qh4 20.Nf3 Qe4 21.Nxg5 Qf5 22.Qxb7 Bc5 23.Ne4+ <i>1-0 Bloodgood,C-Boothe,J/Virginia 1973 (23) Black resigned.</i>) 8.Bxe4 dxe4 9.Nxe4 Qg2 10.Qb5+ Nc6 11.Ng3 a6 (12.Qb6!?) 12.Qa4 b5 13.Qe4 Qxe4 14.Nxe4 Nd4 15.Kd1 Bb7 16.f3 Rc8 17.b3 Bb4 18.Bb2 O-O 19.a3 Ba5 20.b4 Bb6 <i>1/2-1/2 Bloodgood,C-Stroemer,D/Virginia 1972 (20) with counterplay.</i></div></div>",
  "6.Nc3": "While there are several lines which are playable for Black at this point, there are also several which appear playable, but which lose. Clearly bad are:",
  "6...Be6": "<b>Be6?</b> — <div class=\"alts\"><span class=\"cap\">вместо Be6</span><div class=\"alt\"><b>6…Qd7</b>7.Nxd5 Nxd5 8.Bxd5 Nc6 9.Nf3 Rb8 10.Rg1 (10…Nd8!) Bd6 11.Ng5 (11…Nd8) O-O? 12.Qd3 g6 13.Qh3 h5 14.Qd3 Kg7 15.gxh5 Ne7 16.hxg6 Qf5 17.Be4 Qf6 18.Nh7 Qh4 19.gxf7+ Kxf7 20.Bg6+ Nxg6 21.Qxg6+ Ke7 22.Nxf8 Bc5 23.Qh7+ <i>1-0 Grob,H-Gaffar,A/corr 1966 (23) Black resigned.</i></div><div class=\"alt\"><b>6…Bxg4?</b>7.Qxb7 Nbc6 8.Nxd5 Rc8 9.Nxe7 Nxe7 10.Qxa7 <i>1-0 Bloodgood,C-Erwin, H/Virginia 1972 (10) with a winning advantage for White.</i></div></div>",
  "10...Nb4": "<b>Nb4?</b>",
  "14.Qa7#": "(Braune-Rupprecht, 1956) The playable lines to be considered are: Variation \"E1\" 6...d5, Variation \"E2\" 6... Nc6, and Variation \"E3\" 6... e5!?"})

add("e1", C3, "Вариант E1", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 d4 Nd5 Nbc6 Nxe7 Qxe7 h3 g6 a3 Be6 Bd5 Bxd5 Qxd5 Rd8 Qe4 Bg7 d3 O-O g5 f5 gxf6 Qxf6 Nf3 Qf7 Bg5 Bf6 h4 Rc8 h5 Bxg5 hxg6 hxg6 Rg1 Bh6 Rxg6+ Bg7 Qg4 Rc7 Qh5 Ne7 Qxe5 Qxg6 Qxc7 Rxf3 exf3 Qg1+ Ke2 Qxa1 Qxe7 Qxb2+ Kf1 Qc1+ Kg2 Qb2 Qe8+",
 {
  "7.Nd5": "<div class=\"alts\"><span class=\"cap\">вместо Nd5</span><div class=\"alt\"><b>7.Bxb7?</b>7? Bxb7 8.Qxb7 Nbc6 (9.Ne4 Rb8 10.Qa6 Qd5!) 9.Nb5 Rb8 10.Qa6 Rb6 11.Qa4 Qb8 12.Na3 Rb4 with the initiative for a pawn White doesn't really want.</div></div>",
  "7...Nbc6": "<div class=\"alts\"><span class=\"cap\">вместо Nbc6</span><div class=\"alt\"><b>7…Be6</b>8.Qb5+ (8…Nec6 9.e4 with equal chances; Grob) Nbc6 '?' 9.Nxe7 (9…Bxe7) Qxe7 '?' 10.Bxc6+ bxc6 11.Qxc6+ <i>1-0 Bloodgood,C-Brenneman,M/Virginia 1973 (11)</i></div><div class=\"alt\"><b>7…Nxd5</b>8.Bxd5 Qc7 9.Nf3 (9…h6 10.Rg1 Nc6 11.d3 Bb4+ 12.Kd1 with an attack; Grob) Bd6 '?' 10.Ng5 O-O 11.Qd3 g6 12.Qh3 h5 13.Qd3 Kg7 14.gxh5 Bf5 15.Qf3 (15…Nc6) f6 '?' 16.Ne6+ <i>1-0 Bloodgood,C-Brogan,J/Virginia 1972 (16)</i></div></div>",
  "8.Nxe7": "<b>Nxe7!</b> — <div class=\"alts\"><span class=\"cap\">вместо Nxe7</span><div class=\"alt\"><b>8.d3!?</b>!? may be as good, but Na5! 9.Qa4+ Bd7 leaves much to be desired.</div></div>",
  "8...Qxe7": "<div class=\"alts\"><span class=\"cap\">вместо Qxe7</span><div class=\"alt\"><b>8…Bxe7</b></div></div>",
  "9.h3": "<div class=\"alts\"><span class=\"cap\">вместо h3</span><div class=\"alt\"><b>9.Qf3</b>f3 which offers White no more than equality.</div></div>",
  "10.a3": "<div class=\"alts\"><span class=\"cap\">вместо a3</span><div class=\"alt\"><b>10.e3!?</b>3!? which depends on Black errors.</div></div>",
  "11.Bd5": "' This position is not at all clear, but the maze of complications have been reduced to a managable level. '",
  "15...f5": "'!?'",
  "20.h5": "'!?'",
  "25...Ne7": "'the Black King needs a little room.'",
  "26...Qxg6": "'??'",
  "27...Rxf3": "'!?'",
  "33.Qe8+": "(Bloodgood- F. Monroe, 1973)"})

add("e2", C3, "Вариант E2", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 Nbc6 Nxd5 Nd4 Qc4 Nxd5 Bxd5 b5 Bxf7+ Ke7 Qd5 Nc2+ Kd1 Nxa1 Qxa8 Qc7 Qe4 Kxf7 f3 Be6 Qb1 Be7 Qxa1 Rc8",
 {
  "7.Nxd5": "<div class=\"alts\"><span class=\"cap\">вместо Nxd5</span><div class=\"alt\"><b>7.Nf3</b>f3 e4 8.Ng5 f6 9.d3 fxg5 10.Bxg5 Qb6 11.Qxb6 axb6 12.dxe4 dxe4 13.O-O-O Bxg4 14.Bxe4 Ra5 15.Be3 Nc8 16.Bd5 Bb4 17.Rhg1 Bxc3 18.Rxg4 Bf6 19.Re4+ Kf8 20.Be6 N8e7 21.b4! Ra8! 22.Bxb6 g5 23.b5 Ne5 24.f4 gxf4 25.Rxf4 Kg7 26.Rg1+ N7g6 27.h4 h5 28.Bd4 Rad8 (29.Bxe5! Bxe5 30.Rf7+ Kh6 31.Rxb7 with winning chances) 29.Kc2 Rd6 30.Bf5 Ng4! with a material advantage for Black. 31.Bxf6+ Rxf6 32.Rf3 Rxf5 33.Rxg4 Rxf3 34.Rxg6+ Kxg6 35.exf3 Ra8 36.Kb3 b6 <i>0-1 Sommerhalder,W-Grob,H/corr 1966 (36)</i></div><div class=\"alt\"><b>7.e3</b>e3 Be6! 8.Qxb7? Rb8 9.Qa6 Nb4 10.Qa4+ Bd7 11.Qd1 d4 12.exd4 exd4 13.Ne4 (13…d3? 14.Nd6#!) Qc7 14.Kf1 Bb5+ 15.d3 Nxd3 <i>0-1 Erwin,H-Stroemer, D/corr 1973 (15) with a winning advantage for Black.</i></div><div class=\"alt\"><b>7.h3!</b>3! (this solid move avoids all the complications of 7 Nxd5) (7…d4 8.Nd5 Na5 9.Qf3 Ng6 10.h4 Bd6 with an unclear position; Grob) Nd4 8.Qd1 (8…f5 9.e3 Ndc6 10.d4 ;Grob) a6 9.e3 Ndc6 10.d4 (10…exd4!) g6!? 11.dxe5 Nxe5 12.Nxd5 Bg7 13.Ne2 O-O 14.e4 b5 15.Bg5 f6 16.Be3 with a solid advantage for White.</div></div>",
  "7...Nd4": "<b>Nd4!</b> — <div class=\"alts\"><span class=\"cap\">вместо Nd4</span><div class=\"alt\"><b>7…Nxd5</b>8.Bxd5 Nd4 (9.Bxf7+? Ke7!) 9.Qc4 b5 transposes.</div></div>",
  "8...Nxd5": "<div class=\"alts\"><span class=\"cap\">вместо Nxd5</span><div class=\"alt\"><b>8…b5!?</b>9.Nc7+ Kd7 10.Nxb5 Ba6 11.a4 (11…Rc8 12.Qa2 Nc2+ 13.Kd1 Nxa1 14.Qxa1 Bxb5 15.axb5 Qc7 16.Qb1 with an unclear position; Grob) Qc8? 12.Qxc8+ Rxc8 13.Nxd4! exd4 14.b4 <i>1-0 Bloodgood,C-Sanderson,T/Virginia 1973 (14) with a winning advantage for white.</i></div></div>",
  "9...b5": "<div class=\"alts\"><span class=\"cap\">вместо b5</span><div class=\"alt\"><b>9…Be6</b>10.Bxe6 fxe6 11.Kf1! Rc8 12.Qd3 Qd5 13.Nf3 where Black has less than equality.</div></div>",
  "12.Kd1": "<div class=\"alts\"><span class=\"cap\">вместо Kd1</span><div class=\"alt\"><b>12.Kf1!?</b>1!? Nxa1 13.Qxa8 Qc7! with a winning advantage for Black.</div></div>",
  "13...Qc7": "<b>Qc7!</b>",
  "14.Qe4": "<b>Qe4!</b> — <div class=\"alts\"><span class=\"cap\">вместо Qe4</span><div class=\"alt\"><b>14.Bb3?</b>b3? Bb7! 15.Qxa7 Kd8 16.Nf3 Bc5 17.Ng5 Bxa7 18.Ne6+ Kd7 19.Nxc7 Bxh1 <i>0-1 Jordt-Saurmann/Stuttgart 1965 (19) with a winning advantage for Black.</i></div></div>",
  "14...Kxf7": "<div class=\"alts\"><span class=\"cap\">вместо Kxf7</span><div class=\"alt\"><b>14…Bb7?</b>15.Qf5 (15…Bxh1? 16.Qe6+ Kd8 17.Qe8#!) Bc8 16.Qb1 Kxf7 17.Nf3 Bxg4 18.Ng5+ with advantage for White; Grob</div></div>",
  "15.f3": "<div class=\"alts\"><span class=\"cap\">вместо f3</span><div class=\"alt\"><b>15.Nf3?</b>f3? Bb7! 16.Qf5+ Ke8 (17.Nxe5? Qc2+! 18.Qxc2 Nxc2 with a winning advantage for Black) 17.Qb1 Bxf3 18.exf3 Qc6! 19.Qe4 Qxe4 20.fxe4 Bc5 21.f3 Rf8 22.Rf1 Bd4! with a winning advantage for Black.</div><div class=\"alt\"><b>15.Qf5+</b>f5+</div><div class=\"alt\"><b>15.Qf3+</b>f3+ is good for equality, e.g. Ke8 16.Qc3</div></div>"})

add("e3", C3, "Вариант E3", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3 exd3 Bf4 dxe2 Ngxe2 Ng6 Bxd5 Qd7 Bg3 Nc6 O-O-O Bc5 Ne4 Bb6 Bxf7+",
 {
  "6...e4": "<b>e4!?</b> — While this line of play is very complicated, it is also probably Black's best.",
  "7...exd3": "<div class=\"alts\"><span class=\"cap\">вместо exd3</span><div class=\"alt\"><b>7…Nbc6</b>8.dxe4 Na5 9.Qb5+ Bd7 10.Qd3 dxe4 (11.Nxe4 Ng6 12.Bd2 Qb6 13.Qc3 Nc6 14.Be3 Qd8 15.O-O-O Rc8 16.Kb1 Nge5 17.Nf3 (with advantage for White; Grob-Unknown,Corr.) 11.Bxe4 Bc6 12.Nf3 Qxd3 13.Bxd3 Ng6 14.O-O h5 15.g5 Rd8 16.Bxg6 fxg6 17.Ne5 with advantage for White.</div></div>",
  "8.Bf4": "<b>Bf4!</b> — From the diagram position shown, the following are not good: — <div class=\"alts\"><span class=\"cap\">вместо Bf4</span><div class=\"alt\"><b>8.Nxd5</b>d5 Nxd5 9.Bxd5 Bb4+! <i>0-1 Grob, H-Bucher,R/corr 1966 (22) and White not only loses his attack, but also has the worse of the position. The text move is clearly best, and now Black can lose quickly with several seemingly playable moves, but also has several interesting and highly complex lines that are probably good.</i></div></div>",
  "8...dxe2": "<b>dxe2?</b> — <div class=\"alts\"><span class=\"cap\">вместо dxe2</span><div class=\"alt\"><b>8…d4?</b>9.Nb5 (9…Na6? 10.Nd6+ Kd7 11.Qb5+ Nc6 12.Qf5+ Ke7 13.Qxf7# Grob-O. Wisdemieer, Corr.) d2+ 10.Kf1 Be6 11.Qa4! (11…Bd7 12.Nd6#) Nec6 12.Nc7+ Kd7 13.Nxa8 <i>1-0 Grob,H-Sommerhalder,W/corr 1965 (13) with a winning advantage for White.</i></div><div class=\"alt\"><b>8…Nbc6?</b>(9.O-O-O Qb6 10.Nb5 Qc5+ 11.Kb1 Qc2+ 12.Qxc2 dxc2+ 13.Kxc2 Nb4+ 14.Kb1 Na6 <i>1-0 Beck-Bleisch/Zurich 1964 (29) favors White;</i>) 9.Nb5! (9…Qa5+ 10.Kf1 Ng6 11.Nc7+ Kd8 12.Bg3 with advantage for White) d2+ 10.Kf1 (10…Ng6) Na5? 11.Qa4 Ng6 12.Nc7+ Ke7 13.Nxd5+ Ke6 14.Bc7 Qd7 15.Qe4+ Ne5 16.Qxe5# <i>1-0 Grob,H-Wiedemeier/corr 1965 (16)</i></div><div class=\"alt\"><b>8…Na6!?</b>9.O-O-O (9…Nc5 10.Qb5+ Nc6 11.Nxd5 Qa5 12.Nc7+ with a winning advantage for White; Bloodgood-T. Sanderson, 1973) Ng6 10.Bxd5 (10…Nxf4 11.Qa4+! regaining the piece with an attack) Qf6 11.Be3 Bb4 12.Rxd3 Ne5 13.Rd4 Bc5 14.g5 Qf5 15.Rf4 Bxe3+ 16.fxe3 Qd7 17.Nf3 Nc5 18.Qc2 f6 19.gxf6 gxf6 20.Nxe5 fxe5 21.Bf7+ <i>1-0 Grob,H-Langemann,E/corr 1965 (21) with a winning advantage for White.</i></div></div>",
  "11...Nc6": "<div class=\"alts\"><span class=\"cap\">вместо Nc6</span><div class=\"alt\"><b>11…Bd6?</b>12.Bxd6 Qxd6 13.Bxf7+</div></div>",
  "12.O-O-O": "<div class=\"alts\"><span class=\"cap\">вместо O-O-O</span><div class=\"alt\"><b>12.Nb5</b>Nb5 Nge5!</div></div>",
  "13.Ne4": "with a solid advantage for White.",
  "14.Bxf7+": "(Grob- W. Kast, /corr 1965) The playable lines are: Variation \"E3a\" 8...Ng6!?; Variation \"E3b\" 8...a6; Variation \"E3c\" 8... d2+!?"})

add("e3a", C3, "Вариант E3a", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3 exd3 Bf4 Ng6 Bxd5 Nxf4 Qa4+ Nd7 Qxf4 Nf6 Bf3 d2+ Kf1 Qb6 Rd1 Qxb2 Qe3+ Be6 Rxd2",
 {
  "8...Ng6": "<b>Ng6!?</b> — This line is the weakest of the three for Black.",
  "10.Qa4+": "10. Bxf7 is not good.",
  "10...Nd7": "<div class=\"alts\"><span class=\"cap\">вместо Nd7</span><div class=\"alt\"><b>10…Qd7?</b>11.Qxf4 dxe2 12.Ngxe2 (12…Nc6 13.O-O-O! with a sharp attack) Bd6? 13.Bxf7+! <i>1/2-1/2 Grob,H-Huber/ corr 1966 (13) with a winning advantage for White.</i></div></div>",
  "12.Bf3": "<b>Bf3!</b> — <div class=\"alts\"><span class=\"cap\">вместо Bf3</span><div class=\"alt\"><b>12.Qe5+</b>e5+ Qe7 13.Qxe7+ Bxe7 14.g5 Nxd5 15.Nxd5 Bd8 16.e4 Be6 17.Nf3 Bxd5 18.exd5 Ba5+! <i>0-1 Grob,H-Frankenstein/corr 1965 (30) with some advantage for Black.</i></div></div>",
  "13...Qb6": "<div class=\"alts\"><span class=\"cap\">вместо Qb6</span><div class=\"alt\"><b>13…Bd6</b>14.Qxd2 O-O 15.g5 Ne8 16.Rd1 Qe7 17.Nb5 Bb8 18.Qd8 Qxd8 19.Rxd8 with a winning advantage forWhite.</div></div>",
  "15.Qe3+": "White hs the better of this, and possibly enough to discourage this line for Black altogether.",
  "16.Rxd2": "(Grob-W. Blatti, corr 1964) with a solid advantage for White."})

add("e3b", C3, "Вариант E3b", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3 exd3 Bf4 a6 Rd1 d4 Rxd3 Nbc6 e3 Ng6 Bxc6+ bxc6 Rxd4 Qa5 Re4+ Be6 Rxe6+ fxe6 Qxe6+ Ne7 Ne2 Rd8 Nd4 Qb6 O-O Qxb2 Ne4 Rxd4 exd4 Qxd4 Nd6+ Kd8 Nf7+ Ke8 Bc7 Qd7 Nd6+",
 {
  "6...e4": "<b>e4!?</b>",
  "8...a6": "This is safe, but offers Black no more than equality if he avoids the balance of the traps in his path.",
  "9.Rd1": "<div class=\"alts\"><span class=\"cap\">вместо Rd1</span><div class=\"alt\"><b>9.O-O-O</b>-O Nec6 10.Rxd3 d4 (11.h3!) 11.Bxb8 Nb4! 12.Rd2 Rxb8 13.Nf3 Be6 14.Qd1 (14…Qc8!) Qc7 15.Nxd4 <i>1-0 Grob,H-Sommerhalder,W/corr 1965 (49) with advantage in an error-filled game.</i></div><div class=\"alt\"><b>9.Nxd5</b>d5 Nxd5 10.Bxd5 Bb4+ (11.Qxb4 Qxd5 12.e4 Nc6! ; Grob) 11.Kf1! (11…dxe2+? 12.Nxe2 O-O 13.Rd1! Qe7 14.h3 favors White; Grob) O-O 12.Rd1 Qe7 13.Rxd3 Nc6 14.h3 <i>1-0 Bloodgood,C-Monroe,F/Virginia 1973 (14) with advantage for White.</i></div></div>",
  "9...d4": "<div class=\"alts\"><span class=\"cap\">вместо d4</span><div class=\"alt\"><b>9…dxe2?</b>10.Ngxe2 Nbc6 11.Bxd5 Nxd5 12.Nxd5 Na5? 13.Qe3+ Be6 14.Nc7+ Qxc7 15.Bxc7 <i>1-0 Grob,H-Fischer,W/corr 1966 (15) With a winning advantage for White.</i></div><div class=\"alt\"><b>9…Nbc6</b>10.Rxd3 Na5 11.Qd1 (11…Nc4 12.Bxd5 (12…Nxb2 13.Bc6+!) Nxd5 13.Rxd5 Qe7 14.Qa4+ b5 15.Rxb5 axb5 16.Qxa8 with a winning advantage for White.) Be6 (12.Bxd5 is also good.) 12.Nxd5 Nxd5 13.Bxd5 Bb4+ 14.Kf1 Bxd5 15.Rxd5 Qb6 16.Re5+ <i>1-0 Grob,H-Glauser,H/corr 1965 (35) with a solid advantage for White.</i></div></div>",
  "10...Nbc6": "White has a clear advantage, but Black may be able to gradually off-set this with good play.",
  "11.e3": "<div class=\"alts\"><span class=\"cap\">вместо e3</span><div class=\"alt\"><b>11.Bxc6+</b>c6+ Nxc6 12.Nf3 Bc5 with open play for both sides</div></div>",
  "11...Ng6": "<b>Ng6!</b> — <div class=\"alts\"><span class=\"cap\">вместо Ng6</span><div class=\"alt\"><b>11…h6</b>12.Nge2 Ng6 13.Bxc6+ bxc6 14.Rxd4 with advantage for White.</div></div>",
  "14...Be6": "<b>Be6!?</b> — <div class=\"alts\"><span class=\"cap\">вместо Be6</span><div class=\"alt\"><b>14…Be7?</b>15.Bd6!</div></div>",
  "15.Rxe6+": "<b>Rxe6+!</b>",
  "19...Qxb2": "<b>Qxb2?</b>",
  "25.Nd6+": "(Bloodgood-H. Erwin,1973)"})

add("e3c", C3, "Вариант E3c", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e5 c4 c6 cxd5 cxd5 Qb3 Ne7 Nc3 e4 d3 exd3 Bf4 d2+ Kf1 Nbc6 Bg3",
 {
  "6...e4": "<b>e4!?</b>",
  "8.Bf4": "<b>Bf4!</b>",
  "8...d2+": "<b>d2+!?</b> — This line of play has proven very double-edged, and may well be Black's best.",
  "9...Nbc6": "<div class=\"alts\"><span class=\"cap\">вместо Nbc6</span><div class=\"alt\"><b>9…Qb6?</b>10.Nb5 Na6 11.Nd6+ Kd7 12.Nxf7 Qxb3 13.axb3 Rg8 14.Bxd2 <i>1-0 Grob,H-Gubelmann/corr 1964 (14) With advantage for White.</i></div><div class=\"alt\"><b>9…Ng6</b>(10.Bg3 d4 This position is quite double edged! (11.Nb5 Na6 12.Bd5 Qd7 13.Nf3 Bc5 14.Qc4 O-O 15.Ng5 Nh8 16.b4 Bb6 17.Be4 Ng6 18.Bd6 <i>1-0 Bloodgood,C-McKenna,R/corr APCT 1973 (18) with a strong attack.</i>) 11.Bxb7 Bxb7? 12.Qxb7 dxc3 13.bxc3 d1=Q+ 14.Rxd1 Qxd1+ 15.Kg2 Qd7 16.Qxa8 Qc6+ 17.Qxc6+ Nxc6 18.Nf3 Bc5 19.Rd1 Ke7 <i>0-1 Stroemer, D-Bloodgood,C/Virginia 1973 (19) with a winning advantage for Black.</i>) 10.Bxd5 Nxf4 11.Qa4+ Nd7 12.Qxf4 Nf6 13.Bf3 Bd6 14.Qxd2 Nxg4 15.Bxg4 Bxg4 16.Rd1 Qe7 17.Nb5 <i>1-0 Bloodgood,C-Stroemer,D/Virginia 1973 (17) with some advantage for White.</i></div><div class=\"alt\"><b>9…d4?</b>10.Nb5 Na6 11.Nd6+ Kd7 12.Qb5+ Ke6 13.Qe5+ Kd7 14.Nxf7 With a winning advantage for White.</div></div>"})

add("a3", C4, "Вариант A3", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 e6 d3 Bc5 h4 Nc6 Nc3 Bd7 e4 d4 Nce2 e5 Ng3 Nge7 Nf5 Nxf5 gxf5 f6 Qh5+ Ke7 a3 Qe8 Qxe8+ Raxe8 h5 h6 Nf3 Reg8 Nh4 Be8 Bf3",
 {
  "1...d5": "After",
  "2.Bg2": ", Black has a number of playable alternatives which for the most part have not been examined in any detail. While Part 4 will serve s a general guide for play against several of these, it is by no means definitive. Variation A3 covers 2...e6 and Variation B3 covers other second moves for Black. — <div class=\"alts\"><span class=\"cap\">вместо Bg2</span><div class=\"alt\"><b>2.g5</b>g5 e5 3.h4 (3…h6!) Bc5 4.c3 (4…d4 5.Bg2 with good play) Nc6 5.b4 (5…Bb6 6.b5) Bd6 6.Bg2 Nge7 7.b5 Na5 8.d3 c6 9.a4 a6 10.bxa6 Rxa6 11.Qc2 Bf5 12.Nd2 Ng6 13.Nb3 Nxb3 14.Qxb3 Rb6 15.Qc2 Qe7 16.e3 h5 17.Ne2 <i>1/2-1/2 Grob,H-Schnirel/corr 1964 (17)</i> (17…O-O) Nxh4? 18.Rxh4 Qxg5 19.Ng3! Bxd3 20.Qxd3 Qxh4 21.Nf5 Qf6 22.Nxd6+ Qxd6 favors White.</div><div class=\"alt\"><b>2.h3!?</b>!? f5! 3.g5 e5 where Black can then play</div><div class=\"alt\"><b>2.f3?</b>3? e6 3.h4 Bd6 4.Rh3? Qxh4+! 5.Rxh4 Bg3#</div></div>",
  "2...e6": "This passive defense is tempting, and the aggressive player may well wish to attempt to break it open quickly, but it is not weak by any means and should be treated with respect.",
  "3.d3": "<div class=\"alts\"><span class=\"cap\">вместо d3</span><div class=\"alt\"><b>3.c4!?</b>!? dxc4 (4.Qa4+!) 4.b3? (4…Qd4! 5.Nc3 Qxg4) cxb3? 5.Qxb3 c6 6.Bb2 f6 7.d4 Qb6 8.Qc2 Bb4+ 9.Nd2 Ne7 10.a3 Bxd2+ 11.Qxd2 c5 12.dxc5 Qxc5 13.Rc1 Qb6 14.g5 O-O 15.gxf6 gxf6 16.Nh3 e5 17.Rg1 Ng6 18.Be4 (18…Bxh3? 19.Qh6 f5 20.Bd5+ With a mating attack) Kg7 19.Bxg6 hxg6 20.Qd3 with a winning attack. Kf7 21.Qxg6+ Ke7 22.Bxe5 Bxh3 23.Bc3 Nc6 24.Qh7+ Rf7 25.Qxh3 Rd8 26.Rg3 Rd7 27.Re3+ Ne5 28.Bxe5 fxe5 29.Rxe5+ Kf6 30.Rf5+ <i>1-0 Grob,H-Kurz/corr 1965 (30)</i></div></div>",
  "3...Bc5": "<div class=\"alts\"><span class=\"cap\">вместо Bc5</span><div class=\"alt\"><b>3…b6</b>4.c4 c6 5.Qa4 Bd7 6.Nc3 <i>1/2-1/2 Bloodgood,C-Bowlby,R/corr 1973 (6) with an unclear position.</i></div><div class=\"alt\"><b>3…Be7</b>4.Nf3 (4…h5 5.g5!?) c6 5.Nc3 Qb6 6.e4 d4 7.Ne2 c5 8.Ne5 Nc6 9.Nxc6 bxc6 10.b3 e5 11.h3 (11…Bd7 was better; Grob) Be6 12.O-O h6 13.f4 Bd6 14.f5 Bd7 15.Ng3 g5 16.fxg6 fxg6 17.Bd2 a5 18.a4! O-O-O 19.Qe1 winning the a-pawn and leaving Black facing the inevitable Queenside pawn onslaught.</div></div>",
  "5.Nc3": "White's king's side pressure is obvious, and must be countered. To allow White a free hand on the king's side invites disaster.",
  "5...Bd7": "<b>Bd7!?</b> — <div class=\"alts\"><span class=\"cap\">вместо Bd7</span><div class=\"alt\"><b>5…Nge7</b>6.e4 (6…d4!) dxe4? 7.Nxe4 Bb6 8.Nh3 Ng6 9.Nf4 (9…Nxf4!) e5? 10.Nh5 Nxh4? 11.Nxg7+ Kf8 12.Bh6 Nxg2+ 13.Kf1 Kg8 Queen moves lose 14.Kxg2 Qd5 15.Qf3 Qd8 16.Nf6+ Kf8 17.Ne6+ <i>1-0 Bloodgood,C-Leonard,F/Virginia 1973 (17) Black resigned.</i></div></div>",
  "17.Bf3": "(H. Grob-Weidemeier, corr, 1965) with mounting pressure."})

add("b3", C4, "Вариант B3", "÷", "÷ по Бладгуду",
 "g4 d5 Bg2 b5 e4 dxe4 Bxe4 c6 h3 Nf6 Bg2 Be6 Nc3 b4 Ne4 Nxe4 Bxe4 Bd5 Qf3 e5 d3 Nd7 Bxd5 cxd5 Qxd5",
 {
  "2...b5": "Of the remaining alternative for Black at move two, this is the line with the most possibilities. Others are playable. — <div class=\"alts\"><span class=\"cap\">вместо b5</span><div class=\"alt\"><b>2…Nc6</b>3.c4! (3…dxc4 4.Bxc6+! leaving Black with tripled isolated pawns) e6 (4.d3 Bb4+ 5.Bd2 Bxd2+ 6.Qxd2 Nge7 7.Na3 Ng6 8.Nf3 with an unclear position; H. Grob) 4.Qb3!? (4…d4) Na5!? 5.Qa4+ c6 6.cxd5 exd5 7.Nc3 (7…Bxg4 8.Nxd5!) Be6 8.d4 Bd6 9.g5 Ne7 10.h4 Ng6 11.b4 Nc4 12.b5 Qb6 13.bxc6 bxc6 14.Nxd5!? Qxd4 15.Qxc6+ Kd8 16.Qxa8+ Kd7 17.Qb7+ Kd8 18.Rb1 <i>1-0 Bloodgood,C-Waymire,W/Norfolk 1960 (18) Black resigned.</i></div><div class=\"alt\"><b>2…c5</b>(3.c4 d4 4.d3 (4…e5 5.g5 Be7 6.h4 Nd7 7.e4 Bd6 8.Ne2 Ne7 9.Nd2 O-O 10.Ng3 Nb6 11.b3 Nc6 12.Nf5 Bxf5 13.exf5 f6 14.Be4! fxg5 15.hxg5 Qxg5 16.Nf3 with a winning attack; H. Grob-Unknown) Nc6 5.g5 e5 (6.Nf3 b5 7.cxb5 Qa5+ 8.Nfd2 Qxb5 9.Nb3 Rb8 10.f3 Qa6 11.Kf2 with an unclear position.) 6.h4 h5 7.Nd2 Nge7 8.Ne4 Ng6 9.Bh3 Bxh3 10.Rxh3 Be7 11.Nf3 b5 12.cxb5 Qa5+ 13.Nfd2 Qxb5 14.Nc4 Rd8 15.f3 Qa6 16.Kf2 <i>1/2-1/2 Grob, H-Sutton/corr 1966 (16)</i>) 3.g5 e5 4.d3 Nc6 5.Nc3 Be6 6.h4 f6 7.e4 d4 8.Nce2 Qd7 9.f4 Bg4 10.f5 g6 11.Bh3 gxf5 12.Bxg4 fxg4 13.Ng3 h5 14.gxh6 Bxh6 15.N1e2 Bxc1 16.Nxc1 Nce7 17.Nb3 b6 18.Qe2 Ng6 19.Nf5 Nh6 20.Nxh6 Rxh6 21.Qf2 Nf4 22.O-O-O (22…O-O-O!) Rb8? 23.Kb1 f5 24.exf5 Qxf5 25.Nd2 Kd7 26.Rde1 b5 27.Re4 Rh7 28.Rhe1 Re7 29.Nb3 Kd6 30.c3 Rf8 31.Rf1 Rg7 32.cxd4 cxd4 33.Qd2 Rff7 34.Qb4+ <i>1-0 Grob,H-Wampfler/corr 1964 (34) With a winning position.</i></div><div class=\"alt\"><b>2…Nf6?</b>3.g5 Ne4 4.d3 (4…Nc5) Nxf2? 5.Kxf2 e5 6.c3 c6 7.h4 and Black has no compensation for the Knight. Bf5 8.Nf3 Nd7 9.h5 Be7 10.Qc2 h6 11.e4 dxe4 12.dxe4 Be6 13.gxh6 gxh6 14.Be3 b6 15.Nbd2 Rg8 16.Bh3 Bxh3 17.Rxh3 Qc7 18.Bxh6 Nf6 19.Nh2 Qd7 20.Qd3 <i>1-0 Grob, H-Minder/corr 1965 (20)</i></div><div class=\"alt\"><b>2…Na6!?</b>3.c4 e6 4.cxd5 exd5 (5.h3 is safer) 5.Qb3!? Be6! (6.d4!) 6.Qxb7? Nb4 7.Na3 a6 8.d4 Rb8 9.Qa7 Qc8 <i>0-1 Bloodgood,C-Haack,S/corr 1975 (9) and the White Queen is trapped.</i></div><div class=\"alt\"><b>2…Nd7</b>3.d3 (3…e5 4.e4 Bc5 5.g5 dxe4 6.dxe4 c6 7.Nf3 Qc7 8.Nc3 Nb6 9.Nh4 Ne7 10.Qf3 Be6 11.Bh3 with an awkward endgame for Black; H. Grob) e6 4.e4 c6 5.Nc3 Nb6 6.h4 Bb4 7.Bd2 a5 8.Qe2 Ne7 9.f4 d4 10.Nd1 Bxd2+ 11.Qxd2 Ng6 12.h5 Nh4 13.Nf3 Nxf3+ 14.Bxf3 e5 15.g5 f6!? 16.gxf6 Qxf6 17.f5 h6 18.Nf2 Bd7 19.Ng4 Qd6 20.O-O-O and White has a solid advantage.</div></div>",
  "10...e5": "<div class=\"alts\"><span class=\"cap\">вместо e5</span><div class=\"alt\"><b>10…Bxe4</b>11.Qxe4 Qd5</div></div>",
  "11...Nd7": "<b>Nd7?</b> — <div class=\"alts\"><span class=\"cap\">вместо Nd7</span><div class=\"alt\"><b>11…Be7</b>with equality</div></div>",
  "13.Qxd5": "with advantage to White. H. Grob-G. Pinter, corr."})

add("a4", C5, "Вариант A4", "÷", "÷ по Бладгуду",
 "g4 e5 Bg2 h5 gxh5 Rxh5 e3 Rh8 c4 f5 Qc2 g6 Nc3 c6 Nge2 Nf6 d4 d6 Bd2 Be6 d5 cxd5 cxd5 Bf7 Qa4+ Nbd7 Rc1 a6 Ng3 Be7 O-O b5 Qb3 Nc5 Qc2 e4 f3 exf3 Bxf3 b4 Na4 Rb8 Nxc5 dxc5 Qa4+ Qd7 Qxa6 Bxd5 e4 Bc6 Be2 Ra8 Qb6 fxe4 Be3 Nd5",
 {
  "2.Bg2": "While 2 Bg2 d5 transposes to Part III, this defence generally brings about a radical difference in the basic motifs of attack. Several lines not recommended for White include: — <div class=\"alts\"><span class=\"cap\">вместо Bg2</span><div class=\"alt\"><b>2.c4?</b>4? h5! (3.d3) 3.d4? hxg4 4.dxe5 Nc6 5.Qd5 Rh5! 6.f4 Qh4+ 7.Kd1 d6 8.e4 dxe5 9.f5 Nf6 10.Qd3 Bxf5 11.exf5 Rd8 12.Qxd8+ Kxd8 13.Bd3 e4 <i>0-1 Schraner-Grob,H/corr 1964 (13) White resigned.</i></div><div class=\"alt\"><b>2.e4?</b>4? d5! (3.Bg2 Nf6!) 3.Qf3 dxe4 4.Qxe4 Bd6 5.h3 Nc6 6.c3 f5 (7.gxf5 Qf6) 7.Qe2 Qe7 8.d3 g6 9.g5 Bd7 10.Bg2 O-O-O 11.h4 Qf7 12.Qf3 Re8 13.Nd2 Nd8 14.Ne2 Bc6 15.Qh3 Kb8 16.Nc4 Ne7 <i>1/2-1/2 Schraner-Grob,H/corr 1963 (16) with advantage to Black.</i></div><div class=\"alt\"><b>2.d4!?</b>!? e4? 3.c4 Qh4 4.h3 Bb4+ 5.Nc3 Bxc3+ 6.bxc3 Qe7 7.Bf4 d6 8.e3 g5 9.Bg3 Be6 10.Rb1 Bc8 The second tempo lost in this game! 11.Be2 Nf6 12.h4 gxh4 13.Bxh4 Qe6 14.g5 Nfd7 15.Nh3 (15…Nb6!) Rg8? 16.Nf4 Qe7 17.Nd5 Qd8 18.g6 f6 19.gxh7 <i>1-0 Grob,H-Rothschild,W/corr 1964 (19) Black resigned.</i></div></div>",
  "2...h5": "<div class=\"alts\"><span class=\"cap\">вместо h5</span><div class=\"alt\"><b>2…Bc5</b>(3.h3 Qh4 4.e3 Nf6? 5.d4 exd4? 6.exd4 Bd6 7.Nf3 <i>1-0 Bloodgood,C-Mizesko,H/IPC CM-6 1975 (7) and the Black Queen falls;</i>) 3.e3 Nc6 (4.Nc3 d6 5.Na4 Bb6 6.Nxb6 axb6 7.h3 Nge7 8.d4 exd4 9.exd4 d5! 10.a3 O-O 11.Nf3 Ng6 12.O-O Nce7 with equality; H. Grob) 4.c3 d5 5.d4 exd4 6.exd4 Qe7+ 7.Be3 Bb6 8.g5 f6 9.h4 f5 10.Nh3 Be6 11.Nf4 O-O-O 12.Nd2 h6? 13.Ng6 <i>1-0 Bloodgood,C-Christy,R/Virginia 1972 (13) Black Resigned.</i></div><div class=\"alt\"><b>2…Nc6</b>3.c4 (3…Nge7 4.Nc3 Ng6 5.h3 Bc5 6.d3 b6 7.Nf3 Bb7 8.e3 Nce7 9.e4!? (9…c6 followed by) Nf4? 10.Bxf4 exf4 11.a3 Ng6 12.Qd2 c6 13.d4 Be7 14.Ne2 d5 15.cxd5 Qd6!? 16.dxc6 Bxc6 17.e5 Qe6 18.Rc1 (18…Rd8!) Rc8? 19.d5 <i>1-0 Grob,H-Mosiman/corr 1964 (19) and White wins a piece.</i>) (3…d6 4.h3 (4…Nge7 5.d3 Ng6 6.Nf3 Be7 7.Nc3 O-O 8.g5 f6 9.Nd5 fxg5 10.Nxe7+ Qxe7 11.Bxg5 Qf7 12.Be3 Nf4 13.Bf1 Qh5 14.Qd2 Bf5 15.O-O-O Nxd3+? Simply an unsound combination; Black had equality before this move. 16.exd3 Qxf3? 17.Be2 Qg2 18.Rdg1 <i>1-0 Grob,H-Henneberger,W/corr 1964 (18) and the Queen is trapped.</i>) Nf6 5.d3 Be7 6.Nc3 O-O 7.Nf3 Re8 8.e4 Bf8 9.Be3 Ne7 10.g5 Nd7 11.h4 f5 12.exf5 Nxf5 13.Ne2 h6 14.Ng3 Nxe3 15.fxe3 c6 16.g6 Qe7 17.Ne4 Qe6 18.Neg5 Qe7 19.Ne4 <i>1/2-1/2 Grob,H-Henneberger,W/corr 1942 (19) Drawn.</i>) Bc5 4.e3 d6 5.a3 (5…Nge7? 6.b4 Bb6 7.Bb2 Ng6 8.Be4 Qg5 9.h3 f5 10.Nf3 Qf6 11.g5 Qe7 12.Bxc6+ bxc6 13.h4 e4 14.h5 Nf8 15.h6 Ne6 16.hxg7 Nxg7 17.Bf6 Qf7 18.Nh4 Be6 19.c5 Bb3 20.Qc1 dxc5 21.Qc3 c4 22.Bxg7 O-O-O 23.Qf6 <i>1-0 Grob, H-Rognon/corr 1964 (23) Black resigned.</i>) a5 6.Nc3 Bd7 7.h3 Nge7 8.Nge2 O-O 9.d4 exd4 10.exd4 Ba7 11.Be3 Ng6 (12.Ng3 Nh4 13.Be4 f5 14.gxf5 Nxf5 15.Nxf5 Bxf5 16.Qd3 with equality; Grob) 12.Qd2 Qc8 13.O-O-O (13…f5 with counterplay) Nce7 14.Ng3 <i>1/2-1/2 Grob,H-Ruegg/corr 1965 (14) favors White.</i></div></div>",
  "4...Rh8": "<b>Rh8!</b> — <div class=\"alts\"><span class=\"cap\">вместо Rh8</span><div class=\"alt\"><b>4…Nf6</b>5.c4 c6 6.Nc3 d5! 7.cxd5 Rg5 8.Bf3 cxd5 9.Qa4+ Nc6 10.d3 Rg6 11.e4 d4 12.Nd5 Be6 13.Qb5 Qd7 14.Bd2 Bxd5 15.exd5 Nb4 16.Qxd7+ Kxd7 17.Bxb4 Bxb4+ 18.Kd1 <i>1/2-1/2 Hug,P-Grob,H/corr 1964 (18)</i> (18…Bd6 with equality) Kd6!? 19.Ne2 Nxd5? 20.Ng3 Rd8 21.Bh5! Rf6 22.Ne4+ with a material advantage.</div></div>",
  "5...f5": "<div class=\"alts\"><span class=\"cap\">вместо f5</span><div class=\"alt\"><b>5…c6</b>6.Nc3 Bb4 7.Nge2 Qg5 8.Ng3 f5 9.d4 Bxc3+ 10.bxc3 f4 11.exf4 exf4 12.Qe2+ Ne7 13.Qf3 Ng6 14.Ne4 Qe7 15.d5 Ne5 16.Qe2 d6 17.Bxf4 Bf5 18.Nxd6+ Qxd6 19.Bxe5 Qe7 20.Bxb8 Rxb8 21.Qxe7+ Kxe7 22.a4 Bd3 23.Bf1 Be4 24.Rg1 g6 25.Bg2 Bd3 26.c5 cxd5 27.Bxd5 Rxh2 28.O-O-O Bf5 29.Rg2 Rxg2 30.Bxg2 g5 31.Rd5 Bd7 32.Rxg5 Bxa4 33.Rg7+ Kf6 34.Rxb7 Rxb7 35.Bxb7 <i>1-0 Bloodgood,C-Monroe,F/Virginia 1973 (35) and White won in 53 moves.</i></div></div>",
  "24.Qxa6": "<b>Qxa6!?</b> — <div class=\"alts\"><span class=\"cap\">вместо Qxa6</span><div class=\"alt\"><b>24.Qxd7+</b>d7+ with equality.</div></div>",
  "28...Nd5": "R. Ott-H. Grob, corr,1965 with the White Queen trapped."})

add("a5", C6, "Вариант A5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 h6 e4 Nc6 Nc3 Nge7 h4 d5 Bg2 d4 Nd5 Be6 g5 hxg5 hxg5 Rxh1 Bxh1 Ng6 Qh5 Nf4 Nxf4 exf4 Bxf4 Qd7 Nf3 O-O-O Ne5 Nxe5 Bxe5 Bd6 Bxg7 Bg4 Qh6 Bf4 Bf6 Rg8 f3 Be6 Ke2",
 {
  "2...h6": "<div class=\"alts\"><span class=\"cap\">вместо h6</span><div class=\"alt\"><b>2…g6</b>Grob-P. Weiland, corr., continued 3.e4 h6 4.Nc3 Bg7 5.Be3 c6 6.Bg2 Ne7 7.h3 d5 8.Bc5 d4 9.Nce2 Be6 10.Qd2 b6 11.Bxe7 Qxe7 12.Ng3 Nd7 13.a3 Rc8 14.N1e2 c5 15.O-O <i>1/2-1/2 Grob,H-Wieland/corr 1964 (15)</i></div></div>",
  "3.e4": "<div class=\"alts\"><span class=\"cap\">вместо e4</span><div class=\"alt\"><b>3.h4</b>h4 d5 (4.e4!?) 4.e3 Nf6 5.Be2 a6 6.Nd2 Nc6 7.Nf1 Bc5 8.Ng3 Be6 9.f4 exf4 10.exf4 (10…d4!) Be7!? 11.c3 d4 12.c4! <i>1-0 Grob,H-Steinbruchel/corr 1965 (26) with advantage to White.</i></div><div class=\"alt\"><b>3.Bg2</b>g2 Nf6 4.h3 c6 5.e4 d5 6.Nd2 d4 7.Nc4 Nbd7 8.Nf3 Qc7 9.Nh4 (9…b5!) g6?! 10.g5! hxg5 11.Bxg5 Nh5 12.Qf3 Nf4!? 13.Bxf4 exf4 14.Qxf4 <i>0-1 Bloodgood,C-Sanderson,T/Virginia 1973 (14) with advantage to Black.</i></div></div>",
  "4.Nc3": "<div class=\"alts\"><span class=\"cap\">вместо Nc3</span><div class=\"alt\"><b>4.h4</b>h4 d5 5.Bg2 d4 (6.Nd2 may be better) 6.g5!? hxg5 7.hxg5 Rxh1 8.Bxh1 (8…Nge7 with) f6? 9.Qh5+ (9…Ke7 10.Qh7!) Kd7 10.Qf7+ Nge7 11.gxf6 gxf6 12.Qxf6 <i>1-0 Bloodgood,C-Leonard,F/Virginia 1973 (12) with a winning advantage to White.</i></div></div>",
  "4...Nge7": "<div class=\"alts\"><span class=\"cap\">вместо Nge7</span><div class=\"alt\"><b>4…Nf6</b>(5.Bg2 Bc5 6.h4 d5!? 7.g5! hxg5 8.hxg5 Rxh1 9.Bxh1 Ng4! 10.Nh3 d4 11.Nd5 Be6 12.f4! exf4 13.Bxf4 Bd6 14.Qf3 Nge5 15.Qh5 <i>1-0 Bloodgood,C-Sarkis,A/ Virginia 1973 (15) with advantage to White.</i>) 5.h4 d5 6.Bg2 d4 7.Nd5 Nxg4! <i>0-1 Bloodgood,C-Sarkis,A/Virginia 1973 (7) with advantage to Black.</i></div></div>",
  "5.h4": "<div class=\"alts\"><span class=\"cap\">вместо h4</span><div class=\"alt\"><b>5.Bg2</b>g2 Ng6 6.Nf3 d6 7.h3 Be7 8.Be3 with Black quite cramped; Grob.</div></div>",
  "5...d5": "<div class=\"alts\"><span class=\"cap\">вместо d5</span><div class=\"alt\"><b>5…g6</b>6.Bg2 Nd4 7.f4 d6 8.Be3 Nec6 9.Nd5 at which point Black played Bxg4? <i>1-0 Grob,H-Hoffmann/corr 1964 (9) but White already had a considerable advantage.</i></div></div>",
  "11...Nf4": "<b>Nf4?</b> — <div class=\"alts\"><span class=\"cap\">вместо Nf4</span><div class=\"alt\"><b>11…Qd7</b>followed by</div></div>",
  "16...Bd6": "<b>Bd6?</b> — <div class=\"alts\"><span class=\"cap\">вместо Bd6</span><div class=\"alt\"><b>16…Bg4!</b></div></div>",
  "17.Bxg7": "<b>Bxg7!</b> — <div class=\"alts\"><span class=\"cap\">вместо Bxg7</span><div class=\"alt\"><b>17.Bxd6</b>xd6 Qxd6 with Black simply trading</div></div>",
  "21.Ke2": "Bloodgood-R. Christy, 1972 with a winning advantage."})

add("b5", C6, "Вариант B5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 h5 g5 h4 Bh3 d6 Bxc8 Qxc8 h3",
 {
  "2.d3": "<b>d3!</b>",
  "2...h5": "This line of play lacks sting! White should get an advantage with proper play.",
  "3...h4": "<div class=\"alts\"><span class=\"cap\">вместо h4</span><div class=\"alt\"><b>3…Be7</b>4.h4 d5 5.Bg2 Bg4 6.Nd2 c6 7.Ngf3 Nd7 8.e4 d4 9.Bh3 Bxh3 10.Rxh3 (10…Qc7) f6!? 11.Nc4 b5 12.gxf6 (12…gxf6) Bxf6? 13.Nd6+ Ke7 14.Nf5+ Kf7 15.Ng5+ Bxg5 16.Bxg5 Qc7 17.Qf3 Ngf6 18.O-O-O Raf8 19.Rg3! (19…Rh7) Kg8? 20.Nxg7! Ng4 21.Nf5 <i>1-0 Bloodgood,C-Cacalano,A/Norfolk 1961 (21) with a winning advantage to White.</i></div></div>",
  "4.Bh3": "<div class=\"alts\"><span class=\"cap\">вместо Bh3</span><div class=\"alt\"><b>4.f4</b>f4 exf4 5.Bxf4 d5 6.Bg2 c6 7.e4 Be6 8.Nc3 d4 9.Nce2 Be7 10.Qd2 h3! 11.Bf1 Bg4! <i>0-1 Bloodgood,C-Lewis,R/Norfolk 1960 (11) with strong advantage to Black.</i></div></div>",
  "6.h3": "White has the better of this in several ways. First, the Black KRP is a problem for the second player to defend. Add to this the delays Black faces in developing his King-side because of the \"Spike\" pawn while White can free his pieces easily."})

add("c5", C6, "Вариант C5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 Nc6 c4 d6 e4 h6 Nc3 Nge7 h4 Ng6 Bh3 Nf4 Be3 Nb4 Bxf4 exf4 Qa4+ Nc6 Nf3 Bd7 Qb3 b6 O-O-O Be7 Nd5 Be6 Qb5 Bd7 g5 Bxh3 Rxh3 Qd7 Nxe7 Nxe7 Qxd7+ Kxd7 Re1 Ng6 h5 Ne7 Rh4 Raf8 Rxf4 hxg5 Nxg5 f6 Nf3 g6 h6 g5 Rg4 Ng6 Kd2 Rf7 Nd4 Rfh7 Nf5 Ne5 Rg3 Nf7 Rh3 c5 a4",
 {
  "2...Nc6": "This seemingly logical development does little to counter-act White's basic King-side threats.",
  "3...d6": "<div class=\"alts\"><span class=\"cap\">вместо d6</span><div class=\"alt\"><b>3…d5!?</b>(4.cxd5 Qxd5!) 4.Bg2! dxc4 5.Bxc6+ bxc6 6.Qa4!</div></div>",
  "4...h6": "<div class=\"alts\"><span class=\"cap\">вместо h6</span><div class=\"alt\"><b>4…g5?</b>5.Be3 Nh6 6.f3 Nd4 7.Nc3 c6 8.Qd2 f6 9.h4 Nf7 10.Bxd4 exd4 11.Nce2 c5 12.hxg5 fxg5 13.Ng3 Bg7 14.O-O-O with advantage to White.</div></div>",
  "7.Bh3": "Black is virtually committed to exchanging his King-Knight, after which White has a strong attack on the King-side.",
  "33.a4": "Bloodgood-D. Stroemer, 1972 (16 g5 and 18 Nxe7!? are suspect!)"})

add("d5", C6, "Вариант D5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 Be7 Nf3 d6 h3 f5 g5 f4 h4 Bg4 Nbd2 h6 Bg2 hxg5 hxg5 Rxh1+ Bxh1 Nc6 Ne4 Bxf3 Bxf3 Bxg5 Bh5+ Kd7 e3 Bh6 Qg4+ Ke7 exf4 Nd4 fxe5 Nxc2+ Kd1 Nxa1 Bxh6 gxh6 Qg7+",
 {
  "2.d3": "<b>d3!</b>",
  "2...Be7": "This counters the threat of g5 very effectively, and although this line has not been explored in any detail, the potential is definitely there.",
  "3.Nf3": "<div class=\"alts\"><span class=\"cap\">вместо Nf3</span><div class=\"alt\"><b>3.e4</b>e4 d5 4.Qe2 d4 5.h3 Bg5 6.Nd2 Be6 7.Ngf3 Bf4 8.Nb3 Bxc1 9.Nxc1 Qd6 10.Qd2 Nd7 11.Ne2 Ne7 12.a3 <i>1/2-1/2 Grob, H-Bruckmann/corr 1965 (12) with advantage to Black.</i></div></div>",
  "4.h3": "<div class=\"alts\"><span class=\"cap\">вместо h3</span><div class=\"alt\"><b>4.g5?</b>5? h6!</div></div>",
  "4...f5": "<div class=\"alts\"><span class=\"cap\">вместо f5</span><div class=\"alt\"><b>4…h5</b>, when 5.g5! creates some problems.</div></div>",
  "5.g5": "The position is certainly far from clear, but it is equally apparent that Black will encounter some difficulty on the King-side.",
  "10...Nc6": "<b>Nc6!?</b> — <div class=\"alts\"><span class=\"cap\">вместо Nc6</span><div class=\"alt\"><b>10…Bxg5!</b>11.Nxg5 Qxg5 12.Ne4 Qh5 13.Kd2 Nc6 with advantage to Black.</div></div>",
  "20.Qg7+": "Bloodgood-H. Fuller, 1973 Black resigned"})

add("e5", C6, "Вариант E5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 Bc5 h4 d5 g5 Bg4 c4 Ne7 Bg2 Be6 Qb3 Bb6 Nc3 dxc4 Qb5+ Nbc6 dxc4 a6 Qa4 O-O Bh3 Bxh3 Nxh3 f5 c5 Ba7 Qc4+ Kh8 h5 Nd4 Nd1 Qe8 h6 g6 f4 Rd8 fxe5 Nec6 Nf4 Nb4 e6 Nbc2+ Kf2 Nxa1 e3 Nc6 Qc3+ Nd4 exd4 Qe7 d5+ Kg8 Be3 b6 Nxg6 hxg6 h7+",
 {
  "1...e5": "<div class=\"alts\"><span class=\"cap\">вместо e5</span><div class=\"alt\"><b>1…e6</b>2.d4 d5 3.Nf3 Nf6 4.Rg1 h6 5.h4 Nc6 6.c3 Be7 7.g5 hxg5 8.hxg5 Ne4 9.g6 f6 10.Nbd2 f5 11.Nxe4 fxe4 12.Ne5 Nxe5 13.dxe5 Rh5 14.Bf4 Bg5 15.e3 Bxf4 16.Qxh5 <i>1-0 Grob,H-Schaufelberger,H/corr 1964 (16)</i></div></div>",
  "2...Bc5": "This is Black's most aggressive reply and must be treated with respect. Several lines of play are good for White at this point.",
  "3.h4": "<div class=\"alts\"><span class=\"cap\">вместо h4</span><div class=\"alt\"><b>3.e3</b>e3 d5 4.Bg2 Be6 5.h4 (5…c6!) Nc6 6.Nd2 Nge7 7.c4 (7…O-O) dxc4!? 8.dxc4 Qd3 9.Be4 Qd7 10.g5 O-O-O 11.a3 a6 12.Qa4 Nb8 13.Qc2 Ng6 14.b4 Be7 15.Bb2 h6 16.Ngf3 hxg5 17.h5 Nh4 18.Nxe5 Qd6? 19.c5 <i>1-0 Bloodgood,C-Coakley,R/ Virginia 1973 (19) Black resigned.</i></div><div class=\"alt\"><b>3.Nf3</b>f3 Nc6 4.e4 Nf6 5.g5 Ng4 6.d4 (6…Nxd4? 7.Nxd4 with the N at g4 hanging) exd4 7.h3 Nge5 8.Nxe5 Nxe5 9.f4 Nc6 10.Bg2 with ample compensation for the pawn.</div><div class=\"alt\"><b>3.e3</b>e3 d5 4.Bg2 after which: Grob-H. Schaufelberger, corr., continued (4…f5? 5.gxf5 Bxf5 6.Qf3 Ne7 7.Qh5+ g6 8.Qh6 with a tactical finish; Grob) Ne7 5.c4 (5…dxc4 6.Qa4+ and 7 Qxc4 next) O-O 6.cxd5 Nxd5 7.a3 c6 8.h4 f5 9.g5 f4 10.e4 Nc7 11.Nf3 Qd6 12.Qc2 Nd7 13.Nbd2 b5 14.b4 Bb6 15.Bb2 and White has the initiative.</div></div>",
  "4.g5": "<div class=\"alts\"><span class=\"cap\">вместо g5</span><div class=\"alt\"><b>4.e3</b>e3 f5 5.gxf5 Bxf5 6.Qh5+ g6 7.Qe2 Nc6 8.a3 Qd7 9.b4 Be7 10.Bb2 a6 11.Nd2 Nf6 <i>1-0 Grob, H-Debrunner/corr 1965 (38) with a sharp position that is very double-edged.</i></div></div>",
  "5.c4": "<b>c4!</b>",
  "5...Ne7": "<div class=\"alts\"><span class=\"cap\">вместо Ne7</span><div class=\"alt\"><b>5…dxc4</b>6.Qa4+ Bd7 7.Qxc4 Bb6 8.Bg2 Bc6 9.Nf3 Nd7 10.Bd2 Ne7 11.Bc3 Ng6 12.Qg4 Qe7 13.h5 Bxf3 14.Bxf3 Nf4 15.Bxb7 Rd8 16.Bc6 O-O!? 17.Bxd7 (17…Rxd7!) Qxd7 18.Qxd7 Rxd7 19.Bxe5 Ne6 20.f4 f6 21.gxf6 gxf6 22.Rg1+ Kf7 23.Bc3 Nxf4 24.h6 Rg8 25.Rxg8 Kxg8 26.Bxf6 Kf7 27.Bg5 Ne6 28.Bd2 Nd4 29.Kd1 Re7 30.Nc3 Ba5 31.Ne4 Bxd2 32.Kxd2 a5 33.Rg1 Kf8 34.Rg5 a4 35.Ra5 a3 36.Rxa3 Re6 37.Ra8+ Ke7 38.Ng3 Rg6 39.Rh8 Rxg3 40.Rxh7+ Kd6 41.Rh8 Rh3 42.h7 Kc5 43.b4+ Kc6 44.Rd8 <i>1-0 Bloodgood, C-Monroe,F/Virginia 1973 (44) Black resigned.</i></div></div>",
  "7...Bb6": "White clearly has the initiative, but there are complications.",
  "8...dxc4": "<b>dxc4?</b>",
  "21...Nb4": "<b>Nb4!?</b> — <div class=\"alts\"><span class=\"cap\">вместо Nb4</span><div class=\"alt\"><b>21…Nxe5!?</b></div></div>",
  "30.h7+": "Bloodgood- T. Sanderson, 1973 Black resigned."})

add("f5", C6, "Вариант F5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 d6 e4 Nc6 h3 g6 Bg2 h5 g5 Nge7 Nc3 Be6 Nd5 Bg7 c3",
 {
  "2...d6": "This passive line should offer White no problems. Grob suggests:",
  "9.c3": "with White standing better.."})

add("g5", C6, "Вариант G5", "÷", "÷ по Бладгуду",
 "g4 e5 d3 d5 Bg2 c6 e4 Bc5 Qe2 d4 g5 Be6 f4 exf4 Bxf4 Ne7 Nd2 Bb4 a3 Ba5 b4 Bb6 Bh3 Bxh3 Nxh3 O-O Nc4 Bc7 O-O-O Bxf4+ Nxf4 Ng6 Rdf1 Nxf4 Rxf4 Nd7 Rhf1 Qe7 Qg4 Ne5 Nxe5 Qxe5 h4 a5 Rf5 Qe6 bxa5 Rxa5 Rxf7 Qxf7 Rxf7 Rxf7 Qc8+ Rf8 Qe6+ Kh8 Qe7 Rg8 h5 Raa8 e5 b5 e6 b4 Qxb4",
 {
  "2...d5": "This effectively hinders the White thrust e4, while also directly countering White's initiative on the King-side. Not to be overlooked is the possiblility of Black developing a Queen-side attack.",
  "3.Bg2": "<div class=\"alts\"><span class=\"cap\">вместо Bg2</span><div class=\"alt\"><b>3.g5?</b>5? (3…h6!? 4.Nf3 hxg5 5.Nxe5! f6? 6.Ng6 Rh6 7.Nxf8 with an advantage to White; Grob-Unknown) Be7 4.h4 h6 favors Black.</div></div>",
  "3...c6": "<div class=\"alts\"><span class=\"cap\">вместо c6</span><div class=\"alt\"><b>3…a5!?</b>4.e4! dxe4 5.Bxe4 (5…Qh4? 6.h3 Nf6? 7.Nf3 Bxg4 8.Nxh4 Bxd1 9.Kxd1 and White wins a piece) Nf6 6.Bf3 Be7 7.Nc3 c6 8.h3 O-O 9.Nge2 Re8 10.Ng3 Bb4 11.Bg5 (11…h6!? 12.Bd2 Nh7 13.h4 Be7 14.g5 offering the pawn for an open Rook-file; Grob) Be7 12.Bxf6 Bxf6 13.Nce4 Bh4 14.Qd2 Bxg3 15.Nxg3 Nd7 16.O-O-O c5 17.Kb1 Ra6 18.g5 Ree6 19.Bd5 Red6 20.Bc4 Ra7 21.Ne4 Rb6 22.Rdg1 Nf8 23.Nxc5 a4 24.Qe3 Ng6 25.h4 Qd4 26.Qxd4 exd4 27.Re1 Be6 28.Nxe6 fxe6 29.Bxe6+ Kh8 30.Bc8 Nf8 31.Re8 Kg8 32.Rhe1 Raa6 33.R1e7 h6 34.f4 <i>1-0 Grob,H-Rutter/corr 1965 (34) Black resigned.</i></div><div class=\"alt\"><b>3…Bc5</b>4.g5 Nc6 5.Nc3 Be6 6.e4 Nge7 7.h4 Qd7 8.a3 O-O-O (9.Bh3!?) 9.exd5 Nxd5 10.Ne4 Be7 11.Ne2 f5 12.N4c3 h6 (13.g6!) 13.Ng3? Nxc3 14.bxc3 Bd5 15.f3 f4 <i>0-1 Grob,H-Tien/corr 1963 (15) with solid advantage to Black.</i></div><div class=\"alt\"><b>3…Bxg4</b>4.c4 (4…c6 5.cxd5 cxd5 6.Qb3 Ne7 (Blocking in the King-bishop) 7.Qxb7 Nbc6 8.Bxd5 Qxd5 9.Qxa8+ Bc8 10.Nf3 Kd7 (unfortunately there is no Queen trap here) 11.Nc3 Qa5 12.Bd2 f6 13.Ne4 Qb5 14.b4! Nd5 15.a4 Qb6 16.b5 Ncb4 17.a5 Qc7 18.O-O Nf4 19.Bxf4 exf4 20.b6 axb6 21.axb6 Qxb6 22.Ra7+ Kd8 23.Rc1 Nc2 24.Ra2 Ne3 25.Qxc8+ Ke7 26.Rc7+ <i>1-0 Grob,H-Kellenberger,S/corr 1965 (26) Black resigns.</i>) (4…Be6 5.Qb3 b6 6.cxd5 Bd7 7.Nc3 a5 8.Be3 Bd6 9.Ne4 Bb4+ 10.Nc3 Bd6 11.a3 a4 12.Qc4 with some advantage; analysis by Grob.) Bb4+ 5.Nd2 c6 6.cxd5 Ne7 7.dxc6 Nbxc6 8.a3 Bxd2+ 9.Bxd2 O-O 10.Nf3 Qd7 11.Be3 f6 <i>1/2-1/2 Grob,H-Aebi/ corr 1965 (11)</i></div></div>",
  "4.e4": "<div class=\"alts\"><span class=\"cap\">вместо e4</span><div class=\"alt\"><b>4.h3</b>h3 Ne7 5.Nf3 Ng6 6.Nc3 (6…f5! with an immediate advantage to Black) h6? (7.e4!) 7.e3 Bd6 8.e4 <i>1-0 Grob, H-Stingelin/corr 1965 (41) and while White has slightly the better position, its meaning is wasted.</i></div></div>",
  "4...Bc5": "<b>Bc5!</b> — <div class=\"alts\"><span class=\"cap\">вместо Bc5</span><div class=\"alt\"><b>4…dxe4</b>5.Bxe4 : (5…Be6 6.h3 Be7 7.Be3 Nf6 8.Nc3 Nbd7 9.Bf3 with an unclear position.) Nf6 6.Bf3 (6…e4? 7.Qe2!) h6 7.Nc3 , etc</div></div>",
  "5.Qe2": "<div class=\"alts\"><span class=\"cap\">вместо Qe2</span><div class=\"alt\"><b>5.h4</b>h4 is risky, e.g. dxe4 6.Bxe4 Nf6 7.Bf3 Qd4 8.Qe2 Bxg4 with a solid advantage to Black.</div></div>",
  "5...d4": "White has a very minimal edge, and the position is quite double-edged.",
  "33.Qxb4": "Bloodgood-J. Boothe, 1973 Black resigned."})

add("a6", C7, "Вариант A6", "÷", "÷ по Бладгуду",
 "g4 Nf6 g5 Nd5 d4 e6 a3 Be7 e4 Nb6 f4",
 {
  "1...Nf6": "<b>Nf6!?</b> — This is not very effective, and is not recommeded.",
  "2...Nd5": "<div class=\"alts\"><span class=\"cap\">вместо Nd5</span><div class=\"alt\"><b>2…Ne4?</b>3.d3 Nd6 4.Bg2 g6 5.c4 c5 6.Nc3 Bg7 7.e4 Nc6 8.Nge2 e5 9.Nd5 O-O 10.h4 (10…Ne8) Ne7? 11.Nf6+ Kh8 12.Nc3 Ne8 13.Nxe8 Rxe8 14.h5 <i>1-0 Grob,H-Monney,E/corr 1964 (29) with a strong attack.</i></div><div class=\"alt\"><b>2…Nh5</b>3.d3 e5 4.e4 (4…Nf4 5.Bxf4 exf4 6.Qg4!) g6 5.Be2 Ng7 6.Nf3 d6 7.d4 with an advantage for White; Grob.</div></div>",
  "6.f4": "White clearly has the better chances."})

add("b6", C7, "Вариант B6", "÷", "÷ по Бладгуду",
 "g4 h5 g5 h4 d4 d6 Qd3 g6 Bg2 Nc6 c3 Bd7 Na3",
 {
  "1...h5": "An immediate challenge to White's K-side ambition which is very double-edged .",
  "2.g5": "Of doubtful value is 2.gxh5!? which does nothing for White and merely opens the Rook-file for Black.",
  "2...h4": "<div class=\"alts\"><span class=\"cap\">вместо h4</span><div class=\"alt\"><b>2…e5</b>(3.h4 d5 4.Bg2 Ne7 5.c4 dxc4 6.Qc2 c6 7.Qxc4 Be6 (8.Qc3 Ng6 9.d3 Qb6!) 8.Qc2! Na6 9.a3 Qc7 10.d3 (10…Nf5 11.Nf3 Nc5 12.Nbd2 a5 13.b3 f6 14.Bb2 a4 15.b4 Nb3 16.Nxb3 Bxb3 17.Qc3 Ne7 18.e4 Ng6 19.Bc1 Bd6 20.gxf6 gxf6 21.Bh3 Qf7 22.Be3 Ba2 23.Rg1 Rg8 24.Ke2 Rd8 with an unclear position; Grob-Wettstein, corr.) f5 11.b4 O-O-O 12.Nc3 Nd5 (13.Nh3 Nxc3 14.Qxc3 Rd4 15.f4 Nxb4 16.fxe5 Qxe5 17.Nf4 Bc5 18.Rh3 Rxd3 19.Rxd3 Nxd3+ 20.Qxd3 Qxa1 <i>0-1 Grob,H-Wettstein,M/corr 1964 (20)</i>) 13.Nxd5 Bxd5 14.Bxd5 Rxd5 15.Bb2 Nxb4!? (This is not good as it opens lines to the Black King.) 16.axb4 Bxb4+ 17.Kf1 <i>1/2-1/2 Grob,H-Wettstein,M/corr 1966 (62) with a winning advantage to White to White.</i>) 3.d4 exd4 4.Qxd4 Nc6 5.Qe4+ Qe7 6.Bg2 d6 7.Nc3 f5 8.Qxe7+ Ngxe7 9.h4 Bd7 10.Be3 O-O-O 11.Nh3 Be6 12.Nf4 Bf7 13.O-O d5 14.Bc5 b6 15.Bxe7 Nxe7 16.Rad1 c6 <i>1/2-1/2 Bloodgood,C-Buntin,L/ corr 1974/Megacorr (16) with some advantage to White.</i></div></div>",
  "3...d6": "<div class=\"alts\"><span class=\"cap\">вместо d6</span><div class=\"alt\"><b>3…c5</b>4.d5 g6 5.e4 d6 6.h3 f5 7.f3 e5 8.dxe6 Bxe6 9.exf5 Bxf5 10.Bc4 Ne7 11.Nc3 Bg7 12.Nd5 Nxd5 (13.Bxd5 is less complicated.) 13.Qxd5 Qe7+ 14.Kd1 Nc6 15.c3 O-O-O 16.Rh2 Rde8 17.Re2 Qd7 18.Bf4 Ne5 19.Bxe5 Rxe5 20.Qf7 Qxf7 21.Bxf7 Rxe2 22.Kxe2 Be5 <i>1/2-1/2 Grob,H-Wettstein,M/corr 1964 (22)</i></div></div>",
  "5...Nc6": "<div class=\"alts\"><span class=\"cap\">вместо Nc6</span><div class=\"alt\"><b>5…Bg7</b>6.h3 Nc6 7.c3 e5 8.d5 Nce7 9.e4 f5 10.gxf6 Bxf6 11.Nf3 Rh5 12.Be3 g5 13.Nh2! Ng6 14.Bf3 Rh7 15.Bg4! Nf4 16.Bxf4 exf4 17.Nd2 c5 18.dxc6 bxc6 19.O-O-O Rc7 20.Rhe1 Kf8 21.Bxc8 Qxc8 22.Qxd6+ Be7 23.Qg6 Qxh3? ( a costly \"gift\") 24.Ndf3 Rd8 25.Ne5 <i>1-0 Grob, H-Wettstein,M/corr 1964 (25) Black resigned.</i></div></div>",
  "7.Na3": "White has an advantage."})

add("c6", C7, "Вариант C6", "÷", "÷ по Бладгуду",
 "g4 g5 h4 e6 Nf3 Be7 hxg5 Bxg5 Nxg5 Qxg5 e4 Nf6 d4",
 {
  "1...g5": "<b>g5!?</b> — This allows White to hold the initiative for a long time.",
  "2.h4": "<b>h4!</b>",
  "2...e6": "<div class=\"alts\"><span class=\"cap\">вместо e6</span><div class=\"alt\"><b>2…f6?</b>3.d4 Bh6 4.Nf3! ; Grob.</div></div>",
  "3.Nf3": "<b>Nf3!</b> — <div class=\"alts\"><span class=\"cap\">вместо Nf3</span><div class=\"alt\"><b>3.hxg5</b>g5 Qxg5 4.e4 d6 5.d3 Qe7 6.g5 d5 7.Bg2 d4 8.f4 e5 after which White obtains a lasting advantage with 9.f5 Grob-Unknown</div></div>",
  "3...Be7": "<div class=\"alts\"><span class=\"cap\">вместо Be7</span><div class=\"alt\"><b>3…gxh4</b>4.Rxh4 is good for White.</div></div>",
  "6...Nf6": "This move seems sharper than it is; Grob.",
  "7.d4": "Black now has an awkwardly placed Queen and nothing is seriously threatened."})

add("d6", C7, "Вариант D6", "÷", "÷ по Бладгуду",
 "g4 g6 Bg2 h6 e4 Bg7 d4 e6 Nf3 d5 Nbd2 dxe4 Nxe4 Nf6 Nxf6+ Bxf6",
 {
  "1...g6": "Should the Grob become a popular opening, this defense will undoubtedly become a major line, but for the present it is still among the seldom played variations.",
  "2...h6": "<div class=\"alts\"><span class=\"cap\">вместо h6</span><div class=\"alt\"><b>2…Bg7</b>3.c4 d6 4.Nc3 Nf6 (5.g5!) 5.h3 O-O 6.d4 c6 7.Be3 a6 8.Qb3 Nbd7 (9.Nf3!) 9.Rd1 Qb6 10.Nf3 Qxb3!? (this is giving White an open Queen/Rook-file with pawns handy for levers) 11.axb3 with advantage to White.</div></div>",
  "5...d5": "<div class=\"alts\"><span class=\"cap\">вместо d5</span><div class=\"alt\"><b>5…Nf6</b>6.Ne5 d6 7.Nd3!</div></div>",
  "7...Nf6": "<div class=\"alts\"><span class=\"cap\">вместо Nf6</span><div class=\"alt\"><b>7…f5</b>8.gxf5 (8…exf5!) gxf5 9.Nc5 Nc6 10.c3 b6 11.Nh4! Qd6 12.Nd3 Bd7 13.Ng6 Rh7 14.Bf4! e5 15.Ngxe5 <i>1-0 Grob,H-Bartschiger/corr 1967 (15) with a winning attack.</i></div></div>",
  "8...Bxf6": "The position is not clear."})

add("e6", C7, "Вариант E6", "÷", "÷ по Бладгуду",
 "g4 b5 Bg2 c6 a4 d5 axb5 Nf6 c4",
 {
  "1...b5": "<b>b5!?</b> — This counter play on the long diagonal is hardly good for Black.",
  "3.a4": "<b>a4!</b>",
  "3...d5": "<div class=\"alts\"><span class=\"cap\">вместо d5</span><div class=\"alt\"><b>3…Qb6</b>with 4.axb5 Qxb5 5.Nc3</div><div class=\"alt\"><b>3…Qa5</b>with 4.b3 followed by Bb2.</div></div>",
  "5.c4": "<b>c4!</b> — White has much the better of this!"})

add("f6", C7, "Вариант F6", "÷", "÷ по Бладгуду",
 "g4 c5 Bg2 Nc6 e4 e5 d3 Nge7 h4 d5 Nc3",
 {
  "1...c5": "This line can transpose into a sicilian Defense, but it not likely to create the same problems for White."})

add("g6", C7, "Вариант G6", "÷", "÷ по Бладгуду",
 "g4 c6 c4 d5 Qb3 Qc7 cxd5 cxd5 Nc3 e6 d4",
 {
  "1...c6": "This is decidedly inferior to 1...d5.",
  "2.c4": "<div class=\"alts\"><span class=\"cap\">вместо c4</span><div class=\"alt\"><b>2.Bg2</b>g2 e6 3.d3 (3…d5!) Nf6? 4.g5 (4…Ng8 was best.) Ng4? 5.d4! c5 6.h3 <i>1-0 Grob, H-Hasselblatt/corr 1964 (21) and White wins the piece.</i></div><div class=\"alt\"><b>2.Bg2</b>g2 d5 transposes to Part II.</div></div>",
  "2...d5": "<div class=\"alts\"><span class=\"cap\">вместо d5</span><div class=\"alt\"><b>2…g5!?</b>3.d4 h6 4.e4 e6 5.d5 (5…d6!) b6? 6.Qd4 f6 7.d6 c5 8.Qd3 b5 9.e5 Bg7 10.Bg2 Nc6 11.Bxc6 dxc6 12.cxb5 Bb7 13.Be3! cxb5 14.f3 c4 15.Qg6+ Kf8 16.Bc5 <i>1-0 Grob, H-Steucheli/corr 1964 (23) with a winning advantage.</i></div></div>",
  "3.Qb3": "<div class=\"alts\"><span class=\"cap\">вместо Qb3</span><div class=\"alt\"><b>3.cxd5?</b>5? Qxd5 with</div></div>",
  "3...Qc7": "<div class=\"alts\"><span class=\"cap\">вместо Qc7</span><div class=\"alt\"><b>3…dxc4</b>4.Qxc4 with a position similar to those in Part II, Variation \"A\" without being down a pawn.</div></div>",
  "5.Nc3": "<div class=\"alts\"><span class=\"cap\">вместо Nc3</span><div class=\"alt\"><b>5.Bg2</b>g2 Qxc1+</div></div>",
  "6.d4": "White has some advantage, and somewhat more freedom for his pieces."})

add("h6", C7, "Вариант H6", "÷", "÷ по Бладгуду",
 "g4 d6 Bg2 e5 d3 c6 e4 d5 h3 d4 Nf3 f6 Nh4 g5 Nf5 Ne7 h4 Ng6 hxg5 fxg5 Rh5 Nf4 Bxf4 exf4 Nd2 Bxf5 exf5 h6 Qe2+",
 {
  "1...d6": "This is passive and while not exactly bad, it hardly poses any major threats.",
  "2...e5": "<div class=\"alts\"><span class=\"cap\">вместо e5</span><div class=\"alt\"><b>2…a6</b>3.h3 h5 4.g5 e5 5.d3 f6 6.gxf6 Nxf6 7.Nf3 Be7 8.Ng5 h4 9.c4 Nh5 10.Ne4 Bf5 11.Qb3 <i>1/2-1/2 Grob,H-Gabreilli/corr 1964 (11) With a solid advantage to White.</i></div><div class=\"alt\"><b>2…c6</b>3.h3 h6 4.c4 e5 5.Nc3 (5…f5 is more aggressive, but unlikely from a player choosing such a passive line) Be6 6.b3 Be7 7.Nf3 Nf6 8.d3 Nbd7 9.e4 d5 10.exd5 cxd5 11.Qe2 Bb4 12.Bd2 Qa5 13.Rc1 e4 14.dxe4 dxe4 15.Nxe4 Nxe4 16.Qxe4 Nc5 17.Qc2 Rd8 18.Bxb4 Qxb4+ 19.Qc3 Nd3+ 20.Kf1 <i>1-0 Grob,H-Stoll/corr 1966 (49) and White has a pawn with a better position.</i></div><div class=\"alt\"><b>2…Nc6</b>(3.g5 (3…e5!) f6? 4.h4 g6 5.d4 h6 6.Qd3 f5 7.f4 Qd7 8.d5 (8…Nd8) Nb4? 9.Qc3 a5 10.Qxh8 Nxc2+ 11.Kf1 Kf7 12.Qh7+ Bg7 13.h5 gxh5 14.Rxh5 Kf8 15.gxh6 e6 16.dxe6 Qe7 17.hxg7+ Black resigned.) 3.h3 g6 4.d4 Bg7 5.c3 e6 6.e4 Nge7 7.Ne2 O-O 8.Be3 (This is better than an immediate 8.h4) b6 9.Nd2 Bb7 10.Ng3 f5 11.f4 e5 12.dxe5 Nxe5 (13.fxe5 f4!) 13.O-O Nd3 14.exf5 Bxg2 15.Kxg2 Qd7 16.Nf3 Qb5 17.Rb1 Nd5 18.Qd2 Rae8 19.Nd4 Nxe3+ 20.Qxe3 Qxb2+ 21.Rxb2 Rxe3 22.Re2 Bxd4 23.cxd4 Rxe2+ 24.Nxe2 gxf5 25.Kf3 fxg4+ 26.hxg4 <i>1-0 Grob,H-Heinrich/corr 1965 (40) at which point Black can play</i> d5 with advantage.</div></div>",
  "3.d3": "<div class=\"alts\"><span class=\"cap\">вместо d3</span><div class=\"alt\"><b>3.c4</b>c4 c6 4.h3 f5 5.e3 g6 6.Nc3 Be6 7.Qb3 <i>1/2-1/2 Bloodgood,C-Jackson,R/corr 1972 (7) and White stands a little better.</i></div></div>",
  "5.h3": "Black has lost a tempo",
  "5...d4": "<b>d4!?</b> — <div class=\"alts\"><span class=\"cap\">вместо d4</span><div class=\"alt\"><b>5…g6!</b></div></div>",
  "7...g5": "<b>g5?</b> — <div class=\"alts\"><span class=\"cap\">вместо g5</span><div class=\"alt\"><b>7…g6!</b></div></div>",
  "13...Bxf5": "<div class=\"alts\"><span class=\"cap\">вместо Bxf5</span><div class=\"alt\"><b>13…Be6!</b></div></div>",
  "14...h6": "<b>h6?</b> — <div class=\"alts\"><span class=\"cap\">вместо h6</span><div class=\"alt\"><b>14…Bb4</b></div></div>",
  "15.Qe2+": "with a solid advantage to White. Grob-Suhner, Corr."})

add("i6", C7, "Вариант I6", "÷", "÷ по Бладгуду",
 "g4 e6 d3 d5 Bg2 c5 c4 d4 Qb3 Qc7 Nd2 Nc6 Ne4 Nf6 g5 Nxe4 Bxe4 Be7 h4 h6 Nh3 hxg5 hxg5 e5 Bg2 g6 Bd2 Qb6 O-O-O Qxb3 axb3 a5 f4 Bxh3 Rxh3 Rxh3 Bxh3 exf4 Bxf4 a4 bxa4 Rxa4 Kb1 f6 gxf6 Bxf6 Rg1 Kf7 Bd7 Ra6 Bc8 Rb6 Bc7 Rb4 Rf1 Ke7 Rh1 Ne5 Bxe5 Bxe5 Rh7+ Kd6 Bxb7 g5 Bd5 g4 Rh6+ Kc7 Rc6+ Kd7 Rxc5 g3 Bc6+ Ke6 Bd7+ Kf6 Bh3",
 {
  "1...e6": "This apparently Innocent defense is not simple for White to handle, and several pitfalls must be examined.",
  "2.d3": "<div class=\"alts\"><span class=\"cap\">вместо d3</span><div class=\"alt\"><b>2.Bg2!?</b>!? h5! 3.h3 hxg4 4.hxg4 Rxh1 5.Bxh1 Qh4 6.Bf3 Nf6 7.e4 d6 8.d4 e5 9.g5 Nh7 10.dxe5 Nxg5 11.Bxg5 Qxg5 12.Ne2 Qxe5 13.Nbc3 Nc6 14.Nd5 Kd8 15.Nec3 Nd4 16.Ne3 Nxf3+ 17.Qxf3 f6 18.O-O-O Be6 19.Kb1 Ke7 20.Ned5+ Kd7 21.Nf4 Bf7 22.Qg4+ Ke7 23.Ncd5+ Kd8 24.Ng6 Bxg6 25.Qxg6 c6 26.f4 Qe6 27.Ne3 Kc7 <i>0-1 Bloodgood, C-Stroemer,D/Virginia 1972 (27) with advantage to Black.</i></div><div class=\"alt\"><b>2.d4!?</b>!? d5! (3.Bg2 c5 4.c3 Nc6 5.Nf3 Nf6 , and even then, Black has the initiative; Grob) (3.c4! dxc4 4.Qa4+ Bd7 5.Qxc4 Bc6 6.Bg2 Nd7 favors White) 3.Nf3 (3…c5! 4.e3 Nc6 5.h3 Nf6 6.Nbd2 h6 7.c3 Bd7 8.Bg2 Qc7 9.O-O (9…Bd6 is recommended by Grob) O-O-O 10.dxc5 Bxc5 11.b4 Bd6 12.Bb2 Ne5 13.Nxe5 Bxe5 14.a4 Ne4 15.Nxe4 dxe4 16.Qb3 f5 17.b5 g5 18.a5 a6 19.c4 Bxb2 20.Qxb2 h5 21.gxf5 exf5 22.Rab1 Rh6 23.Qg7 Qd6 24.bxa6 Qxa6 25.f3 Rg6 26.Qb2 Bc6 27.fxe4 fxe4 28.Qe5 <i>1-0 Grob,H-Ruegg/corr 1964 (39) with advantage to White.</i>) (3…c5! 4.c3 Nc6 5.Bg2 cxd4 6.cxd4 Bb4+ with initiative for Black.) Nf6? 4.Rg1 h6 5.h4 (5…Nbd7!) Nc6 6.c3 Be7 7.g5 hxg5 8.hxg5 Ne4 9.g6 f6 10.Nbd2 f5 11.Nxe4 fxe4 12.Ne5 Nxe5 13.dxe5 Rh5!? 14.Bf4 Bg5? 15.e3! Bxf4 16.Qxh5 <i>1-0 Grob,H-Schaufelberger,H/ corr 1964 (16) with a winning advantage for White.</i></div></div>",
  "3.Bg2": "<div class=\"alts\"><span class=\"cap\">вместо Bg2</span><div class=\"alt\"><b>3.Nc3</b>c3 (3…Bb4 4.Bd2!) c5 4.e4 (4…dxe4 5.dxe4 Qxd1+ 6.Nxd1 Nf6 7.f3) (4…d4 5.Nce2 e5 6.Ng3 with K-side initiative; Grob.) Nc6</div></div>",
  "4.c4": "White has the initiative and potential threats on both flanks!",
  "14...Qb6": "<b>Qb6!?</b>",
  "17...Bxh3": "<b>Bxh3?</b>",
  "22...f6": "<b>f6?</b>",
  "30...Bxe5": "<b>Bxe5?</b>",
  "33...g4": "<b>g4?</b>",
  "39.Bh3": "Bloodgood-T. Sanderson, 1973; Black resigned."})

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
  ],
  "21...Kh8": [   [    "вместо Kh8",
    "Ng6",
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
  ],
  "24.Qxa6": [   [    "вместо Qxa6",
    "Qxd7+",
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
  ],
  "21...Nb4": [   [    "вместо Nb4",
    "Nxe5",
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
