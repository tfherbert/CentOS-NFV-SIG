#!/bin/bash
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
set -e

PWD=`pwd`
mkdir -p $PWD/rpmbuild/{BUILD,RPMS,SOURCES,SPECS}
cp centos-release-nfv-common.spec $PWD/rpmbuild/SPECS
cp RPM-GPG-KEY-CentOS-SIG-NFV $PWD/rpmbuild/SOURCES 

rpmbuild -bs --define "%_topdir $PWD/rpmbuild" $PWD/centos-release-nfv-common.spec

exit 0
