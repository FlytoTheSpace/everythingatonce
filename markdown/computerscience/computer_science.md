
# Programming

**Markdown** (new Format):

- [`C`](./c.md)
- [`Shell (CMD, Bash)`](./shell.md)

**Text** (original, deprecated):

- [`C`](./c.txt)
- [`CSS`](./CSS.txt)
- [`DataBases`](./DataBases.txt)
- [`Docker`](./docker.txt)
- [`Git`](./git.txt)
- [`Hacking`](./hacking.txt)
- [`HTML`](./HTML.txt)
- [`JavaScript`](./JavaScript.txt)
- [`Python`](./python.txt)
- [`Shell (CMD, Bash)`](./shell.txt)
- [`TypeScript`](./TypeScript.txt)

# Network

- [`Network`](./network.md) (markdown)
- [`Network`](./network.txt) (text)

# Hacking

- [`Hacking`](./hacking.md) (markdown)
- [`Hacking`](./hacking.txt) (text)

# Data Structures

## Array-Like

| **Data Structure** | **Definition**                                          | **Ordered** | **Mutable** | **Indexed** | **Duplicates** | **Key Operations**                  | Space Time |
| ------------------ | ------------------------------------------------------- | ----------- | ----------- | ----------- | -------------- |------------------------------------ | ---------- |
| **Array**          | Fixed-size collection of elements of the same type.     | ✅         | ❌          | ✅         | ✅             | `Access`, `Update`, `Delete`        | $O(1)$     |
| **List**           | Dynamic-size collection of elements.                    | ✅         | ✅          | ✅         | ✅             | `Append`, `Pop`, `Insert`, `Access` | $O(1)$     |
| **Tuple**          | Immutable collection of elements.                       | ✅         | ❌          | ✅         | ✅             | `Access`                            | $O(1)$     |
| **Set**            | Unordered collection of unique elements.                | ❌         | ✅          | ❌         | ❌             | `Add`, `Remove`, `Check Membership` | $O(1)$     |
| **Queue**          | FIFO (First In First Out) collection.                   | ✅         | ✅          | ❌         | ❌             | `Enqueue`, `Dequeue`, `Front`       | $O(1)$     |
| **Stack**          | LIFO (Last In First Out) collection.                    | ✅         | ✅          | ❌         | ❌             | `Push`, `Pop`, `Top`                | $O(1)$     |
| **Linked List**    | Collection of nodes where each node points to the next. | ✅         | ✅          | ❌         | ✅             | `Add` `Node`, `Remove Node`         | $O(n)$     |


# ASCII Table
## Unprintable

| DEC | OCT | HEX | BIN      | SYM | HTML-UM | HTML-NAME |   DESCRIPTION  |
| --- | --- | --- | -------- | --- | ------- | --------- | -------------- |
| 0   | 000 | 00  | 00000000 | NUL | \&#00;  |           | Null character |
| 1   | 001 | 01  | 00000001 | SOH | \&#01;  |           | Start of Heading |
| 2   | 002 | 02  | 00000010 | STX | \&#02;  |           | Start of Text |
| 3   | 003 | 03  | 00000011 | ETX | \&#03;  |           | End of Text |
| 4   | 004 | 04  | 00000100 | EOT | \&#04;  |           | End of Transmission |
| 5   | 005 | 05  | 00000101 | ENQ | \&#05;  |           | Enquiry |
| 6   | 006 | 06  | 00000110 | ACK | \&#06;  |           | Acknowledge |
| 7   | 007 | 07  | 00000111 | BEL | \&#07;  |           | Bell, Alert |
| 8   | 010 | 08  | 00001000 | BS  | \&#08;  |           | Backspace |
| 9   | 011 | 09  | 00001001 | HT  | \&#09;  |           | Horizontal Tab |
| 10  | 012 | 0A  | 00001010 | LF  | \&#10;  |           | Line Feed |
| 11  | 013 | 0B  | 00001011 | VT  | \&#11;  |           | Vertical Tabulation |
| 12  | 014 | 0C  | 00001100 | FF  | \&#12;  |           | Form Feed |
| 13  | 015 | 0D  | 00001101 | CR  | \&#13;  |           | Carriage Return |
| 14  | 016 | 0E  | 00001110 | SO  | \&#14;  |           | Shift Out |
| 15  | 017 | 0F  | 00001111 | SI  | \&#15;  |           | Shift In |
| 16  | 020 | 10  | 00010000 | DLE | \&#16;  |           | Data Link Escape |
| 17  | 021 | 11  | 00010001 | DC1 | \&#17;  |           | Device Control One (XON) |
| 18  | 022 | 12  | 00010010 | DC2 | \&#18;  |           | Device Control Two |
| 19  | 023 | 13  | 00010011 | DC3 | \&#19;  |           | Device Control Three (XOFF) |
| 20  | 024 | 14  | 00010100 | DC4 | \&#20;  |           | Device Control Four |
| 21  | 025 | 15  | 00010101 | NAK | \&#21;  |           | Negative Acknowledge |
| 22  | 026 | 16  | 00010110 | SYN | \&#22;  |           | Synchronous Idle |
| 23  | 027 | 17  | 00010111 | ETB | \&#23;  |           | End of Transmission Block |
| 24  | 030 | 18  | 00011000 | CAN | \&#24;  |           | Cancel |
| 25  | 031 | 19  | 00011001 | EM  | \&#25;  |           | End of medium |
| 26  | 032 | 1A  | 00011010 | SUB | \&#26;  |           | Substitute |
| 27  | 033 | 1B  | 00011011 | ESC | \&#27;  |           | Escape |
| 28  | 034 | 1C  | 00011100 | FS  | \&#28;  |           | File Separator |
| 29  | 035 | 1D  | 00011101 | GS  | \&#29;  |           | Group Separator |
| 30  | 036 | 1E  | 00011110 | RS  | \&#30;  |           | Record Separator |
| 31  | 037 | 1F  | 00011111 | US  | \&#31;  |           | Unit Separator |

