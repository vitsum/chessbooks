# -*- coding: utf-8 -*-
"""Перевод авторских комментариев «The Tactical Grob» на русский.

Комментарии Бладгуда и Гроба почти сплошь формульные: из 578 штук больше половины —
короткие вердикты вроде «with advantage to White.». Поэтому перевод сделан словарём,
а не пересказом: EXACT для живых фраз целиком, PHRASES для повторяющихся кусков.

Ссылки на партии («1-0 Bloodgood,C-Clark,J/corr Zugzwang 1975 (23)») не переводятся:
это имена, места и годы. Переводится только вердикт после них.

Отчёт о непокрытом: python3 src/grob_ru.py books/tactical_grob.pgn
"""
import re

# ---------------------------------------------------------------- живые фразы целиком
EXACT = {
 "This solid defensive line is an attempt by Black to move the game into positional situations rather than meet the tactical possiblilities resulting from 2...Bxg4!? White has several playable alternatives":
   "Солидная защита: чёрные уводят игру в позиционное русло, лишь бы не связываться с тактикой после 2…Bxg4!? У белых есть несколько годных продолжений",
 "The \"Short Spike\" is a fluid system in which White has several interesting means of disrupting the black defenses. The obvious threat of g5 discourages development of the black Knight at f6":
   "«Короткий шип» — гибкая система, в которой у белых несколько любопытных способов расстроить оборону чёрных. Очевидная угроза g5 мешает вывести коня на f6",
 "This is the key line in Grob's Attack, and the tactical aspects of the position are unlimited.":
   "Ключевая линия атаки Гроба: тактические возможности позиции безграничны.",
 "This is Black's most aggressive reply and must be treated with respect. Several lines of play are good for White at this point.":
   "Самый агрессивный ответ чёрных, к нему надо отнестись серьёзно. У белых здесь несколько хороших продолжений.",
 "White's king's side pressure is obvious, and must be countered. To allow White a free hand on the king's side invites disaster.":
   "Давление белых на королевском фланге очевидно, и его надо чем-то встречать. Дать белым там свободу рук — напроситься на разгром.",
 "The position is certainly far from clear, but it is equally apparent that Black will encounter some difficulty on the King-side.":
   "Позиция далеко не ясна, но так же ясно, что на королевском фланге чёрным придётся несладко.",
 "Black is virtually committed to exchanging his King-Knight, after which White has a strong attack on the King-side.":
   "Чёрные фактически обязаны менять королевского коня, после чего у белых сильная атака на королевском фланге.",
 "Of the remaining alternative for Black at move two, this is the line with the most possibilities. Others are playable.":
   "Из оставшихся вторых ходов чёрных этот даёт больше всего возможностей. Прочие тоже играбельны.",
 "This apparently Innocent defense is not simple for White to handle, and several pitfalls must be examined.":
   "На вид безобидная защита, но белым с ней непросто: подводных камней хватает.",
 "This line can transpose into a sicilian Defense, but it not likely to create the same problems for White.":
   "Линия может перейти в сицилианскую защиту, но таких проблем белым, скорее всего, не создаст.",
 "This is safe, but offers Black no more than equality if he avoids the balance of the traps in his path.":
   "Надёжно, но большего равенства чёрным не даст — если они обойдут остальные ловушки по дороге.",
 "Perhaps Black does best with 8...N e7 to g6; however the text is the most aggressive move at Black's disposal.":
   "Возможно, лучше всего 8…Ne7-g6, но ход в тексте — самый агрессивный из имеющихся у чёрных.",
 "is a queen trap of interest because it occurs in a line where Black appears to have good counterplay.":
   "— любопытная ловушка на ферзя: она встречается там, где у чёрных вроде бы хорошая контригра.",
 "Of doubtful value is 2.gxh5!? which does nothing for White and merely opens the Rook-file for Black.":
   "Сомнительно 2.gxh5!?: белым это ничего не даёт и лишь вскрывает ладейную линию чёрным.",
 "This line of play has proven very double-edged, and may well be Black's best.":
   "Продолжение оказалось очень обоюдоострым и вполне может быть лучшим за чёрных.",
 "While this line of play is very complicated, it is also probably Black's best.":
   "Линия очень запутанная, но, вероятно, лучшая за чёрных.",
 "This line of play lacks sting! White should get an advantage with proper play.":
   "Беззубое продолжение! При правильной игре белые получают перевес.",
 "This is an awkward line for Black which creates more problems than it solves.":
   "Неудобная для чёрных линия: проблем создаёт больше, чем решает.",
 "This is passive and while not exactly bad, it hardly poses any major threats.":
   "Пассивно; не то чтобы плохо, но серьёзных угроз не создаёт.",
 "An immediate challenge to White's K-side ambition which is very double-edged .":
   "Немедленный вызов замыслам белых на королевском фланге — очень обоюдоостро.",
 "Black now has an awkwardly placed Queen and nothing is seriously threatened.":
   "Ферзь чёрных стоит неуклюже, а серьёзных угроз нет.",
 "White has a very minimal edge, and the position is quite double-edged.":
   "Перевес белых минимален, позиция обоюдоострая.",
 "White has some advantage, and somewhat more freedom for his pieces.":
   "У белых некоторый перевес и чуть больше свободы для фигур.",
 "Simply an unsound combination; Black had equality before this move.":
   "Просто некорректная комбинация: до этого хода у чёрных было равенство.",
 "The move is probably best, but a little exploration here is overdue.":
   "Ход, вероятно, лучший, но разобраться тут давно пора.",
 "Black is very cramped, but a waiting move was all that he could play.":
   "У чёрных очень тесно, но выжидательный ход — всё, что им оставалось.",
 "This allows White to hold the initiative for a long time.":
   "Это позволяет белым надолго удержать инициативу.",
 "White clearly has the initiative, but there are complications.":
   "Инициатива явно у белых, но осложнения не исключены.",
 "White has the initiative and potential threats on both flanks!":
   "У белых инициатива и потенциальные угрозы на обоих флангах!",
 "This counter play on the long diagonal is hardly good for Black.":
   "Контригра по большой диагонали чёрным вряд ли на пользу.",
 "This passive line should offer White no problems. Grob suggests:":
   "Пассивная линия, белым проблем не создаёт. Гроб предлагает:",
 "This seemingly logical development does little to counter-act White's basic King-side threats.":
   "Логичное на вид развитие мало что противопоставляет главным угрозам белых на королевском фланге.",
 "White has a clear advantage, but Black may be able to gradually off-set this with good play.":
   "У белых явный перевес, но при хорошей игре чёрные могут постепенно его нейтрализовать.",
 "White hs the better of this, and possibly enough to discourage this line for Black altogether.":
   "У белых лучше, и, возможно, настолько, что чёрным эту линию играть расхочется.",
 "This is a risky gambit for White to play, but it is far from simple for Black to refute.":
   "Рискованный гамбит за белых, но опровергнуть его чёрным совсем не просто.",
 "This frequently transposes to Variation \"A\". Several independent lines also are possible:":
   "Часто переходит в вариант «A» перестановкой ходов. Возможны и самостоятельные линии:",
 "Black threatens 8...Qd4! This is obviously not good for White.":
   "Чёрные грозят 8…Qd4! Белым это явно не годится.",
 "and Black's pieces are committed to the defense of his king":
   "и фигуры чёрных прикованы к защите короля",
 "and White resigned. This line is worth exploring for White.":
   "и белые сдались. Линию стоит изучить внимательнее.",
 "gives White a pawn while doing nothing to ease Black's position":
   "отдаёт белым пешку и ничем не облегчает положение чёрных",
 "where Black has 2 pawns, but a bad defensive position; and now:":
   "где у чёрных две пешки, но плохая оборонительная позиция; и теперь:",
 "is not particularly good for Black, so 13...Bf7 is forced; after which:":
   "чёрным не особенно хорошо, так что 13…Bf7 вынужденно; после чего:",
 "is more aggressive, but unlikely from a player choosing such a passive line":
   "агрессивнее, но вряд ли от того, кто выбрал столь пассивную линию",
 "winning the a-pawn and leaving Black facing the inevitable Queenside pawn onslaught":
   "выигрывая пешку a и оставляя чёрных перед неизбежным пешечным наступлением на ферзевом фланге",
 "with the initiative for a pawn White doesn't really want.":
   "с инициативой за пешку, которая белым, в общем-то, не нужна.",
 "with White holding the pawn at the cost of the initiative.":
   "белые удерживают пешку ценой инициативы.",
 "Grob gives this as best and cites the following variation":
   "Гроб считает это сильнейшим и приводит такой вариант",
 "From the diagram position shown, the following are not good:":
   "Из позиции на диаграмме не годится следующее:",
 "with a position similar to those in Part II, Variation \"A\" without being down a pawn.":
   "с позицией вроде тех, что в части II, вариант «A», но без потери пешки.",
 "(this solid move avoids all the complications of 7 Nxd5)":
   "(солидный ход, уводящий от всех осложнений после 7.Nxd5)",
 "(this is giving White an open Queen/Rook-file with pawns handy for levers)":
   "(это даёт белым открытую линию для ферзя и ладьи, а пешки рядом — как рычаги)",
 "(Black is trying to avoid a number of Queen traps and survive the attack. Something has to fall)":
   "(чёрные пытаются обойти ловушки на ферзя и пережить атаку. Что-то всё равно упадёт)",
 "(compare this with the position after 9... Kd8 in Bloodgood-Ebright below)":
   "(сравни с позицией после 9…Kd8 в партии Бладгуд — Эбрайт ниже)",
 "as cramped as Black's position was, this was no answer...an idea would be 13...a5 followed by Ra6,":
   "как ни тесно было чёрным, это не ответ… мысль была в 13…a5 с последующим Ra6,",
 "winning a piece; H. Grob-Unknown This trap is important since it can occur frequently in the Spike.":
   "выигрывая фигуру; Гроб — неизвестный. Ловушка важна: в «шипе» она встречается часто.",
 "' This position is not at all clear, but the maze of complications have been reduced to a managable level. '":
   "«Позиция совсем не ясна, но лабиринт осложнений сведён к обозримому».",
 ", Black has a number of playable alternatives which for the most part have not been examined in any detail. While Part 4 will serve s a general guide for play against several of these, it is":
   ", у чёрных есть ряд играбельных продолжений, по большей части толком не разобранных. Часть 4 даёт общий ориентир против некоторых из них, но это",
}

