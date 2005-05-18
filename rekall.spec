Summary:	Rekall - database front-end
Summary(pl):	Rekall - frontend do baz danych
Name:		rekall
Version:	2.2.3
Release:	2
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://www.rekallrevealed.org/packages/%{name}-%{version}-2.tar.gz
# Source0-md5:	0c27445eb9d58877067d60c94ef0dca9
Patch0:		%{name}-python.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.rekallrevealed.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xbsql-devel
Requires:	%{name}-common = %{version}-%{release}
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

%package common
Summary:	Common files for full and runtime version of Rekall
Summary(pl):	Pliki wspólne dla wersji pe³nej i uruchomieniowej Rekalla
Group:		Libraries

%description common
Common files for full and runtime version of Rekall.

%description common -l pl
Pliki wspólne dla wersji pe³nej i uruchomieniowej Rekalla.

%package runtime
Summary:	Runtime version of Rekall
Summary(pl):	Wersja uruchomieniowa Rekalla
Group:		Applications/Databases/Interfaces
Requires:	%{name}-common = %{version}-%{release}

%description runtime
Runtime version of Rekall.

%description runtime -l pl
Wersja uruchomieniowa Rekalla.

%package driver-mysql
Summary:	MySQL database driver for Rekall
Summary(pl):	Sterownik baz danych MySQL dla Rekalla
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description driver-mysql
MySQL database driver for Rekall.

%description driver-mysql -l pl
Sterownik baz danych MySQL dla Rekalla.

%package driver-pgsql
Summary:	PostgreSQL database driver for Rekall
Summary(pl):	Sterownik baz danych PostgreSQL dla Rekalla
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description driver-pgsql
PostgreSQL database driver for Rekall.

%description driver-pgsql -l pl
Sterownik baz danych PostgreSQL dla Rekalla.

%package driver-xbase
Summary:	XBase/XBSQL database driver for Rekall
Summary(pl):	Sterownik baz danych XBase/XBSQL dla Rekalla
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}

%description driver-xbase
XBase/XBSQL database driver for Rekall.

%description driver-xbase -l pl
Sterownik baz danych XBase/XBSQL dla Rekalla.

%package devel
Summary:	Header files for Rekall libraries
Summary(pl):	Pliki nag³ówkowe bibliotek Rekalla
Group:		Development/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description devel
Header files for Rekall libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek Rekalla.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure \
	--enable-runtime \
	--with-mysql-libraries=%{_libdir} \
	--with-pgsql-libraries=%{_libdir} \
	--with-qt-libraries=%{_libdir} \
	--with-xbase-libraries=%{_libdir} \
	--with-xbsql-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/rekall{,rt}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	common -p /sbin/ldconfig
%postun	common -p /sbin/ldconfig

%post	runtime -p /sbin/ldconfig
%postun	runtime -p /sbin/ldconfig

%post	driver-mysql -p /sbin/ldconfig
%postun	driver-mysql -p /sbin/ldconfig

%post	driver-pgsql -p /sbin/ldconfig
%postun	driver-pgsql -p /sbin/ldconfig

%post	driver-xbase -p /sbin/ldconfig
%postun	driver-xbase -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.FIRST Release.Notes doc/HOWTO
%attr(755,root,root) %{_bindir}/rekall
# libraries
%attr(755,root,root) %{_libdir}/libkbase.so.*.*.*
%attr(755,root,root) %{_libdir}/libkbase_app.so.*.*.*
%attr(755,root,root) %{_libdir}/libkbase_wizard.so.*.*.*
%attr(755,root,root) %{_libdir}/librekall.so.*.*.*
# KDE-like modules
%attr(755,root,root) %{_libdir}/libkbase_componentview.so
%{_libdir}/libkbase_componentview.la
%attr(755,root,root) %{_libdir}/libkbase_copierview.so
%{_libdir}/libkbase_copierview.la
%attr(755,root,root) %{_libdir}/libkbase_editor.so
%{_libdir}/libkbase_editor.la
%attr(755,root,root) %{_libdir}/libkbase_formview.so
%{_libdir}/libkbase_formview.la
%attr(755,root,root) %{_libdir}/libkbase_macroview.so
%{_libdir}/libkbase_macroview.la
%attr(755,root,root) %{_libdir}/libkbase_plugin_extra.so
%{_libdir}/libkbase_plugin_extra.la
%attr(755,root,root) %{_libdir}/libkbase_plugin_kde.so
%{_libdir}/libkbase_plugin_kde.la
%attr(755,root,root) %{_libdir}/libkbase_queryview.so
%{_libdir}/libkbase_queryview.la
%attr(755,root,root) %{_libdir}/libkbase_reportview.so
%{_libdir}/libkbase_reportview.la
%attr(755,root,root) %{_libdir}/libkbase_script_py.so
%{_libdir}/libkbase_script_py.la
%attr(755,root,root) %{_libdir}/libkbase_script_pysys.so
%{_libdir}/libkbase_script_pysys.la
%attr(755,root,root) %{_libdir}/libkbase_tableview.so
%{_libdir}/libkbase_tableview.la
# data
%{_datadir}/apps/rekall/services/kdeparts.lst
%{_datadir}/apps/rekall/services/rekall_component.desktop
%{_datadir}/apps/rekall/services/rekall_copier.desktop
%{_datadir}/apps/rekall/services/rekall_editor.desktop
%{_datadir}/apps/rekall/services/rekall_form.desktop
%{_datadir}/apps/rekall/services/rekall_macro.desktop
%{_datadir}/apps/rekall/services/rekall_plugin_extra.desktop
%{_datadir}/apps/rekall/services/rekall_plugin_kde.desktop
%{_datadir}/apps/rekall/services/rekall_query.desktop
%{_datadir}/apps/rekall/services/rekall_report.desktop
%{_datadir}/apps/rekall/services/rekall_script_py.desktop
%{_datadir}/apps/rekall/services/rekall_table.desktop
%{_datadir}/apps/rekall/stock
%{_datadir}/apps/rekall/wizards
%{_desktopdir}/rekall.desktop

