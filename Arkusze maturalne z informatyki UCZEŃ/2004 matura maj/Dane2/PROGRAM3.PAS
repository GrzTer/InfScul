program program3;
var
tablica: array[1..20] of real;
tmp,wynik:real;
i,j:integer;
p,dane:text;
begin
for j:=1 to 20 do tablica[j] := 0;
assign(dane,'oporniki.txt');
reset(dane);
   for i:=1 to 20 do
     for j:=1 to i do
     begin
       read(dane,tmp);
       tablica[i]:=tablica[i]+tmp;
     end;
close(dane);
   wynik:=0;
   for i:=1 to 20 do
       wynik:=wynik+1/tablica[i];
   wynik:=1/wynik;
   assign(p,'wynik3.txt');
   rewrite(p);
   write(p,wynik:8:2);
   close(p);
end.