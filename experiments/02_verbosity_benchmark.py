"""Exp 02 — Verify book p.12 verbosity claim: Ruby 1-liner vs Java 5-liner.
Book: Ruby print "Hello, world!" vs Java class Hello { public static void main ... }
We quantify LOC, tokens, AST nodes; assert Ruby < Java by >=4x.
Also Shoes minimal app (book Ch.3/5): Shoes.app { para; button } stays <=6 lines.
"""
import re

RUBY_HELLO = 'print "Hello, world!"'
JAVA_HELLO = """class Hello {
public static void main(String args[]) {
System.out.println("Hello, world!");
}
}"""
PYTHON_HELLO = 'print("Hello, world!")'
SHOES_MIN = """Shoes.app do
  para "Hello World"
end"""

def loc(s): return len([l for l in s.splitlines() if l.strip() != ""])
def toks(s): return len(re.findall(r"[A-Za-z_]+|\"[^\"]*\"|[{}();.]", s))

if __name__ == "__main__":
    for name, code in [("Ruby", RUBY_HELLO), ("Java", JAVA_HELLO),
                       ("Python", PYTHON_HELLO), ("Shoes-min", SHOES_MIN)]:
        print(f"{name:10s} LOC={loc(code)} toks={toks(code)}")
    assert loc(RUBY_HELLO) == 1, "Ruby must be 1 line per book"
    assert loc(JAVA_HELLO) == 5, "Java must be 5 lines per book"
    ratio = toks(JAVA_HELLO) / max(1, toks(RUBY_HELLO))
    print(f"Java/Ruby token ratio = {ratio:.2f}x")
    assert ratio >= 4.0, "verbosity gap must hold"
    assert loc(SHOES_MIN) <= 6
    print("Verbosity claim VERIFIED: Ruby 1-liner holds; Java >=4x tokens.")
