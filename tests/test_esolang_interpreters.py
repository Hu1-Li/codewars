# coding=utf-8
import unittest
from solutions.esolang_interpreters_v1 import my_first_interpreter as interpreter_v1
from solutions.esolang_lnterpreters_v2 import interpreter as interpreter_v2
from solutions.esolang_lnterpreters_v3 import interpreter as interpreter_v3
from solutions.esolang_lnterpreters_v4 import boolfuck


class MostFreqWordsTestCase(unittest.TestCase):
    def test_v1(self):
        solution = interpreter_v1
        self.assertEqual(
            solution(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
            ),
            "Hello, World!",
        )
        self.assertEqual(
            solution(
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+."
            ),
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )

    def test_v2(self):
        interpreter = interpreter_v2
        # Flips the leftmost cell of the tape
        self.assertEqual(interpreter("*", "00101100"), "10101100")
        # Flips the second and third cell of the tape
        self.assertEqual(interpreter(">*>*", "00101100"), "01001100")
        # Flips all the bits in the tape
        self.assertEqual(interpreter("*>*>*>*>*>*>*>*", "00101100"), "11010011")
        # Flips all the bits that are initialized to 0
        self.assertEqual(interpreter("*>*>>*>>>*>*", "00101100"), "11111111")
        # Goes somewhere to the right of the tape and then flips all bits that are initialized to 1, progressing leftwards through the tape
        self.assertEqual(interpreter(">>>>>*<*<<*", "00101100"), "00000000")
        # ignore non-op
        self.assertEqual(interpreter("abc", "00000000"), "00000000")
        # with []
        self.assertEqual(interpreter(">*>*[*<]", "00000000"), "00000000")

    def test_v3(self):
        interpreter = interpreter_v3
        self.assertEqual(
            interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9),
            "000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000",
            "Your interpreter should initialize all cells in the datagrid to 0",
        )
        self.assertEqual(
            interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 7, 6, 9),
            "111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000",
            "Your interpreter should adhere to the number of iterations specified",
        )
        self.assertEqual(
            interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 19, 6, 9),
            "111100\r\n000010\r\n000001\r\n000010\r\n000100\r\n000000\r\n000000\r\n000000\r\n000000",
            "Your interpreter should traverse the 2D datagrid correctly",
        )
        self.assertEqual(
            interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 42, 6, 9),
            "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000",
            'Your interpreter should traverse the 2D datagrid correctly for all of the "n", "e", "s" and "w" commands',
        )
        self.assertEqual(
            interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 100, 6, 9),
            "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000",
            "Your interpreter should terminate normally and return a representation of the final state of the 2D datagrid when all commands have been considered from left to right even if the number of iterations specified have not been fully performed",
        )

        # print(interpreter("eee*s*s*s*w*w*w*w*w*w*w*n*n*n*n*n*n*n*n*n*e*e*e*e*e*e*e*s*s*s*s*s*", 1000, 8, 10))
        # print(interpreter("*eesws*we*wwennswnnnenss**wse**eews*esn*wn*newww*w*n*nnnwe**ewwnwenns*snn*e*wns***nnenn*sss*s*wenne*wn**we*wnw*ee**w*ee**nnse*wss*nsw*sneenesnsseewswsn*ene*enesewse*ewwssen*wwwsnwnnww*eeneneswws*nw*s*n**wen*ensswswwe*wes*wswse*ssnes*s*e*sws*nnenwsns*w*eessn*ssnenws*nwse*nessee*ssen*wwe*snewwssnsseweneewnw*en*eew*sssewne*wnnwes*ne*w*we*n*sweeneeeeew***eewsswsss**neewwwsnwnw*ee*e*snsnnww*n*nwewnwewsew*ee*esesne*ess*nnwsswnw*ens**sse*swnees*nssen*e*s*s**s*wen", 594, 10, 10))
        # print(interpreter("*[[s*en]sw[w]enn[[e]w*ssss*nnnnw[w]ess[e]*[w]enn]ssss[*nnnn*essss]nnnnw[w]ess]", 1000, 100, 100))

    def test_v4(self):
        self.assertEqual(
            boolfuck(";"),
            "\u0000",
        )
        self.assertEqual(
            boolfuck(
                ";;;+;+;;+;+;+;+;+;+;;+;;+;;;+;;+;+;;+;;;+;;+;+;;+;+;;;;+;+;;+;;;+;;+;+;+;;;;;;;+;+;;+;;;+;+;;;+;+;;;;+;+;;+;;+;+;;+;;;+;;;+;;+;+;;+;;;+;+;;+;;+;+;+;;;;+;+;;;+;+;+;",
                "",
            ),
            "Hello, world!\n",
        )
        self.assertEqual(
            boolfuck(
                ">,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>;>;>;>;>;>;>;>;>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]",
                "Codewars",
            ),
            "Codewars",
        )
        self.assertEqual(
            boolfuck(
                ">,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<;>;>;>;>;>;>;>;<<<<<<<,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]",
                "Codewars\u00ff",
            ),
            "Codewars",
        )

        self.assertEqual(
            boolfuck(
                ">,>,>,>,>,>,>,>,>>,>,>,>,>,>,>,>,<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]>[>]+<[+<]>>>>>>>>>[+]>[>]+<[+<]>>>>>>>>>[+]<<<<<<<<<<<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>>>>>>>>>>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<<<<<<<<<<<<<<<<<<<[>]+<[+<]>>>>>>>>>[+]>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]<<<<<<<<<<<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>>>>>>>>>>>>>>>>>>>;>;>;>;>;>;>;>;<<<<<<<<",
                "\u0008\u0009",
            ),
            "\u0048",
        )