## Printable:
    
| DEC | OCT | HEX | BIN      | SYM  | HTML-UM | HTML-NAME | DESCRIPTION |
| --- | --- | --- | -------- | ---- | ------- | --------- | ---------------- |
| 32  | 040 | 20  | 00100000 | SP  	| \&#32;  |	 	      | Space |
| 33  | 041 | 21  | 00100001 | !   	| \&#33;  |	\&excl;	  | Exclamation mark |
| 34  | 042 | 22  | 00100010 | "   	| \&#34;  |	\&quot;	  | Double quotes (or speech marks) |
| 35  | 043 | 23  | 00100011 | #   	| \&#35;  |	\&num;	  | Number sign |
| 36  | 044 | 24  | 00100100 | $   	| \&#36;  |	\&dollar; | Dollar |
| 37  | 045 | 25  | 00100101 | %   	| \&#37;  |	\&percnt; | Per cent sign |
| 38  | 046 | 26  | 00100110 | &   	| \&#38;  |	\&amp;	  | Ampersand |
| 39  | 047 | 27  | 00100111 | '   	| \&#39;  |	\&apos;	  | Single quote |
| 40  | 050 | 28  | 00101000 | (   	| \&#40;  |	\&lparen; | Open parenthesis (or open bracket) |
| 41  | 051 | 29  | 00101001 | )   	| \&#41;  |	\&rparen; | Close parenthesis (or close bracket) |
| 42  | 052 | 2A  | 00101010 | *   	| \&#42;  |	\&ast;	  | Asterisk |
| 43  | 053 | 2B  | 00101011 | +   	| \&#43;  |	\&plus;	  | Plus |
| 44  | 054 | 2C  | 00101100 | ,   	| \&#44;  |	\&comma;  | Comma |
| 45  | 055 | 2D  | 00101101 | -   	| \&#45;  |	 	      | Hyphen-minus |
| 46  | 056 | 2E  | 00101110 | .   	| \&#46;  |	\&period; | Period, dot or full stop |
| 47  | 057 | 2F  | 00101111 | /   	| \&#47;  |	\&sol;	  | Slash or divide |
| 48  | 060 | 30  | 00110000 | 0   	| \&#48;  |	 	      | Zero |
| 49  | 061 | 31  | 00110001 | 1   	| \&#49;  |	 	      | One |
| 50  | 062 | 32  | 00110010 | 2   	| \&#50;  |	 	      | Two |
| 51  | 063 | 33  | 00110011 | 3   	| \&#51;  |	 	      | Three |
| 52  | 064 | 34  | 00110100 | 4   	| \&#52;  |	 	      | Four |
| 53  | 065 | 35  | 00110101 | 5   	| \&#53;  |	 	      | Five |
| 54  | 066 | 36  | 00110110 | 6   	| \&#54;  |	 	      | Six |
| 55  | 067 | 37  | 00110111 | 7   	| \&#55;  |	 	      | Seven |
| 56  | 070 | 38  | 00111000 | 8   	| \&#56;  |	 	      | Eight |
| 57  | 071 | 39  | 00111001 | 9   	| \&#57;  |	 	      | Nine |
| 58  | 072 | 3A  | 00111010 | :   	| \&#58;  |	\&colon;  | Colon |
| 59  | 073 | 3B  | 00111011 | ;   	| \&#59;  |	\&semi;	  | Semicolon |
| 60  | 074 | 3C  | 00111100 | <   	| \&#60;  |	\&lt;	  | Less than (or open angled bracket) |
| 61  | 075 | 3D  | 00111101 | =   	| \&#61;  |	\&equals; | Equals |
| 62  | 076 | 3E  | 00111110 | >   	| \&#62;  |	\&gt;	  | Greater than (or close angled bracket) |
| 63  | 077 | 3F  | 00111111 | ?   	| \&#63;  |	\&quest;  | Question mark |
| 64  | 100 | 40  | 01000000 | @   	| \&#64;  |	\&commat; | At sign |
| 65  | 101 | 41  | 01000001 | A   	| \&#65;  |	 	      | Uppercase A |
| 66  | 102 | 42  | 01000010 | B   	| \&#66;  |	 	      | Uppercase B |
| 67  | 103 | 43  | 01000011 | C   	| \&#67;  |	 	      | Uppercase C |
| 68  | 104 | 44  | 01000100 | D   	| \&#68;  |	 	      | Uppercase D |
| 69  | 105 | 45  | 01000101 | E   	| \&#69;  |	 	      | Uppercase E |
| 70  | 106 | 46  | 01000110 | F   	| \&#70;  |	 	      | Uppercase F |
| 71  | 107 | 47  | 01000111 | G   	| \&#71;  |	 	      | Uppercase G |
| 72  | 110 | 48  | 01001000 | H   	| \&#72;  |	 	      | Uppercase H |
| 73  | 111 | 49  | 01001001 | I   	| \&#73;  |	 	      | Uppercase I |
| 74  | 112 | 4A  | 01001010 | J   	| \&#74;  |	 	      | Uppercase J |
| 75  | 113 | 4B  | 01001011 | K   	| \&#75;  |	 	      | Uppercase K |
| 76  | 114 | 4C  | 01001100 | L   	| \&#76;  |	 	      | Uppercase L |
| 77  | 115 | 4D  | 01001101 | M   	| \&#77;  |	 	      | Uppercase M |
| 78  | 116 | 4E  | 01001110 | N   	| \&#78;  |	 	      | Uppercase N |
| 79  | 117 | 4F  | 01001111 | O   	| \&#79;  |	 	      | Uppercase O |
| 80  | 120 | 50  | 01010000 | P   	| \&#80;  |	 	      | Uppercase P |
| 81  | 121 | 51  | 01010001 | Q   	| \&#81;  |	 	      | Uppercase Q |
| 82  | 122 | 52  | 01010010 | R   	| \&#82;  |	 	      | Uppercase R |
| 83  | 123 | 53  | 01010011 | S   	| \&#83;  |	 	      | Uppercase S |
| 84  | 124 | 54  | 01010100 | T   	| \&#84;  |	 	      | Uppercase T |
| 85  | 125 | 55  | 01010101 | U   	| \&#85;  |	 	      | Uppercase U |
| 86  | 126 | 56  | 01010110 | V   	| \&#86;  |	 	      | Uppercase V |
| 87  | 127 | 57  | 01010111 | W   	| \&#87;  |	 	      | Uppercase W |
| 88  | 130 | 58  | 01011000 | X   	| \&#88;  |	 	      | Uppercase X |
| 89  | 131 | 59  | 01011001 | Y   	| \&#89;  |	 	      | Uppercase Y |
| 90  | 132 | 5A  | 01011010 | Z   	| \&#90;  |	 	      | Uppercase Z |
| 91  | 133 | 5B  | 01011011 | [   	| \&#91;  |	\&lsqb;	  | Opening bracket |
| 92  | 134 | 5C  | 01011100 | \   	| \&#92;  |	\&bsol;	  | Backslash |
| 93  | 135 | 5D  | 01011101 | ]   	| \&#93;  |	\&rsqb;	  | Closing bracket |
| 94  | 136 | 5E  | 01011110 | ^   	| \&#94;  |	\&Hat;	  | Caret - circumflex |
| 95  | 137 | 5F  | 01011111 | _   	| \&#95;  |	\&lowbar; | derscore |
| 96  | 140 | 60  | 01100000 | `   	| \&#96;  |	\&grave;  | Grave accent |
| 97  | 141 | 61  | 01100001 | a   	| \&#97;  |	 	      | Lowercase a |
| 98  | 142 | 62  | 01100010 | b   	| \&#98;  |	 	      | Lowercase b |
| 99  | 143 | 63  | 01100011 | c   	| \&#99;  |	 	      | Lowercase c |
| 100 | 144 | 64  | 01100100 | d   	| \&#100; |	 	      | Lowercase d |
| 101 | 145 | 65  | 01100101 | e   	| \&#101; |	 	      | Lowercase e |
| 102 | 146 | 66  | 01100110 | f   	| \&#102; |	 	      | Lowercase f |
| 103 | 147 | 67  | 01100111 | g   	| \&#103; |	 	      | Lowercase g |
| 104 | 150 | 68  | 01101000 | h   	| \&#104; |	 	      | Lowercase h |
| 105 | 151 | 69  | 01101001 | i   	| \&#105; |	 	      | Lowercase i |
| 106 | 152 | 6A  | 01101010 | j   	| \&#106; |	 	      | Lowercase j |
| 107 | 153 | 6B  | 01101011 | k   	| \&#107; |	 	      | Lowercase k |
| 108 | 154 | 6C  | 01101100 | l   	| \&#108; |	 	      | Lowercase l |
| 109 | 155 | 6D  | 01101101 | m   	| \&#109; |	 	      | Lowercase m |
| 110 | 156 | 6E  | 01101110 | n   	| \&#110; |	 	      | Lowercase n |
| 111 | 157 | 6F  | 01101111 | o   	| \&#111; |	 	      | Lowercase o |
| 112 | 160 | 70  | 01110000 | p   	| \&#112; |	 	      | Lowercase p |
| 113 | 161 | 71  | 01110001 | q   	| \&#113; |	 	      | Lowercase q |
| 114 | 162 | 72  | 01110010 | r   	| \&#114; |	 	      | Lowercase r |
| 115 | 163 | 73  | 01110011 | s   	| \&#115; |	 	      | Lowercase s |
| 116 | 164 | 74  | 01110100 | t   	| \&#116; |	 	      | Lowercase t |
| 117 | 165 | 75  | 01110101 | u   	| \&#117; |	 	      | Lowercase u |
| 118 | 166 | 76  | 01110110 | v   	| \&#118; |	 	      | Lowercase v |
| 119 | 167 | 77  | 01110111 | w   	| \&#119; |	 	      | Lowercase w |
| 120 | 170 | 78  | 01111000 | x   	| \&#120; |	 	      | Lowercase x |
| 121 | 171 | 79  | 01111001 | y   	| \&#121; |	 	      | Lowercase y |
| 122 | 172 | 7A  | 01111010 | z   	| \&#122; |	 	      | Lowercase z |
| 123 | 173 | 7B  | 01111011 | {   	| \&#123; |	\&lcub;	  | Opening brace |
| 124 | 174 | 7C  | 01111100 | \|  	| \&#124; |	\&verbar; | Vertical bar  |
| 125 | 175 | 7D  | 01111101 | }   	| \&#125; |	\&rcub;	  | Closing brace |
| 126 | 176 | 7E  | 01111110 | ~   	| \&#126; |	\&tilde;  | Equivalency sign - tilde |
| 127 | 177 | 7F  | 01111111 | DEL 	| \&#127; |	 	      | Delete |

## Extended:

| DEC | OCT | HEX | BIN      | SYM | HTML-UM  | HTML-NAME | DESCRIPTION |
| --- | --- | --- | -------- | --- | -------- | --------- | ----------- |
| 128 | 200 | 80  | 10000000 | €   | \&#8364; |	\&euro;	  | Euro sign |
| 129 | 201 | 81  | 10000001 | 	   |  	      |           | Unused |
| 130 | 202 | 82  | 10000010 | ‚   | \&#130;  |	\&sbquo;  | Single low-9 quotation mark |
| 131 | 203 | 83  | 10000011 | ƒ   | \&#131;  |	\&fnof;	  | Latin small letter f with hook |
| 132 | 204 | 84  | 10000100 | „   | \&#132;  |	\&bdquo;  | Double low-9 quotation mark |
| 133 | 205 | 85  | 10000101 | …   | \&#133;  |	\&hellip; | Horizontal ellipsis |
| 134 | 206 | 86  | 10000110 | †   | \&#134;  |	\&dagger; | Dagger |
| 135 | 207 | 87  | 10000111 | ‡   | \&#135;  |	\&Dagger; | Double dagger |
| 136 | 210 | 88  | 10001000 | ˆ   | \&#136;  |	\&circ;	  | Modifier letter circumflex accent |
| 137 | 211 | 89  | 10001001 | ‰   | \&#137;  |	\&permil; | Per mille sign |
| 138 | 212 | 8A  | 10001010 | Š   | \&#138;  |	\&Scaron; | Latin capital letter S with caron |
| 139 | 213 | 8B  | 10001011 | ‹   | \&#139;  |	\&lsaquo; | Single left-pointing angle quotation |
| 140 | 214 | 8C  | 10001100 | Œ   | \&#140;  |	\&OElig;  | Latin capital ligature OE |
| 141 | 215 | 8D  | 10001101 | 	   |	 	  |           | Unused                                      |  
| 142 | 216 | 8E  | 10001110 | Ž   | \&#142;  |	\&Zcaron; | Latin capital letter Z with caron |
| 143 | 217 | 8F  | 10001111 | 	   |	 	  |           | Unused |
| 144 | 220 | 90  | 10010000 | 	   |	 	  |           | Unused |
| 145 | 221 | 91  | 10010001 | ‘   | \&#145;  |	\&lsquo;  | Left single quotation mark |
| 146 | 222 | 92  | 10010010 | ’   | \&#146;  |	\&rsquo;  | Right single quotation mark |
| 147 | 223 | 93  | 10010011 | “   | \&#147;  |	\&ldquo;  | Left double quotation mark |
| 148 | 224 | 94  | 10010100 | ”   | \&#148;  |	\&rdquo;  | Right double quotation mark |
| 149 | 225 | 95  | 10010101 | •   | \&#149;  |	\&bull;	  | Bullet |
| 150 | 226 | 96  | 10010110 | –   | \&#150;  |	\&ndash;  | En dash |
| 151 | 227 | 97  | 10010111 | —   | \&#151;  |	\&mdash;  | Em dash |
| 152 | 230 | 98  | 10011000 | ˜   | \&#152;  |	\&tilde;  | Small tilde |
| 153 | 231 | 99  | 10011001 | ™   | \&#153;  |	\&trade;  | Trade mark sign |
| 154 | 232 | 9A  | 10011010 | š   | \&#154;  |	\&scaron; | Latin small letter S with caron |
| 155 | 233 | 9B  | 10011011 | ›   | \&#155;  |	\&rsaquo; | Single right-pointing angle quotation mark |
| 156 | 234 | 9C  | 10011100 | œ   | \&#156;  |	\&oelig;  | Latin small ligature oe |
| 157 | 235 | 9D  | 10011101 | 	   |	 	  |           | Unused |
| 158 | 236 | 9E  | 10011110 | ž   | \&#158;  |	\&zcaron; | Latin small letter z with caron |
| 159 | 237 | 9F  | 10011111 | Ÿ   | \&#159;  |	\&Yuml;	  | Latin capital letter Y with diaeresis |
| 160 | 240 | A0  | 10100000 | N   | \&#160;  | \&nbsp;	  | Non-breaking space |
| 161 | 241 | A1  | 10100001 | ¡   | \&#161;  |	\&iexcl;  |     Inverted exclamation mark |
| 162 | 242 | A2  | 10100010 | ¢   | \&#162;  |	\&cent;	  |     Cent sign |
| 163 | 243 | A3  | 10100011 | £   | \&#163;  |	\&pound;  |     Pound sign |
| 164 | 244 | A4  | 10100100 | ¤   | \&#164;  |	\&curren; | Currency sign |
| 165 | 245 | A5  | 10100101 | ¥   | \&#165;  |	\&yen;	|     Yen sign |
| 166 | 246 | A6  | 10100110 | ¦   | \&#166;  |	\&brvbar;	| Pipe, broken vertical bar |
| 167 | 247 | A7  | 10100111 | §   | \&#167;  |	\&sect;	|     Section sign |
| 168 | 250 | A8  | 10101000 | ¨   | \&#168;  |	\&uml;	|     Spacing diaeresis - umlaut |
| 169 | 251 | A9  | 10101001 | ©   | \&#169;  |	\&copy;	|     Copyright sign |
| 170 | 252 | AA  | 10101010 | ª   | \&#170;  |	\&ordf;	|     Feminine ordinal indicator |
| 171 | 253 | AB  | 10101011 | «   | \&#171;  |	\&laquo;	|     Left double angle quotes |
| 172 | 254 | AC  | 10101100 | ¬   | \&#172;  |	\&not;	|     Negation |
| 173 | 255 | AD  | 10101101 | ­    | \&#173;  | \&shy;	 |   Soft hyphen |
| 174 | 256 | AE  | 10101110 | ®   | \&#174;  |	\&reg;	|     Registered trade mark sign |
| 175 | 257 | AF  | 10101111 | ¯   | \&#175;  |	\&macr;	|     Spacing macron - overline |
| 176 | 260 | B0  | 10110000 | °   | \&#176;  |	\&deg;	|     Degree sign |
| 177 | 261 | B1  | 10110001 | ±   | \&#177;  |	\&plusmn;	| Plus-or-minus sign |
| 178 | 262 | B2  | 10110010 | ²   | \&#178;  |	\&sup2;	|     Superscript two - squared |
| 179 | 263 | B3  | 10110011 | ³   | \&#179;  |	\&sup3;	|     Superscript three - cubed |
| 180 | 264 | B4  | 10110100 | ´   | \&#180;  |	\&acute;	|     Acute accent - spacing acute |
| 181 | 265 | B5  | 10110101 | µ   | \&#181;  |	\&micro;	|     Micro sign |
| 182 | 266 | B6  | 10110110 | ¶   | \&#182;  |	\&para;	|     Pilcrow sign - paragraph sign |
| 183 | 267 | B7  | 10110111 | ·   | \&#183;  |	\&middot;	| Middle dot - Georgian comma |
| 184 | 270 | B8  | 10111000 | ¸   | \&#184;  |	\&cedil;	|     Spacing cedilla |
| 185 | 271 | B9  | 10111001 | ¹   | \&#185;  |	\&sup1;	|     Superscript one |
| 186 | 272 | BA  | 10111010 | º   | \&#186;  |	\&ordm;	|     Masculine ordinal indicator |
| 187 | 273 | BB  | 10111011 | »   | \&#187;  |	\&raquo;	|     Right double angle quotes |
| 188 | 274 | BC  | 10111100 | ¼   | \&#188;  |	\&frac14;	| Fraction one quarter |
| 189 | 275 | BD  | 10111101 | ½   | \&#189;  |	\&frac12;	| Fraction one half |
| 190 | 276 | BE  | 10111110 | ¾   | \&#190;  |	\&frac34;	| Fraction three quarters |
| 191 | 277 | BF  | 10111111 | ¿   | \&#191;  |	\&iquest;	| Inverted question mark |
| 192 | 300 | C0  | 11000000 | À   | \&#192;  |	\&Agrave;	| Latin capital letter A with grave |
| 193 | 301 | C1  | 11000001 | Á   | \&#193;  |	\&Aacute;	| Latin capital letter A with acute |
| 194 | 302 | C2  | 11000010 | Â   | \&#194;  |	\&Acirc;	|     Latin capital letter A with circumflex |
| 195 | 303 | C3  | 11000011 | Ã   | \&#195;  |	\&Atilde;	| Latin capital letter A with tilde |
| 196 | 304 | C4  | 11000100 | Ä   | \&#196;  |	\&Auml;	|     Latin capital letter A with diaeresis |
| 197 | 305 | C5  | 11000101 | Å   | \&#197;  |	\&Aring;	|     Latin capital letter A with ring above |
| 198 | 306 | C6  | 11000110 | Æ   | \&#198;  |	\&AElig;	|     Latin capital letter AE |
| 199 | 307 | C7  | 11000111 | Ç   | \&#199;  |	\&Ccedil;	| Latin capital letter C with cedilla |
| 200 | 310 | C8  | 11001000 | È   | \&#200;  |	\&Egrave;	| Latin capital letter E with grave |
| 201 | 311 | C9  | 11001001 | É   | \&#201;  |	\&Eacute;	| Latin capital letter E with acute |
| 202 | 312 | CA  | 11001010 | Ê   | \&#202;  |	\&Ecirc;	|     Latin capital letter E with circumflex |
| 203 | 313 | CB  | 11001011 | Ë   | \&#203;  |	\&Euml;	|     Latin capital letter E with diaeresis |
| 204 | 314 | CC  | 11001100 | Ì   | \&#204;  |	\&Igrave;	| Latin capital letter I with grave |
| 205 | 315 | CD  | 11001101 | Í   | \&#205;  |	\&Iacute;	| Latin capital letter I with acute |
| 206 | 316 | CE  | 11001110 | Î   | \&#206;  |	\&Icirc;	|     Latin capital letter I with circumflex |
| 207 | 317 | CF  | 11001111 | Ï   | \&#207;  |	\&Iuml;	|     Latin capital letter I with diaeresis |
| 208 | 320 | D0  | 11010000 | Ð   | \&#208;  |	\&ETH;	|     Latin capital letter ETH |
| 209 | 321 | D1  | 11010001 | Ñ   | \&#209;  |	\&Ntilde;	| Latin capital letter N with tilde |
| 210 | 322 | D2  | 11010010 | Ò   | \&#210;  |	\&Ograve;	| Latin capital letter O with grave |
| 211 | 323 | D3  | 11010011 | Ó   | \&#211;  |	\&Oacute;	| Latin capital letter O with acute |
| 212 | 324 | D4  | 11010100 | Ô   | \&#212;  |	\&Ocirc;	|     Latin capital letter O with circumflex |
| 213 | 325 | D5  | 11010101 | Õ   | \&#213;  |	\&Otilde;	| Latin capital letter O with tilde |
| 214 | 326 | D6  | 11010110 | Ö   | \&#214;  |	\&Ouml;	|     Latin capital letter O with diaeresis |
| 215 | 327 | D7  | 11010111 | ×   | \&#215;  |	\&times;	|     Multiplication sign |
| 216 | 330 | D8  | 11011000 | Ø   | \&#216;  |	\&Oslash;	| Latin capital letter O with slash |
| 217 | 331 | D9  | 11011001 | Ù   | \&#217;  |	\&Ugrave;	| Latin capital letter U with grave |
| 218 | 332 | DA  | 11011010 | Ú   | \&#218;  |	\&Uacute;	| Latin capital letter U with acute |
| 219 | 333 | DB  | 11011011 | Û   | \&#219;  |	\&Ucirc;	|     Latin capital letter U with circumflex |
| 220 | 334 | DC  | 11011100 | Ü   | \&#220;  |	\&Uuml;	|     Latin capital letter U with diaeresis |
| 221 | 335 | DD  | 11011101 | Ý   | \&#221;  |	\&Yacute;	| Latin capital letter Y with acute |
| 222 | 336 | DE  | 11011110 | Þ   | \&#222;  |	\&THORN;	|     Latin capital letter THORN |
| 223 | 337 | DF  | 11011111 | ß   | \&#223;  |	\&szlig;	|     Latin small letter sharp s - ess-zed |
| 224 | 340 | E0  | 11100000 | à   | \&#224;  |	\&agrave;	| Latin small letter a with grave |
| 225 | 341 | E1  | 11100001 | á   | \&#225;  |	\&aacute;	| Latin small letter a with acute |
| 226 | 342 | E2  | 11100010 | â   | \&#226;  |	\&acirc;	|     Latin small letter a with circumflex |
| 227 | 343 | E3  | 11100011 | ã   | \&#227;  |	\&atilde;	| Latin small letter a with tilde |
| 228 | 344 | E4  | 11100100 | ä   | \&#228;  |	\&auml;	|     Latin small letter a with diaeresis |
| 229 | 345 | E5  | 11100101 | å   | \&#229;  |	\&aring;	|     Latin small letter a with ring above |
| 230 | 346 | E6  | 11100110 | æ   | \&#230;  |	\&aelig;	|     Latin small letter ae |
| 231 | 347 | E7  | 11100111 | ç   | \&#231;  |	\&ccedil;	| Latin small letter c with cedilla |
| 232 | 350 | E8  | 11101000 | è   | \&#232;  |	\&egrave;	| Latin small letter e with grave |
| 233 | 351 | E9  | 11101001 | é   | \&#233;  |	\&eacute;	| Latin small letter e with acute |
| 234 | 352 | EA  | 11101010 | ê   | \&#234;  |	\&ecirc;	|     Latin small letter e with circumflex |
| 235 | 353 | EB  | 11101011 | ë   | \&#235;  |	\&euml;	|     Latin small letter e with diaeresis |
| 236 | 354 | EC  | 11101100 | ì   | \&#236;  |	\&igrave;	| Latin small letter i with grave |
| 237 | 355 | ED  | 11101101 | í   | \&#237;  |	\&iacute;	| Latin small letter i with acute |
| 238 | 356 | EE  | 11101110 | î   | \&#238;  |	\&icirc;	|     Latin small letter i with circumflex |
| 239 | 357 | EF  | 11101111 | ï   | \&#239;  |	\&iuml;	|     Latin small letter i with diaeresis |
| 240 | 360 | F0  | 11110000 | ð   | \&#240;  |	\&eth;	|     Latin small letter eth |
| 241 | 361 | F1  | 11110001 | ñ   | \&#241;  |	\&ntilde;	| Latin small letter n with tilde |
| 242 | 362 | F2  | 11110010 | ò   | \&#242;  |	\&ograve;	| Latin small letter o with grave |
| 243 | 363 | F3  | 11110011 | ó   | \&#243;  |	\&oacute;	| Latin small letter o with acute |
| 244 | 364 | F4  | 11110100 | ô   | \&#244;  |	\&ocirc;	|     Latin small letter o with circumflex |
| 245 | 365 | F5  | 11110101 | õ   | \&#245;  |	\&otilde;	| Latin small letter o with tilde |
| 246 | 366 | F6  | 11110110 | ö   | \&#246;  |	\&ouml;	|     Latin small letter o with diaeresis |
| 247 | 367 | F7  | 11110111 | ÷   | \&#247;  |	\&divide;	| Division sign |
| 248 | 370 | F8  | 11111000 | ø   | \&#248;  |	\&oslash;	| Latin small letter o with slash |
| 249 | 371 | F9  | 11111001 | ù   | \&#249;  |	\&ugrave;	| Latin small letter u with grave |
| 250 | 372 | FA  | 11111010 | ú   | \&#250;  |	\&uacute;	| Latin small letter u with acute |
| 251 | 373 | FB  | 11111011 | û   | \&#251;  |	\&ucirc;	|     Latin small letter u with circumflex |
| 252 | 374 | FC  | 11111100 | ü   | \&#252;  |	\&uuml;	|     Latin small letter u with diaeresis |
| 253 | 375 | FD  | 11111101 | ý   | \&#253;  |	\&yacute;	| Latin small letter y with acute |
| 254 | 376 | FE  | 11111110 | þ   | \&#254;  |	\&thorn;	|     Latin small letter thorn |
| 255 | 377 | FF  | 11111111 | ÿ   | \&#255;  |	\&yuml;	|     Latin small letter y with diaeresis |

- ESC Character

A Special Character That can be used to Customize things in an uncountable amount of Ways:

Encodings:


| DEC | OCT | HEX | BIN      | SYM | HTML-UM | HTML-NAME | DESCRIPTION |
| --- | --- | --- | -------- | --- | ------- | --------- | ----------- |
| 27  | 033 | 1B  | 00011011 | ESC | \&#27;	 |	         | Escape      |


## Escape Squence
by: [ConnerWill](https://gist.github.com/ConnerWill/d4b6c776b509add763e17f9f113fd25b)
### Cursor Control

| ESC Code Sequence    |   Description                                          |
| -------------------- | ------------------------------------------------------ |
| ESC[H 	           | moves cursor to home position (0, 0)                   |
| ESC[{line};{column}H | moves cursor to line #, column #                       |
| ESC[{line};{column}f | moves cursor to line #, column #                       |
| ESC[#A 	           | moves cursor up # lines                                |
| ESC[#B 	           | moves cursor down # lines                              |
| ESC[#C 	           | moves cursor right # columns                           |
| ESC[#D 	           | moves cursor left # columns                            |
| ESC[#E 	           | moves cursor to beginning of next line, # lines down   |
| ESC[#F 	           | moves cursor to beginning of previous line, # lines up |
| ESC[#G 	           | moves cursor to column #                               |
| ESC[6n 	           | request cursor position (reports as ESC[#;#R)          |
| ESCM  	           | moves cursor one line up, scrolling if needed          |
| ESC7  	           | save cursor position (DEC)                             |
| ESC8  	           | restores the cursor to the last saved position (DEC)   |
| ESC[s 	           | save cursor position (SCO)                             |
| ESC[u 	           | restores the cursor to the last saved position (SCO)   |
            
### Erase Functions
                            
| ESC Code Sequence | Description                              |
| ----------------- | ---------------------------------------- |
| ESC[J 	        | erase in display (same as ESC[0J)        |
| ESC[0J 	        | erase from cursor until end of screen    |
| ESC[1J 	        | erase from cursor to beginning of screen |
| ESC[2J 	        | erase entire screen                      |
| ESC[3J 	        | erase saved lines                        |
| ESC[K 	        | erase in line (same as ESC[0K)           |
| ESC[0K 	        | erase from cursor to end of line         |
| ESC[1K 	        | erase start of line to the cursor        |
| ESC[2K 	        | erase the entire line                    |

### Colors / Graphics Mode

| ESC Code Sequence | Reset Sequence | Description                                              |
| ----------------- | -------------- | -------------------------------------------------------- |
| ESC[1;34;{...}m 	|                | Set graphics modes for cell, separated by semicolon (;). |
| ESC[0m 		    |                | reset all modes (styles and colors)                      |
| ESC[1m 	        | ESC[22m 	     | set bold mode.                                           |
| ESC[2m 	        | ESC[22m 	     | set dim/faint mode.                                      |
| ESC[3m 	        | ESC[23m 	     | set italic mode.                                         |
| ESC[4m 	        | ESC[24m 	     | set underline mode.                                      |
| ESC[5m 	        | ESC[25m 	     | set blinking mode                                        |
| ESC[7m 	        | ESC[27m 	     | set inverse/reverse mode                                 |
| ESC[8m 	        | ESC[28m 	     | set hidden/invisible mode                                |
| ESC[9m 	        | ESC[29m 	     | set strikethrough mode.                                  |

- Color

    (I) 8 - 16 Color Mode

        (A) `ESC[CODEm`

        -------------------------------------
        | Name    | Foreground | Background |
        -------------------------------------
        | Black   | 30 	       | 40         |
        | Red 	  | 31 	       | 41         |
        | Green   |	32 	       | 42         |
        | Yellow  | 33 	       | 43         |
        | Blue 	  | 34 	       | 44         |
        | Magenta |	35 	       | 45         |
        | Cyan 	  | 36 	       | 46         |
        | White   |	37 	       | 47         |
        | Default |	39 	       | 49         |
        | Reset   |	0 	       | 0          |
        -------------------------------------

        --------------------------------------------
        | Color Name     | Foreground | Background |
        --------------------------------------------
        | Bright Black   | 90 	      | 100        |
        | Bright Red     | 91 	      | 101        |
        | Bright Green   | 92 	      | 102        |
        | Bright Yellow  | 93 	      | 103        |
        | Bright Blue    | 94 	      | 104        |
        | Bright Magenta | 95 	      | 105        |
        | Bright Cyan    | 96 	      | 106        |
        | Bright White   | 97 	      | 107        |
        --------------------------------------------

    (II) 256 Colors

        ---------------------------------------------
        | ESC Code Sequence | Description           |
        ---------------------------------------------
        | ESC[38;5;{ID}m 	| Set foreground color. |
        | ESC[48;5;{ID}m 	| Set background color. |
        ---------------------------------------------

        (A) ID can be any number from 0 to 255

        CODES: https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png

    (III) RGB Color Mode
            
        --------------------------------------------------------
        | ESC Code Sequence 	| Description                  |
        --------------------------------------------------------
        | ESC[38;2;{r};{g};{b}m | Set foreground color as RGB. |
        | ESC[48;2;{r};{g};{b}m | Set background color as RGB. |
        --------------------------------------------------------

(e) Common Private Modes

| ESC Code   | Description                     |
| ---------- | ------------------------------- |
| ESC[?25l 	 | make cursor invisible           |
| ESC[?25h 	 | make cursor visible             |
| ESC[?47l   | restore screen                  |
| ESC[?47h   | save screen                     |
| ESC[?1049h | enables the alternative buffer  |
| ESC[?1049l | disables the alternative buffer |

]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Computational Complexity

Computational Complexity Describes the how well an algorith performs/task performs as the inputs grow as $n$

## Big-O

![](../../img/cs/bigo_notation.png)

### Exponential

$O(n!)$

$O(2^n)$

$O(n^2)$: looping over an entire $n \times n$ Matrix

```py
matrix = [
    [y_0_x_0, y_0_x_1, y_0_x_2, y_0_x_3, y_0_x_n],
    [y_1_x_0, y_1_x_1, y_1_x_2, y_1_x_3, y_1_x_n],
    [y_2_x_0, y_2_x_1, y_2_x_2, y_2_x_3, y_2_x_n],
    [y_3_x_0, y_3_x_1, y_3_x_2, y_3_x_3, y_3_x_n],
    [y_n_x_0, y_n_x_1, y_n_x_2, y_n_x_3, y_n_x_n],
]

for row in matrix:
    for element in row:
        # ...
```

### Linear Log

### Linear

$O(n)$: Looping over $n$ count of items

```py
list = [n_0, n_1, n_2, n_3, n_n]

for element in list:
    # ...
```

### Logarithmic, Constant

$O(1)$: Best possible space time complexity

```py
list.push(element)
```

# Algorithms

## Mathematical

**GCD Euclidean Algorithm**

Space-Time Complexity: $O(n)$

```python
def gcd(a, b):
    while b != 0:
        r = a % b;
        a = b;
        b = r;
    return a;
```

## Sorting

### Bubble Sort

**Bubble Sort**: Sorts elements by repeatedly swapping adjacent elements if they're in the wrong order.

Implementation:

[`bubblesort.py`](./algorithms/bubblesort.py)

```py
sampleList = [5, 4, 2, 6, 7, 2, 3, 1, 9]

def bubbleSort(List):
    loopList = List
    loopListlen = len(loopList)
    while True:
        continues = 0 # Check if all the elements are in order
        for i in range(1, loopListlen):

            j = i - 1
            if j < 0 : continue

            # Switch Elements if left one is bigger
            if loopList[j] > loopList[i]:
                tempElement = loopList[i]
                loopList[i] = loopList[j]
                loopList[j] = tempElement
            else:
                # Increment order if in order
                continues = continues + 1

        if(continues >= (loopListlen - 1)): break # Stop Looping if Sorted
        
    return loopList

print(bubbleSort(sampleList)) # [1, 2, 2, 3, 4, 5, 6, 7, 9]
```

### Insertion Sort

**Insertion Sort**: Builds a sorted array by inserting elements one at a time.

[`insertionsort.py`](./algorithms/insertionsort.py)

```py
sampleList = [5, 4, 2, 6, 7, 2, 3, 1, 9]

def insertionsort(List):
    loopList = List
    loopListlen = len(loopList)

    for i in range(1, loopListlen):
        element = loopList[i] # Selected Element

        for j in range(i):
            # Adjacent Elements
            Pelement = loopList[j]
            Nelement = loopList[j + 1]
            
            # Insert if previous is greater than current
            if Pelement >= element:
                loopList.pop(i)
                loopList.insert(j, element)
                break

            # Insert Element if it fits in between the 2 elements
            if (Pelement <= element) and (element <= Nelement):
                loopList.pop(i)
                loopList.insert(j + 1, element)
                break

    return loopList

print(insertionsort(sampleList)) # [1, 2, 2, 3, 4, 5, 6, 7, 9]
```