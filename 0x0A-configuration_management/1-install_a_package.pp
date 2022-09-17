# install_a_package.pp
# package

package { 'flask-pip3':
  ensure   => '2.1.1',
  provider => 'gem'
}
