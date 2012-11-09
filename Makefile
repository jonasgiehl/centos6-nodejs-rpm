include defines.mk

version:=$(ver)
nodefile:=node-v$(version).tar.gz
spec:=nodejs.spec

rpm: clean prepare
	rpmbuild -bb ~/rpmbuild/SPECS/nodejs.spec
clean:
	rm -rf ~/rpmbuild/SOURCES/$(nodefile)
	rm -rf $(nodefile)
	rm -rf ~/rpmbuild/SPECS/$(spec)	 
		
prepare: 
	mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	if [ ! -f $(nodefile) ] ; then \
	wget http://nodejs.org/dist/v$(version)/$(nodefile);fi;	
	cp $(nodefile) ~/rpmbuild/SOURCES 
	sed s/@@VERSION@@/$(version)/g $(spec)| \
	sed s/@@RELEASE@@/$(rel)/g | \
	sed s/@@JOBS@@/$(jobs)/g > ~/rpmbuild/SPECS/$(spec)
		