# ---------------------------------------------------------------- повторяющиеся куски
# порядок важен: длинные раньше коротких
# --- длинные авторские куски, которые словарём фраз не собрать ---
EXACT.update({
 "The \"Short Spike\" is a fluid system in which White has several interesting means of disrupting the black defenses. The obvious threat of g5 discourages development of the black Knight at f6, and any attempt to attack this pawn structure to neutralize the threat has the effect of simultaneously weakening the black defenses. Should Black not play aggressively, the are still gambit possibilities for White which render the long diagonal a melting pot of double-edged tactics.":
   "«Короткий шип» — гибкая система, в которой у белых несколько любопытных способов расстроить оборону чёрных. Явная угроза g5 отбивает охоту выводить коня на f6, а любая попытка атаковать эту пешечную структуру, чтобы снять угрозу, заодно ослабляет и оборону чёрных. Если чёрные не играют активно, у белых остаются гамбитные возможности, превращающие большую диагональ в котёл обоюдоострой тактики.",

 "This solid defensive line is an attempt by Black to move the game into positional situations rather than meet the tactical possiblilities resulting from 2...Bxg4!? White has several playable alternatives now: Variation \"A1\" covers the \"Double Gambit\" 3. c4; Variation \"B1\" covers the \"Short Spike' 3. h3; and Variation \"C1\" covers the \"Spike\" 3. g5.":
   "Солидная защита: чёрные уводят игру в позиционное русло, лишь бы не связываться с тактикой после 2…Bxg4!? У белых теперь несколько годных путей: вариант «A1» — «двойной гамбит» 3.c4, вариант «B1» — «короткий шип» 3.h3, вариант «C1» — «шип» 3.g5.",

 "The \"Spike\" is a system which disrupts Black's normal lines of development and creates immediate problems for him. White has an obvious kind-side attack and to counter this, Black must react aggressively or literally expect to be pushed off the board":
   "«Шип» — система, которая ломает чёрным привычное развитие и сразу создаёт им проблемы. Атака белых на королевском фланге очевидна, и чёрным приходится отвечать активно — иначе их буквально сметут с доски",

 "White has the better of this in several ways. First, the Black KRP is a problem for the second player to defend. Add to this the delays Black faces in developing his King-side because of the \"Spike\" pawn while White can free his pieces easily.":
   "У белых лучше сразу по нескольким причинам. Во-первых, чёрным трудно защищать пешку h. Прибавь к этому задержку в развитии королевского фланга из-за пешки-«шипа», тогда как белые разворачивают фигуры без помех.",

 "Black's purpose in playing 3...e5 is to avoid the compications arising after any direct attempt to hold the gambit pawn; since the pawn cannot be held anyway, this would seem best, but has not proven successful in practice.":
   "Смысл 3…e5 — обойти осложнения, возникающие при попытке удержать гамбитную пешку. Удержать её всё равно нельзя, так что решение выглядит логичным, но на практике себя не оправдало.",

 "This effectively hinders the White thrust e4, while also directly countering White's initiative on the King-side. Not to be overlooked is the possiblility of Black developing a Queen-side attack.":
   "Ход надёжно мешает продвижению e4 и прямо гасит инициативу белых на королевском фланге. Не стоит забывать и о возможности контратаки чёрных на ферзевом фланге.",

 "This seemingly logical line of defense leads to complications almost immediately. There is much to be explored here, but from what has been played, White obtains an advantage in this variation.":
   "Логичная на вид защита почти сразу ведёт к осложнениям. Изучать тут есть что, но по сыгранным партиям белые в этом варианте получают перевес.",

 "This passive defense is tempting, and the aggressive player may well wish to attempt to break it open quickly, but it is not weak by any means and should be treated with respect.":
   "Пассивная защита выглядит соблазнительно для атакующего — хочется вскрыть её побыстрее. Но слабой она отнюдь не является, и относиться к ней надо уважительно.",

 "The black defenses are tied to a very precariously situated Knight, but White has to be careful because Black commands most of the board. C. Bloodgood- K. Stevens, 1960, continued":
   "Оборона чёрных держится на очень шатко стоящем коне, но белым надо быть осторожными: чёрные контролируют бо́льшую часть доски. Партия Бладгуд — Стивенс, 1960, продолжалась",

 "White has two sets of connected doubled pawns, which are serious threats in the center, e.g. two connected passed would not be easy for Black to cope with.":
   "У белых две пары связанных сдвоенных пешек — серьёзная сила в центре: с двумя связанными проходными чёрным пришлось бы туго.",

 "While there are several lines which are playable for Black at this point, there are also several which appear playable, but which lose. Clearly bad are:":
   "Играбельных продолжений у чёрных здесь несколько, но есть и такие, которые выглядят играбельными, а на деле проигрывают. Явно плохо:",

 "While 2 Bg2 d5 transposes to Part III, this defence generally brings about a radical difference in the basic motifs of attack. Several lines not recommended for White include:":
   "Хотя 2.Bg2 d5 переходит в часть III, эта защита обычно в корне меняет основные мотивы атаки. Белым не рекомендуются, в частности:",

 "Should the Grob become a popular opening, this defense will undoubtedly become a major line, but for the present it is still among the seldom played variations.":
   "Если Гроб когда-нибудь войдёт в моду, эта защита наверняка станет основной. Пока же она остаётся среди редко играемых.",

 "This passive defense is tempting, and the aggressive player may well wish to attempt to break it open quickly, but it is not weak by any means and should be treated with respect. ":
   "Пассивная защита выглядит соблазнительно, но слабой она не является.",

 "This counters the threat of g5 very effectively, and although this line has not been explored in any detail, the potential is definitely there.":
   "Очень действенно против угрозы g5. Линия толком не изучена, но потенциал у неё определённо есть.",

 "This variation differs from 3...c6 in that Black sacrifices some co-ordination of his pieces for more choice in which pawn he will return.":
   "От 3…c6 вариант отличается тем, что чёрные жертвуют слаженностью фигур ради выбора, какую пешку возвращать.",

 "with a winning advantage for Black. At this point, two important lines of defence are possible: Variation \"D2a\" 4...c6; and Variation \"D2b\" 4...Qd4.":
   "с решающим перевесом у чёрных. Здесь возможны две важные защиты: вариант «D2a» 4…c6 и вариант «D2b» 4…Qd4.",

 "(Braune-Rupprecht, 1956) The playable lines to be considered are: Variation \"E1\" 6...d5, Variation \"E2\" 6... Nc6, and Variation \"E3\" 6... e5!?":
   "(Брауне — Рупрехт, 1956) Рассматриваются играбельные линии: вариант «E1» 6…d5, вариант «E2» 6…Nc6 и вариант «E3» 6…e5!?",

 ", Black has a number of playable alternatives which for the most part have not been examined in any detail. While Part 4 will serve s a general guide for play against several of these, it is by no means definitive. Variation A3 covers 2...e6 and Variation B3 covers other second moves for Black.":
   ", у чёрных есть ряд играбельных продолжений, по большей части толком не разобранных. Часть 4 даёт общий ориентир против некоторых из них, но исчерпывающей её не назовёшь. Вариант A3 — про 2…e6, вариант B3 — про остальные вторые ходы чёрных.",

 "0-1 Grob, H-Bucher,R/corr 1966 (22) and White not only loses his attack, but also has the worse of the position. The text move is clearly best, and now Black can lose quickly with several seemingly playable moves, but also has several interesting and highly complex lines that are probably good.":
   "0-1 Grob,H-Bucher,R/corr 1966 (22) и белые не только теряют атаку, но и получают худшую позицию. Ход в тексте явно сильнейший; теперь чёрные могут быстро проиграть несколькими вроде бы играбельными ходами, но есть у них и несколько интересных, очень сложных и, вероятно, хороших линий.",

 "1-0 Bloodgood,C-Sokel,S/Norfolk 1959 (13) , after which White won because of his opponent's blunder, but Black clearly has the best of this. Improvements on White's 10th and 12th moves are probable.":
   "1-0 Bloodgood,C-Sokel,S/Norfolk 1959 (13) — белые выиграли из-за зевка соперника, но у чёрных тут явно лучше. На 10-м и 12-м ходах белые, вероятно, могут сыграть сильнее.",
})

