const
  dl_str = 130;
  dl_liczby = 80;
type
  dane_t = string[dl_str];
  liczba_t = record
               naj_znacz : 0..dl_liczby;
               cyf  : array[0..dl_liczby] of 0..2
             end;

procedure wczytaj_liczby(var l1, l2: liczba_t);
var
  i, j, dl : integer;
  d : dane_t;
begin
  for i := 0 to dl_liczby do
  begin l1.cyf[i] := 0; l2.cyf[i] := 0 end;
  readln(d);
  dl := length(d);
  i := -1; j := length(d);
  while d[j] <> ' 'do
  begin
    i := i+1;
    l1.cyf[i] := ord(d[j]) - ord('0');
    j := j-1
  end;
  l1.naj_znacz := dl - j - 1;
  i := -1; j := j-1;
  l2.naj_znacz := j-1;
  while j > 0 do
  begin
    i := i+1;
    l2.cyf[i] := ord(d[j]) - ord('0');
    j := j-1
  end
end;

procedure dodaj(var l1, l2, w: liczba_t);
var
  i, max, przen, s: integer;
begin
  for i := 0 to dl_liczby do w.cyf[i] := 0;
  if l1.naj_znacz >= l2.naj_znacz then
    max := l1.naj_znacz
  else
    max := l2.naj_znacz;
  przen := 0;
  for i := 0 to max do
  begin
    s := l1.cyf[i] + l2.cyf[i] + przen;
    w.cyf[i] := s mod 3;
    przen := s div 3;
  end;
  if przen > 0 then
  begin
    max := max + 1;
    w.cyf[max] := przen
  end;
  w.naj_znacz := max
end;

procedure wypisz(var w: liczba_t);
var
  i : integer;
begin
  for i := w.naj_znacz downto 0 do
    write(w.cyf[i]);
  writeln
end;

const
  liczba_testow = 50;

var
  liczba1, liczba2, wynik : liczba_t;
  i : integer;

begin
  for i := 1 to liczba_testow do
  begin
  wczytaj_liczby(liczba1, liczba2);
  dodaj(liczba1, liczba2, wynik);
  wypisz(wynik);
  end
end.
