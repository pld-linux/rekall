Summary:	Rekall - database front-end
Summary(pl):	Rekall - frontend do baz danych
Name:		rekall
Version:	2.2.3
Release:	0.1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://www.rekallrevealed.org/packages/%{name}-%{version}-2.tar.gz
# Source0-md5:	0c27445eb9d58877067d60c94ef0dca9
Patch0:		%{name}-python.patch
URL:		http://www.rekallrevealed.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	xbsql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rekall is a database front-end, somewhat in the style of MicroSoft(R)
Access(TM). However, Rekall is not itself a database, and does not
include a database. By this we mean that data is stored somewhere else
in an SQL server, and Rekall is fundementaly just a tool to extract,
display and update that data (of course, it does lots more than that,
it does forms and reports and scripting and... you get the idea). It
is database agnostic, and does not have any preferred database in the
sense that Access(TM) uses the Jet database engine (although the
Windows version can use the Jet database engine via an ODBC driver).

Rekall can do lots of the things that you would expect of a database
front-end (or if it can't, let us know!). You can design and use forms
and reports, you can construct database queries, and you can import
and export data (actually, you can copy data, import is just copy file
to table, and export is just copy table to file). You can also create
reusable components which you can use in forms and reports, to reduce
application development time.

Rekall can be scripted using the Python language. You can arrange that
a script is executed when various events occur (for instance, when the
user changes the value of a control). Scripts can be associated
directly with the event, but you can also store scripts in script
modules for more general use. And, of course, you have full access to
all the modules that are available for Python. Plus, Rekall has an
integrated Python debugger with syntax highlighting.

%description -l pl
Rekall to frontend do baz danych nieco podobny do programu
MicroSoft(R) Access(TM). Rekall nie jest jednak baz± danych i nie
zawiera bazy danych. Znaczy to, ¿e dane s± przechowywane gdzie¶
indziej na serwerze SQL, a Rekall jest zasadniczo tylko narzêdziem do
wyci±gania, wy¶wietlania i uaktualniania tych danych (oczywi¶cie robi
du¿o wiêcej, jak na przyk³ad formularze, raporty, skrypty...). Jest
niezale¿ny od bazy danych i nie ma preferowanej bazy w tym sensie, w
jakim Access(TM) u¿ywa silnika Jet (choæ wersja dla Windows mo¿e
u¿ywaæ silnika baz danych Jet poprzez sterownik ODBC).

Rekall potrafi du¿o rzeczy, jakich mo¿na by oczekiwaæ od frontendu do
baz danych. Pozwala projektowaæ i u¿ywaæ formularze i raporty,
konstruowaæ zapytania, importowaæ i eksportowaæ dane (w³a¶ciwie
pozwala kopiowaæ dane, import to po prostu kopia z pliku do tabeli, a
eksport - kopia z tabeli do pliku). Mo¿na tak¿e tworzyæ komponenty
wielokrotnego u¿ycia do wykorzystania w formularzach i raportach w
celu zaoszczêdzenia czasu tworzenia aplikacji.

Rekall mo¿e byæ oskryptowany przy u¿yciu jêzyka Python. Mo¿na ustawiæ,
¿eby skrypt by³ wykonywany przy wyst±pieniu ró¿nych zdarzeñ (na
przyk³ad kiedy u¿ytkownik zmienia zawarto¶æ kontrolki). Skrypty mog±
byæ wi±zane bezpo¶rednio ze zdarzeniem albo przechowywane w modu³ach
skryptów do bardziej ogólnego u¿ytku. Oczywi¶cie mo¿liwy jest pe³ny
dostêp do wszystkich modu³ów dostêpnych dla Pythona. Dodatkowo Rekall
ma zintegrowany debugger Pythona z pod¶wietlaniem sk³adni.

%package devel
Summary:	Header files for Rekall libraries
Summary(pl):	Pliki nag³ówkowe bibliotek Rekalla
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Rekall libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek Rekalla.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/rekall.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.FIRST Release.Notes doc/HOWTO
%attr(755,root,root) %{_bindir}/rekall
%attr(755,root,root) %{_bindir}/rekallCon
%attr(755,root,root) %{_bindir}/rekallHelp
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libkbase_componentview.so
%attr(755,root,root) %{_libdir}/libkbase_copierview.so
%attr(755,root,root) %{_libdir}/libkbase_driver_mysql.so
%attr(755,root,root) %{_libdir}/libkbase_driver_pgsql.so
%attr(755,root,root) %{_libdir}/libkbase_driver_xbase.so.*.*.*
%attr(755,root,root) %{_libdir}/libkbase_driver_xbase.so
%attr(755,root,root) %{_libdir}/libkbase_editor.so
%attr(755,root,root) %{_libdir}/libkbase_formview.so
%attr(755,root,root) %{_libdir}/libkbase_macroview.so
%attr(755,root,root) %{_libdir}/libkbase_plugin_extra.so
%attr(755,root,root) %{_libdir}/libkbase_plugin_kde.so
%attr(755,root,root) %{_libdir}/libkbase_queryview.so
%attr(755,root,root) %{_libdir}/libkbase_reportview.so
%attr(755,root,root) %{_libdir}/libkbase_script_py*.so
%attr(755,root,root) %{_libdir}/libkbase_tableview.so
%{_datadir}/apps/rekall
%{_datadir}/apps/rekallrt
%{_desktopdir}/rekall.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libel_compile.so
%attr(755,root,root) %{_libdir}/libel_interp.so
%attr(755,root,root) %{_libdir}/libkbase.so
%attr(755,root,root) %{_libdir}/libkbase_app.so
%attr(755,root,root) %{_libdir}/libkbase_common.so
%attr(755,root,root) %{_libdir}/libkbase_kde.so
%attr(755,root,root) %{_libdir}/libkbase_tkwidgets.so
%attr(755,root,root) %{_libdir}/libkbase_wizard.so
%attr(755,root,root) %{_libdir}/librekall.so
%{_libdir}/lib*.la
%{_includedir}/rekall