PHRASES = [
 (r"with a winning advantage for White\.?", "с решающим перевесом у белых."),
 (r"with a winning advantage to White\.?", "с решающим перевесом у белых."),
 (r"with a winning advantage for Black\.?", "с решающим перевесом у чёрных."),
 (r"with a winning advantage to Black\.?", "с решающим перевесом у чёрных."),
 (r"with a winning advantage\.?", "с решающим перевесом."),
 (r"with a solid advantage for White\.?", "с прочным перевесом у белых."),
 (r"with a solid advantage to White\.?", "с прочным перевесом у белых."),
 (r"with a solid advantage to Black\.?", "с прочным перевесом у чёрных."),
 (r"with solid advantage to Black\.?", "с прочным перевесом у чёрных."),
 (r"with strong advantage to Black\.?", "с сильным перевесом у чёрных."),
 (r"with some advantage for White\.?", "с некоторым перевесом у белых."),
 (r"with some advantage to White\.?", "с некоторым перевесом у белых."),
 (r"with some advantage for Black\.?", "с некоторым перевесом у чёрных."),
 (r"with some advantage to Black\.?", "с некоторым перевесом у чёрных."),
 (r"with a material advantage\.?", "с материальным перевесом."),
 (r"with material advantage;?", "с материальным перевесом;"),
 (r"with advantage for White\.?", "с перевесом у белых."),
 (r"with advantage to White\.?", "с перевесом у белых."),
 (r"with advantage for white\.?", "с перевесом у белых."),
 (r"with advantage for Black\.?", "с перевесом у чёрных."),
 (r"with advantage to Black\.?", "с перевесом у чёрных."),
 (r"with advantage in an error-filled game\.?", "с перевесом в партии, полной ошибок."),
 (r"with advantage\.?", "с перевесом."),
 (r"and White has a pawn with a better position\.?", "и у белых пешка и позиция получше."),
 (r"and White has the initiative\.?", "и инициатива у белых."),
 (r"and White wins a piece\.?", "и белые выигрывают фигуру."),
 (r"and White wins the piece\.?", "и белые выигрывают фигуру."),
 (r"and White won in 53 moves\.?", "и белые выиграли на 53-м ходу."),
 (r"and the White Queen is trapped\.?", "и белый ферзь пойман."),
 (r"and the Black Queen falls;?", "и чёрный ферзь гибнет;"),
 (r"and the Queen is trapped\.?", "и ферзь пойман."),
 (r"And White loses the Bishop", "И белые теряют слона"),
 (r"and Black has the advantage;?", "и перевес у чёрных;"),
 (r"and Black has an attack\.?", "и у чёрных атака."),
 (r"and Black stands better\. White can improve this!",
  "и чёрные стоят лучше. Белые могут сыграть сильнее!"),
 (r"and Black loses quickly,", "и чёрные быстро проигрывают,"),
 (r"and Black won\b", "и чёрные выиграли"),
 (r"and White stands a little better\.?", "и белые стоят чуть лучше."),
 (r"and while White has slightly the better position, its meaning is wasted\.?",
  "и хотя у белых чуть лучше, толку от этого нет."),
 (r"and despite the draw result, Black stands decidedly better\.?",
  "и, несмотря на ничью, чёрные стоят заметно лучше."),
 (r"but White already had a considerable advantage\.?", "но у белых уже был солидный перевес."),
 (r"at which point Black can play", "и здесь чёрные могут сыграть"),
 (r"at which point Black played", "и здесь чёрные сыграли"),
 (r"where White's advantage is due to Black's weak play\.?",
  "где перевес белых — следствие слабой игры чёрных."),
 (r"with Black having much the better of this\.?", "и у чёрных заметно лучше."),
 (r"with Black having nothing for the pawn\.?", "и у чёрных нет компенсации за пешку."),
 (r"with White having much the better position\.?", "и у белых заметно лучшая позиция."),
 (r"with White having the better position\.?", "и у белых позиция получше."),
 (r"with White having some threats;?", "у белых есть угрозы;"),
 (r"with White standing much the better;?", "белые стоят заметно лучше;"),
 (r"with White standing better\.*", "белые стоят лучше."),
 (r"with White struggling to hold equality\.?", "белым с трудом удаётся удержать равенство."),
 (r"with White a pawn up\.?", "белые с лишней пешкой."),
 (r"with Black standing better\.?", "чёрные стоят лучше."),
 (r"with Black equalizing\.?", "чёрные уравнивают."),
 (r"with Black simply trading", "чёрные просто меняются"),
 (r"with Black winning in 33\.?", "чёрные выиграли на 33-м ходу."),
 (r"with Black threatening Qxc1 mate and Qxh1\)", "чёрные грозят Qxc1 матом и Qxh1)"),
 (r"with complications favoring Black", "с осложнениями в пользу чёрных"),
 (r"with double-edged complications;?", "с обоюдоострыми осложнениями;"),
 (r"with a sharp position that is very double-edged\.?",
  "с острой и очень обоюдоострой позицией."),
 (r"with an easy endgame win for White\.?", "с лёгким выигрышем в эндшпиле за белых."),
 (r"with an easy engame win\.?", "с лёгким выигрышем в эндшпиле."),
 (r"with an easy win for White\.?", "с лёгким выигрышем за белых."),
 (r"with an easy win- H\. Grob\.?", "с лёгким выигрышем — Гроб."),
 (r"with an easy win\.?", "с лёгким выигрышем."),
 (r"with a quick win for White\.?", "с быстрым выигрышем за белых."),
 (r"with a winning position\.?", "с выигранной позицией."),
 (r"with a winning attack\.?", "с выигрывающей атакой."),
 (r"with a strong attack\.?", "с сильной атакой."),
 (r"with a mating attack", "с матовой атакой"),
 (r"with a sharp attack", "с острой атакой"),
 (r"with a pawn and the attack\.?", "с пешкой и атакой."),
 (r"with a good position;?", "с хорошей позицией;"),
 (r"with a drawish position;?", "с ничейной позицией;"),
 (r"with an unclear position\.?", "с неясной позицией."),
 (r"with an attack;?", "с атакой;"),
 (r"with strong attack\.?", "с сильной атакой."),
 (r"with winning chances", "с шансами на выигрыш"),
 (r"with about equal chances", "примерно с равными шансами"),
 (r"with equal chances", "с равными шансами"),
 (r"with counterchances;?", "с контршансами;"),
 (r"with counter play\.?", "с контригрой."),
 (r"with counterplay\.?", "с контригрой."),
 (r"with mounting pressure\.?", "с нарастающим давлением."),
 (r"with initiative for Black\.?", "с инициативой у чёрных."),
 (r"with initiative", "с инициативой"),
 (r"with equality;?", "с равенством;"),
 (r"with equality\.?", "с равенством."),
 (r"with threats;?", "с угрозами;"),
 (r"with good play", "при хорошей игре"),
 (r"with the Queen lost\.?", "с потерей ферзя."),
 (r"with the N at g4 hanging", "и конь на g4 повисает"),
 (r"with a tactical finish;?", "с тактической концовкой;"),
 (r"winning the d-pawn\.?", "выигрывая пешку d."),
 (r"threatening Bf4 followed by Nd6\+ and Re1 and White wins easily\.?",
  "с угрозой Bf4, затем Nd6+ и Re1, и белые легко выигрывают."),
 (r"White has a clear advantage\.?", "У белых явный перевес."),
 (r"White has an advantage\.?", "У белых перевес."),
 (r"White has the better chances!", "У белых шансы лучше!"),
 (r"White has a strong attack!", "У белых сильная атака!"),
 (r"The position is not clear\.?", "Позиция не ясна."),
 (r"Black has lost a tempo", "Чёрные потеряли темп"),
 (r"Black Resigned\.?", "чёрные сдались."),
 (r"Black resigned\.?", "чёрные сдались."),
 (r"White resigned\.?", "белые сдались."),
 (r"Queen moves lose", "ходы ферзём проигрывают"),
 (r"Any 13 Nb5 traps the Queen\.?", "Любое 13.Nb5 ловит ферзя."),
 (r"10\. Bxf7 is not good\.?", "10.Bxf7 нехорошо."),
 (r"or 12\.\.\. Bc8", "или 12…Bc8"),
 (r"and 7 Qxc4 next", "и затем 7.Qxc4"),
 (r"with 8\. QxB next", "и затем 8.Q:B"),
 (r"with 17\. f3 following", "с последующим 17.f3"),
 (r"with 0-0 next\.?", "и затем 0-0."),
 (r"with \.\.\.Nb6- Nd5 following", "с последующим …Nb6-Nd5"),
 (r"followed by Bb2\.?", "с последующим Bb2."),
 (r"followed by", "с последующим"),
 (r"is Black's best chance", "— лучший шанс чёрных"),
 (r"was Black's only chance", "— единственный шанс чёрных"),
 (r"is better for Black", "лучше для чёрных"),
 (r"is better for White", "лучше для белых"),
 (r"is not as good for Black\.?", "для чёрных не так хорошо."),
 (r"is good for White\.?", "хорошо для белых."),
 (r"is good for equality,?", "годится для уравнения,"),
 (r"is less complicated\.?", "проще."),
 (r"is another example\.?", "— ещё один пример."),
 (r"is suggested by Bloodgood", "предлагает Бладгуд"),
 (r"is suggested by Grob,?", "предлагает Гроб,"),
 (r"is recommended by Grob", "рекомендует Гроб"),
 (r"is worth a try", "стоит попробовать"),
 (r"is worth trying\.?", "стоит попробовать."),
 (r"is not good,?", "нехорошо,"),
 (r"is no better", "не лучше"),
 (r"is also good\.?", "тоже хорошо."),
 (r"is unclear\.?", "неясно."),
 (r"is sharper,?", "острее,"),
 (r"is safer", "надёжнее"),
 (r"is risky, e\.g\.", "рискованно, например"),
 (r"this is risky!", "это рискованно!"),
 (r"is the best", "сильнейшее"),
 (r"is better,?", "лучше"),
 (r"is best", "сильнейшее"),
 (r"may be as good, but", "возможно, не хуже, но"),
 (r"may be better", "возможно, лучше"),
 (r"was better;?", "было лучше;"),
 (r"was best\.?", "было сильнейшим."),
 (r"leaves much to be desired\.?", "оставляет желать лучшего."),
 (r"creates some problems\.?", "создаёт некоторые проблемы."),
 (r"appears to favor White", "выглядит в пользу белых"),
 (r"favors White also\.?", "тоже в пользу белых."),
 (r"favors White;?", "в пользу белых;"),
 (r"favors White\.?", "в пользу белых."),
 (r"favors [Bb]lack;?", "в пользу чёрных;"),
 (r"favors Black\.?", "в пользу чёрных."),
 (r"in Black's favor\.?", "в пользу чёрных."),
 (r"in White's favor\.?", "в пользу белых."),
 (r"wins for White\.?", "выигрывает за белых."),
 (r"wins for Black;?", "выигрывает за чёрных;"),
 (r"winning a piece;?", "выигрывая фигуру;"),
 (r"and White wins a piece", "и белые выигрывают фигуру"),
 (r"transposes to Part 1\.?", "с перестановкой в часть 1."),
 (r"transposes to Part II\.?", "с перестановкой в часть II."),
 (r"transposes to Grob-Spichtig,?", "с перестановкой в партию Гроб — Шпихтиг,"),
 (r"transposes\.?", "с перестановкой ходов."),
 (r"where Black can then play", "и здесь чёрные могут сыграть"),
 (r"when Black replies", "на что чёрные отвечают"),
 (r"in this line\.?", "в этой линии."),
 (r"as in previous note", "как в предыдущем примечании"),
 (r"A line of note continues", "Заслуживающая внимания линия продолжается"),
 (r"The playable lines are:", "Играбельные линии:"),
 (r"\(Blocking in the King-bishop\)", "(запирая королевского слона)"),
 (r"\( a costly \"gift\"\)", "(дорогой «подарок»)"),
 (r"\(16 g5 and 18 Nxe7!\? are suspect!\)", "(16.g5 и 18.N:e7!? сомнительны!)"),
 (r"unsound!", "некорректно!"),
 (r"and now:", "и теперь:"),
 (r"and if", "а если"),
 (r"After\b", "После"),
 (r"\bwins\.?", "выигрывает."),
 (r"\bnext\b", "далее"),
 (r"\bor\b", "или"),
 (r"\bwhen\b", "когда"),
 (r"\bwith\b", "с"),
 (r"etc\.?", "и т.д."),
 (r"analysis by H\. Grob\.?", "анализ Гроба."),
 (r"regaining the piece", "отыгрывая фигуру"),
 (r"analysis by Grob\.?", "анализ Гроба."),
 (r"with an advantage for White", "с перевесом у белых"),
 (r"regaining the piece with attack;?", "отыгрывая фигуру с атакой;"),
 (r"White has a solid advantage\.?", "у белых прочный перевес."),
 (r"with Black quite cramped;?", "у чёрных весьма тесно;"),
 (r"which depends on Black errors\.?", "что зависит от ошибок чёрных."),
 (r"with open play for both sides", "с открытой игрой для обеих сторон"),
 (r"which offers White no more than equality\.?", "что даёт белым не больше равенства."),
 (r"leaving Black with tripled isolated pawns", "оставляя чёрных со строенными изолированными пешками"),
 (r"\(This is better than an immediate ([^)]+)\)", r"(Это лучше немедленного \1)"),
 (r"This is decidedly inferior to ([\d.]+\w*)\.?", r"Это заметно слабее, чем \1."),
 (r"'?the Black King needs a little room\.?'?", "«чёрному королю нужен воздух»."),
 (r"White clearly has the better chances\.?", "У белых явно лучшие шансы."),
 (r"with ample compensation for the pawn\.?", "с достаточной компенсацией за пешку."),
 (r"This position is quite double edged!", "Позиция весьма обоюдоострая!"),
 (r"with an immediate advantage to Black", "с немедленным перевесом у чёрных"),
 (r"where Black has less than equality\.?", "где у чёрных меньше равенства."),
 (r"The second tempo lost in this game!", "Второй потерянный темп в этой партии!"),
 (r"This is the only aggressive reply\.?", "Единственный агрессивный ответ."),
 (r"with an advantage to White", "с перевесом у белых"),
 (r"with some advantage;", "с некоторым перевесом;"),
 (r"winning the a-pawn", "выигрывая пешку a"),
 (r"\(This\b", "(Это"),
 (r"\bthe position\b", "позиция"),
 (r"\s+to White\.\s*$", ""),
 (r"\bUnknown\b", "неизвестный"),
 (r"leaving Black facing the inevitable Queenside pawn onslaught",
  "оставляя чёрных перед неизбежным пешечным наступлением на ферзевом фланге"),
 (r"the White Queen trapped", "белый ферзь пойман"),
 (r"as it opens lines to the Black King", "так как вскрывает линии к чёрному королю"),
 (r"where Black can contest the king's side more actively\.?",
  "где чёрные могут активнее бороться за королевский фланг."),
 (r"White has some advantage, but this is very minimal\.?",
  "У белых некоторый перевес, но совсем незначительный."),
 (r"This is not very effective, and is not recommeded\.?",
  "Не слишком действенно и не рекомендуется."),
 (r"White obtains a lasting advantage", "белые получают устойчивый перевес"),
 (r"This line is the weakest of the three", "Эта линия — слабейшая из трёх"),
 (r"and even then, Black has the initiative", "и даже тогда инициатива у чёрных"),
 (r"offering the pawn for an open Rook-file", "отдавая пешку за открытую ладейную линию"),
 (r"and Black has no compensation for the Knight\.?",
  "и у чёрных нет компенсации за коня."),
 (r"\(unfortunately there is no Queen trap here\)",
  "(к сожалению, ловушки на ферзя здесь нет)"),
 (r"This is definitely not a gambit pawn", "Это определённо не гамбитная пешка"),
 (r"This move seems sharper than it is", "Ход кажется острее, чем есть на деле"),
 (r"to White\.\s*$", ""),
 (r"Black resigns\.?", "чёрные сдались."),
 (r"White resigns\.?", "белые сдались."),
 (r"\bcorrespondence\b", "по переписке"),
 (r"\bcont\.", "продолжение:"),
 (r"according to", "по мнению"),
 (r"White maintaining the pressure on Black's d-pawn",
  "белые сохраняют давление на пешку d чёрных"),
 (r"White having better endgame prospects", "у белых лучше перспективы в эндшпиле"),
 (r"Black losing a pawn in a pressure position\.?", "чёрные теряют пешку в стеснённой позиции."),
 (r"the e-pawn held to support White's center pawns\.?",
  "пешка e держится и поддерживает центральные пешки белых."),
 (r"White regaining the rook,?", "белые отыгрывают ладью,"),
 (r"breaks the white pawn center to White's disadvantage",
  "разбивает белый пешечный центр во вред самим белым"),
 (r"some attack for the pawn\.?", "некоторая атака за пешку."),
 (r"and White is down a pawn", "и белые без пешки"),
 (r"White has little for the two pawns\.?", "У белых мало компенсации за две пешки."),
 (r"a drawish position;?", "ничейная позиция;"),
 (r"a solid advantage", "прочный перевес"),
 (r"\(answering the threat ([^)]+)\)", r"(парируя угрозу \1)"),
 (r"after which:", "после чего:"),
 (r"some initiative for White\.?", "некоторая инициатива у белых."),
 (r"from his postal play", "из его игры по переписке"),
 (r"This is definitely not recommended!", "Так играть точно не советую!"),
 (r"Where White gains a solid advantage\.?", "Белые получают прочный перевес."),
 (r"\bthreatening\b", "с угрозой"),
 (r"\battack\b", "атака"),
 (r"\bwhich\b", "что"),
 (r"\bdefinitely\b", "определённо"),
 (r"\band\b", "и"),
 (r"\bfor Black\b", "за чёрных"),
 (r"\bfor White\b", "за белых"),
 (r"with White winning a R for B\)", "белые выигрывают ладью за слона)"),
 (r"and the white queen cannot be taken because of", "и белого ферзя брать нельзя из-за"),
 (r"and the white Queen is trapped, e\.g\. if", "и белый ферзь пойман, например при"),
 (r"and the White queen is lost или White is mated",
  "и белый ферзь теряется либо белым мат"),
 (r"and the White queen is lost or White is mated",
  "и белый ферзь теряется либо белым мат"),
 (r"come several lines of interest", "идут несколько интересных линий"),
 (r"relieves some of the pressure on Black", "снимает часть давления с чёрных"),
 (r"is not as good as the text because it allows",
  "не так хорошо, как ход в тексте, потому что допускает"),
 (r"Black has better moves\b", "У чёрных есть ходы получше"),
 (r"White has much the better of this\.?", "У белых заметно лучше."),
 (r"White has a distinct advantage", "У белых явный перевес"),
 (r"Black now gets good counterplay", "теперь у чёрных хорошая контригра"),
 (r"Black getting some counterplay", "чёрные получают некоторую контригру"),
 (r"against both Black's b7 pawn and f7 pawn", "против обеих пешек чёрных, b7 и f7"),
 (r"avoiding the queen trade would have been better",
  "уклониться от размена ферзей было лучше"),
 (r"delaying Blacks? KB development", "задерживая развитие королевского слона чёрных"),
 (r"mate threatened if the White queen moves\.?", "угроза мата, если белый ферзь уйдёт."),
 (r"and Black threatens mate if the queen moves", "и чёрные грозят матом, если ферзь уйдёт"),
 (r"Black can't afford this!", "Чёрным это не по карману!"),
 (r"'See ([^,]+), Variation \"([A-Z0-9]+)\", for ([^']+)\.'",
  r"См. \1, вариант «\2», о \3."),
 (r"transposes into Variation", "с перестановкой в вариант"),
 (r"transposes to Variation", "с перестановкой в вариант"),
 (r"\bVariation\b", "вариант"),
 (r"\bPart\b", "часть"),
 (r"if ", "если "),
 (r"Black has better moves in this line\.?", "У чёрных в этой линии есть ходы получше."),
 (r"[-;]\s*H\. Grob\.?", " — Гроб."),
 (r"[-;]\s*Grob\.?", " — Гроб."),
 (r"\bH\. Gro[bp]\b(?![,\-])", "Гроб"),
 (r"\bGrob\b(?![,\-])", "Гроб"),
 (r"\bBloodgood\b(?![,\-])", "Бладгуд"),
]
PHRASES.sort(key=lambda pr: -len(pr[0]))
PHRASES = [(re.compile(p, re.IGNORECASE), r) for p, r in PHRASES]

