Primjeri pokretanja prog.py:<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;python prog.py -u www.microsoft.com biff<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;python prog.py -u -n -x www.microsoft.com biff<br/> 
    &nbsp;&nbsp;&nbsp;&nbsp;python prog.py -u www.microsoft.com 80<br/>

Kako pokrenuti zadacu 2 (udpklijent/udpserver):<br/>
    &nbsp;&nbsp;&nbsp;&nbsp; u jednom terminalu pokrenuti python udpserver.py -p 5555 <br/>
    &nbsp;&nbsp;&nbsp;&nbsp; u drugom terminalu pokrenuti python udpklijent.py -p 5555 127.0.0.1 <br/>
    &nbsp;&nbsp;&nbsp;&nbsp; u terminalu gdje je pokrenut klijent unositi znakove s tipkovnice i nakon Enter bi se trebao pojaviti rezultat <br />

Što je potrebno za zadaću 3 (tcpklijent/tcpserver):<br />
    &nbsp;&nbsp;&nbsp;&nbsp; potrebne su tri datoteke: tcpklijent.py, tcpserver.py, datoteka.txt <br />
    &nbsp;&nbsp;&nbsp;&nbsp; u jednom terminalu pokrenuti python tcpserver.py <br />
    &nbsp;&nbsp;&nbsp;&nbsp; u drugom terminalu pokrenuti python tcpklijent.py localhost <br />
    &nbsp;&nbsp;&nbsp;&nbsp; u terminalu gdje je pokrenut klijent unijeti ime datoteke (u mom slučaju datoteka.txt) <br />
    &nbsp;&nbsp;&nbsp;&nbsp; ako je program uspješan program će pročitati sadržaj navedene datoteke, ako ne baca grešku