%files common -f %{name}.lang
%defattr(644,root,root,755)
# libraries
%attr(755,root,root) %{_libdir}/libkbase_common.so.*.*.*
%attr(755,root,root) %{_libdir}/libel_compile.so.*.*.*
%attr(755,root,root) %{_libdir}/libel_interp.so.*.*.*
%attr(755,root,root) %{_libdir}/libkbase_kde.so.*.*.*
%attr(755,root,root) %{_libdir}/libkbase_tkwidgets.so.*.*.*
# data
%dir %{_datadir}/apps/rekall
%{_datadir}/apps/rekall/LICENSE
%{_datadir}/apps/rekall/dict
%{_datadir}/apps/rekall/help
%{_datadir}/apps/rekall/highlight
%{_datadir}/apps/rekall/icons
%{_datadir}/apps/rekall/keymap
%{_datadir}/apps/rekall/pics
%{_datadir}/apps/rekall/rekall.png
%{_datadir}/apps/rekall/rekallui.*
%{_datadir}/apps/rekall/script
%dir %{_datadir}/apps/rekall/services
%{_datadir}/apps/rekall/services/rekall_dummy.desktop

%files runtime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rekallrt
# libraries
%attr(755,root,root) %{_libdir}/libkbasert.so.*.*.*
%attr(755,root,root) %{_libdir}/libkbasert_app.so.*.*.*
%attr(755,root,root) %{_libdir}/librekallrt.so.*.*.*
# modules
%attr(755,root,root) %{_libdir}/libkbasert_formview.so
%{_libdir}/libkbasert_formview.la
%attr(755,root,root) %{_libdir}/libkbasert_plugin_extra.so
%{_libdir}/libkbasert_plugin_extra.la
%attr(755,root,root) %{_libdir}/libkbasert_queryview.so
%{_libdir}/libkbasert_queryview.la
%attr(755,root,root) %{_libdir}/libkbasert_reportview.so
%{_libdir}/libkbasert_reportview.la
%attr(755,root,root) %{_libdir}/libkbasert_script_py.so
%{_libdir}/libkbasert_script_py.la
%attr(755,root,root) %{_libdir}/libkbasert_script_pysys.so
%{_libdir}/libkbasert_script_pysys.la
%attr(755,root,root) %{_libdir}/libkbasert_tableview.so
%{_libdir}/libkbasert_tableview.la
# data
%{_datadir}/apps/rekall/services/rekallrt_copier.desktop
%{_datadir}/apps/rekall/services/rekallrt_form.desktop
%{_datadir}/apps/rekall/services/rekallrt_plugin_extra.desktop
%{_datadir}/apps/rekall/services/rekallrt_query.desktop
%{_datadir}/apps/rekall/services/rekallrt_report.desktop
%{_datadir}/apps/rekall/services/rekallrt_script_py.desktop
%{_datadir}/apps/rekall/services/rekallrt_table.desktop
%{_datadir}/apps/rekallrt
%{_desktopdir}/rekallrt.desktop

%files driver-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkbase_driver_mysql.so
%{_libdir}/libkbase_driver_mysql.la
%{_datadir}/apps/rekall/services/rekall_driver_mysql.desktop

%files driver-pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkbase_driver_pgsql.so
%{_libdir}/libkbase_driver_pgsql.la
%{_datadir}/apps/rekall/services/rekall_driver_pgsql.desktop

%files driver-xbase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkbase_driver_xbase.so.*.*.*
%attr(755,root,root) %{_libdir}/libkbase_driver_xbase.so
%{_libdir}/libkbase_driver_xbase.la
%{_datadir}/apps/rekall/services/rekall_driver_xbase.desktop

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
%attr(755,root,root) %{_libdir}/libkbasert.so
%attr(755,root,root) %{_libdir}/libkbasert_app.so
%attr(755,root,root) %{_libdir}/librekall.so
%attr(755,root,root) %{_libdir}/librekallrt.so
%{_libdir}/libel_compile.la
%{_libdir}/libel_interp.la
%{_libdir}/libkbase.la
%{_libdir}/libkbase_app.la
%{_libdir}/libkbase_common.la
%{_libdir}/libkbase_kde.la
%{_libdir}/libkbase_tkwidgets.la
%{_libdir}/libkbase_wizard.la
%{_libdir}/libkbasert.la
%{_libdir}/libkbasert_app.la
%{_libdir}/librekall.la
%{_libdir}/librekallrt.la
%{_includedir}/rekall