# ссылка на партию: результат, имена, турнир, год, число ходов
CITE = re.compile(r"^(1-0|0-1|1/2-1/2|½-½)\s+(.+?\(\d+\))\s*(.*)$", re.S)


def ru(text):
    """Комментарий -> русский. Ссылки на партии остаются как есть."""
    t = " ".join(str(text).split()).strip()
    if not t:
        return ""
    if t in EXACT:
        return EXACT[t]

    head = ""
    m = CITE.match(t)
    if m:
        head, t = f"{m.group(1)} {m.group(2)} ", m.group(3)
        if t in EXACT:
            return head + EXACT[t]

    for pat, sub in PHRASES:
        t = pat.sub(sub, t)
    t = re.sub(r"\s+([,.;:])", r"\1", t).strip()
    t = re.sub(r"\.\s*\.", ".", t)
    t = re.sub(r"\.\s*([;,])", r"", t)
    if t and not head and text[:1].isupper() and t[:1].islower():
        t = t[0].upper() + t[1:]
    return (head + t).strip()


# Английскую прозу узнаём по строчным словам: имена, турниры и ходы пишутся с большой
# буквы или короткие, и латиницей остаются законно.
PROSE = re.compile(r"\b[a-z]{3,}\b")
CAPS_EN = {"This", "The", "There", "White", "Black", "After", "While", "Several",
           "Perhaps", "Simply", "From", "Any", "Queen", "King", "Knight", "Bishop",
           "Rook", "Pawn", "And", "But", "With", "Of"}
SAN = re.compile(r"^(corr|etc|www)$")


if __name__ == "__main__":
    import sys, io as _io, chess.pgn
    src = sys.argv[1] if len(sys.argv) > 1 else "books/tactical_grob.pgn"
    f = _io.open(src, encoding="utf-8", errors="replace")
    left, total = [], 0
    while True:
        g = chess.pgn.read_game(f)
        if g is None:
            break
        w = g.headers.get("White", "?").replace('\\"', '"')
        if "Variation" not in w and w != "?":
            break
        if not g.variations:
            continue
        st = [g]
        while st:
            nd = st.pop()
            t = " ".join(nd.comment.split()).replace("$", "").strip()
            if t:
                total += 1
                out = ru(t)
                bad = [x for x in PROSE.findall(out) if not SAN.match(x)]
                bad += [x for x in re.findall(r"\b[A-Z][a-z]{2,}\b", out) if x in CAPS_EN]
                if bad:
                    left.append((sorted(set(bad))[:5], out[:110]))
            st.extend(nd.variations)
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"комментариев: {total} | с непереведёнными словами: {len(left)}")
    for words, sample in left[:40]:
        print(f"  {','.join(words):38} | {sample}")
