**winccoa-manager**

***

# API documentation for WinCC OA JavaScript Manager for Node.js&#174;

---

The main API class is **[WinccoaManager](#winccoamanager)**, start your exploration there.

---

> **IMPORTANT**
>
> Most code examples in this documentation are not complete, but only
> snippets that show how to use a method or type. Note that the methods
> described in this documentation must be **called from code inside a
> method or function** to prevent unexpected or undefined behavior.

> **NOTE**
>
> If a code example does not contain an `import` statement, it is assumed that an
> instance of [WinccoaManager](#winccoamanager) has been created and can be accessed with
> the constant `winccoa`, e. g.:
>
> ```ts
> import { WinccoaManager } from 'winccoa-manager';
> const winccoa = new WinccoaManager();
> ```

> **NOTE**
>
> Almost all examples in this API documentation are given in TypeScript, but it is
> easy to convert them to JavaScript, if required:
>
> 1. Replace `import { ... } from 'winccoa-manager'` with
>    `const { ... } = require('winccoa-manager')`.
> 2. Remove all explicit type definitions (e. g. replace `name: number` with `name`).
> 3. Remove all type conversions that are using the keyword `as`.
> 4. Do not use the question mark for optional parameters.
>
> Examples given both in TypeScript and JavaScript that illustrate all these points
> can be found In the documentation for [WinccoaDpConnectCallback](#winccoadpconnectcallback),
> [WinccoaError](#winccoaerror) and [WinccoaAlertTime](#winccoaalerttime).
>
> ---
>
> **_require() or import?_**
>
> Using `require()` in JavaScript code allows the JavaScript Manager to find
> modules also when they are located in sub-projects or the WinCC OA installation.
> This includes the Node.js AddOn that implements this API. Therefore it is strongly
> recommended to use `require()` in JavaScript code.
>
> This is also the reason why TypeScript `import` statements will be transpiled to
> `require()` when using the templates provided by WinCC OA.

## Enumerations

<a id="winccoacnsaction"></a>

### WinccoaCnsAction

Enumerates the actions that are returned by callbacks registered
with [WinccoaManager.cnsAddObserver](#cnsaddobserver).

#### Enumeration Members

<a id="addtree"></a>

##### AddTree

> **AddTree**: `9`

CNS tree added.

<a id="changenodedata"></a>

##### ChangeNodeData

> **ChangeNodeData**: `11`

Node data changed.

<a id="changenodenames"></a>

##### ChangeNodeNames

> **ChangeNodeNames**: `10`

Node name changed.

<a id="changetree"></a>

##### ChangeTree

> **ChangeTree**: `8`

Tree changed.

<a id="changeviewnames"></a>

##### ChangeViewNames

> **ChangeViewNames**: `4`

View name changed.

<a id="changeviewseparators"></a>

##### ChangeViewSeparators

> **ChangeViewSeparators**: `5`

View separator changed.

<a id="createtree"></a>

##### CreateTree

> **CreateTree**: `6`

Tree created.

<a id="createview"></a>

##### CreateView

> **CreateView**: `2`

View created.

<a id="deletetree"></a>

##### DeleteTree

> **DeleteTree**: `7`

Tree deleted.

<a id="deleteview"></a>

##### DeleteView

> **DeleteView**: `3`

View deleted.

<a id="none"></a>

##### None

> **None**: `0`

No specific action

<a id="systemnames"></a>

##### SystemNames

> **SystemNames**: `1`

System name changed.

***

<a id="winccoacnschangetype"></a>

### WinccoaCnsChangeType

Enumerates the type of changes that are returned by callbacks registered
with [WinccoaManager.cnsAddObserver](#cnsaddobserver).

#### Enumeration Members

<a id="data"></a>

##### Data

> **Data**: `3`

Node data changed.

<a id="names"></a>

##### Names

> **Names**: `2`

Other name changed.

<a id="structure"></a>

##### Structure

> **Structure**: `4`

Structure of the CNS tree changed.

<a id="systemnames-1"></a>

##### SystemNames

> **SystemNames**: `0`

System name changed.

<a id="viewseparators"></a>

##### ViewSeparators

> **ViewSeparators**: `1`

View separator changed.

***

<a id="winccoacnsconstants"></a>

### WinccoaCnsConstants

Enumerates constants used by CNS methods (e. g.: [WinccoaManager.cnsGetIdSet](#cnsgetidset)).

#### Enumeration Members

<a id="alllanguages"></a>

##### AllLanguages

> **AllLanguages**: `255`

Search for all languages

***

<a id="winccoacnsnodetype"></a>

### WinccoaCnsNodeType

Enumerates the pre-defined CNS node types (additional numerical values can be
used as custom types)

#### Enumeration Members

<a id="all"></a>

##### All

> **All**: `0`

All node types, e.g. for searches (e. g.: [WinccoaManager.cnsGetIdSet](#cnsgetidset)).

<a id="datapoint"></a>

##### Datapoint

> **Datapoint**: `2`

Data point node.

<a id="empty"></a>

##### Empty

> **Empty**: `1`

Empty node (alias for [WinccoaCnsNodeType.Structure](#structure-1)).

<a id="structure-1"></a>

##### Structure

> **Structure**: `1`

Structure node type.

***

<a id="winccoacnssearchmode"></a>

### WinccoaCnsSearchMode

Enumerates the different search modes for [WinccoaManager.cnsGetIdSet](#cnsgetidset).

Can be combined using a pipe symbol (`|`), e. g.:
`WinccoaCnsSearchMode.DisplayName | WinccoaCnsSearchMode.CaseInsensitive`

#### Enumeration Members

<a id="allnames"></a>

##### AllNames

> **AllNames**: `3`

Search both in ID and name path

<a id="caseinsensitive"></a>

##### CaseInsensitive

> **CaseInsensitive**: `4`

Search case insensitve, to be combined with other flags

<a id="displayname"></a>

##### DisplayName

> **DisplayName**: `2`

Only search in name path

<a id="name"></a>

##### Name

> **Name**: `1`

Only search in ID path

***

<a id="winccoacnssubstrflags"></a>

### WinccoaCnsSubStrFlags

Enumerates flags for [WinccoaManager.cnsSubStr](#cnssubstr). Flags can be combined with binary OR (`|`).

#### Enumeration Members

<a id="node"></a>

##### Node

> **Node**: `32`

The last node from [Path](#path).

<a id="parent"></a>

##### Parent

> **Parent**: `8`

Like [Path](#path), but without the last node. If [Path](#path) only has a single node,
that node will be returned.

<a id="path"></a>

##### Path

> **Path**: `4`

The node path. If resolvePath is true and the path can be resolved, this spans from
after the view separator up to and including the last existing node. Otherwise, it spans
from after the view separator up to and excluding the optional second view separator and
the optional path separator directly before it.

<a id="root"></a>

##### Root

> **Root**: `16`

The first node from [Path](#path).

<a id="system"></a>

##### System

> **System**: `1`

The system name. If resolvePath is true and the view can be resolved, the system name
will be taken from the existing view, otherwise it will be taken from the given path string.

<a id="tail"></a>

##### Tail

> **Tail**: `64`

Everything after [Path](#path).

<a id="view"></a>

##### View

> **View**: `2`

If specified without other flags, the view name (`<view>`),
otherwise the view path (`.<view>:`).

***

<a id="winccoaconnectupdatetype"></a>

### WinccoaConnectUpdateType

Enumerates the type of updates received by connect callbacks.

#### See

- [WinccoaDpConnectCallback](#winccoadpconnectcallback)
- [WinccoaDpQueryConnectCallback](#winccoadpqueryconnectcallback)

#### Enumeration Members

<a id="answer"></a>

##### Answer

> **Answer**: `1`

Initial update with current values.

<a id="normal"></a>

##### Normal

> **Normal**: `0`

Normal update after value changes.

<a id="refresh"></a>

##### Refresh

> **Refresh**: `2`

Refresh update after REDU switch or DIST connection.

***

<a id="winccoactrltype"></a>

### WinccoaCtrlType

Enumerates CTRL data types that can be used as parameters for CTRL function calls.
The enumerated values have exactly the same name as the corresponding CTRL type
and therefore start with a lowercase letter.

#### See

[WinccoaCtrlScript.start](#start)

#### Enumeration Members

<a id="atime"></a>

##### atime

> **atime**: `2424832`

`atime` variable type

<a id="bit32"></a>

##### bit32

> **bit32**: `589824`

`bit32` variable type

<a id="bit64"></a>

##### bit64

> **bit64**: `4980736`

`bit64` variable type

<a id="blob"></a>

##### blob

> **blob**: `3014656`

`blob` variable type

<a id="bool"></a>

##### bool

> **bool**: `262144`

`bool` variable type

<a id="char"></a>

##### char

> **char**: `655360`

`char` variable type

<a id="double"></a>

##### double

> **double**: `458752`

`double` variable type

<a id="dyn_atime"></a>

##### dyn\_atime

> **dyn\_atime**: `2490368`

`dyn_atime` variable type

<a id="dyn_bit32"></a>

##### dyn\_bit32

> **dyn\_bit32**: `1245184`

`dyn_32bit` variable type

<a id="dyn_bit64"></a>

##### dyn\_bit64

> **dyn\_bit64**: `5046272`

`dyn_bit6` variable type

<a id="dyn_bool"></a>

##### dyn\_bool

> **dyn\_bool**: `917504`

`dyn_bool` variable type

<a id="dyn_char"></a>

##### dyn\_char

> **dyn\_char**: `1310720`

`dyn_char` variable type

<a id="dyn_dyn_atime"></a>

##### dyn\_dyn\_atime

> **dyn\_dyn\_atime**: `2555904`

`dyn_dyn_atime` variable type

<a id="dyn_dyn_bit32"></a>

##### dyn\_dyn\_bit32

> **dyn\_dyn\_bit32**: `2097152`

`dyn_dyn_32bit` variable type

<a id="dyn_dyn_bit64"></a>

##### dyn\_dyn\_bit64

> **dyn\_dyn\_bit64**: `5111808`

`dyn_dyn_bit64` variable type

<a id="dyn_dyn_bool"></a>

##### dyn\_dyn\_bool

> **dyn\_dyn\_bool**: `1769472`

`dyn_dyn_bool` variable type

<a id="dyn_dyn_char"></a>

##### dyn\_dyn\_char

> **dyn\_dyn\_char**: `2162688`

`dyn_dyn_char` variable type

<a id="dyn_dyn_float"></a>

##### dyn\_dyn\_float

> **dyn\_dyn\_float**: `1966080`

`dyn_dyn_float` variable type

<a id="dyn_dyn_int"></a>

##### dyn\_dyn\_int

> **dyn\_dyn\_int**: `1835008`

`dyn_dyn_int` variable type

<a id="dyn_dyn_langstring"></a>

##### dyn\_dyn\_langString

> **dyn\_dyn\_langString**: `2752512`

`dyn_dyn_langString variable type

<a id="dyn_dyn_long"></a>

##### dyn\_dyn\_long

> **dyn\_dyn\_long**: `4718592`

`dyn_dyn_long` variable type

<a id="dyn_dyn_string"></a>

##### dyn\_dyn\_string

> **dyn\_dyn\_string**: `2031616`

`dyn_dyn_string` variable type

<a id="dyn_dyn_time"></a>

##### dyn\_dyn\_time

> **dyn\_dyn\_time**: `1703936`

`dyn_dyn_time` variable type

<a id="dyn_dyn_uint"></a>

##### dyn\_dyn\_uint

> **dyn\_dyn\_uint**: `1900544`

`dyn_dyn_uint` variable type

<a id="dyn_dyn_ulong"></a>

##### dyn\_dyn\_ulong

> **dyn\_dyn\_ulong**: `4915200`

`dyn_dyn_ulong` variable type

<a id="dyn_float"></a>

##### dyn\_float

> **dyn\_float**: `1114112`

`dyn_float` variable type

<a id="dyn_int"></a>

##### dyn\_int

> **dyn\_int**: `983040`

`dyn_int` variable type

<a id="dyn_langstring"></a>

##### dyn\_langString

> **dyn\_langString**: `2686976`

`dyn_langString` variable type

<a id="dyn_long"></a>

##### dyn\_long

> **dyn\_long**: `4653056`

`dyn_long` variable type

<a id="dyn_string"></a>

##### dyn\_string

> **dyn\_string**: `1179648`

`dyn_string` variable type

<a id="dyn_time"></a>

##### dyn\_time

> **dyn\_time**: `851968`

`dyn_time` variable type

<a id="dyn_uint"></a>

##### dyn\_uint

> **dyn\_uint**: `1048576`

`dyn_uint` variable type

<a id="dyn_ulong"></a>

##### dyn\_ulong

> **dyn\_ulong**: `4849664`

`dyn_ulong` variable type

<a id="float"></a>

##### float

> **float**: `458752`

`float` variable type

<a id="int"></a>

##### int

> **int**: `327680`

`int` variable type

<a id="langstring"></a>

##### langString

> **langString**: `2621440`

`langString` variable type

<a id="long"></a>

##### long

> **long**: `4587520`

`long` variable type

<a id="string"></a>

##### string

> **string**: `524288`

`string` variable type

<a id="time"></a>

##### time

> **time**: `196608`

`time` variable type

<a id="uint"></a>

##### uint

> **uint**: `393216`

`uint` variable type

<a id="ulong"></a>

##### ulong

> **ulong**: `4784128`

`ulong` variable type

***

<a id="winccoadirectorylevel"></a>

### WinccoaDirectoryLevel

Enumerates the directories of the projects level for [WinccoaManager.cfgReadContent](#cfgreadcontent).

#### Enumeration Members

<a id="proj"></a>

##### Proj

> **Proj**: `0`

Level of the current project directory.

<a id="winccoa"></a>

##### WinCCOA

> **WinCCOA**: `-1`

Level of the product installation directory.

***

<a id="winccoadpsub"></a>

### WinccoaDpSub

Enumerates the different sub-strings that can be selected by
[WinccoaManager.dpSubStr](#dpsubstr).

#### Enumeration Members

<a id="all-1"></a>

##### ALL

> **ALL**: `65535`

[WinccoaManager.dpSubStr](#dpsubstr) returns the whole name string.

<a id="conf"></a>

##### CONF

> **CONF**: `4`

[WinccoaManager.dpSubStr](#dpsubstr) only returns the config.

<a id="conf_det"></a>

##### CONF\_DET

> **CONF\_DET**: `6`

[WinccoaManager.dpSubStr](#dpsubstr) only returns the config and detail.

<a id="conf_det_att"></a>

##### CONF\_DET\_ATT

> **CONF\_DET\_ATT**: `7`

[WinccoaManager.dpSubStr](#dpsubstr) only returns the config, detail
and attribute.

<a id="dp"></a>

##### DP

> **DP**: `16`

[WinccoaManager.dpSubStr](#dpsubstr) only returns the data point name.

<a id="dp_el"></a>

##### DP\_EL

> **DP\_EL**: `24`

[WinccoaManager.dpSubStr](#dpsubstr) returns the name string without
the system details,  attribute, detail and config.

<a id="dp_el_conf"></a>

##### DP\_EL\_CONF

> **DP\_EL\_CONF**: `28`

[WinccoaManager.dpSubStr](#dpsubstr) returns the name string without
the system details, attribute and detail.

<a id="dp_el_conf_det"></a>

##### DP\_EL\_CONF\_DET

> **DP\_EL\_CONF\_DET**: `30`

[WinccoaManager.dpSubStr](#dpsubstr) returns the name string without
the system details and attribute.

<a id="dp_el_conf_det_att"></a>

##### DP\_EL\_CONF\_DET\_ATT

> **DP\_EL\_CONF\_DET\_ATT**: `31`

[WinccoaManager.dpSubStr](#dpsubstr) returns the name string without
the system details.

<a id="sys"></a>

##### SYS

> **SYS**: `32`

[WinccoaManager.dpSubStr](#dpsubstr) only returns the system details
of a name string.

<a id="sys_dp"></a>

##### SYS\_DP

> **SYS\_DP**: `48`

[WinccoaManager.dpSubStr](#dpsubstr) only returns the system details
and the data point name.

<a id="sys_dp_el"></a>

##### SYS\_DP\_EL

> **SYS\_DP\_EL**: `56`

[WinccoaManager.dpSubStr](#dpsubstr) returns the name path except for
the attribute and the config.

<a id="sys_dp_el_conf"></a>

##### SYS\_DP\_EL\_CONF

> **SYS\_DP\_EL\_CONF**: `60`

[WinccoaManager.dpSubStr](#dpsubstr) returns the name path except for
the attribute and the detail.

<a id="sys_dp_el_conf_det"></a>

##### SYS\_DP\_EL\_CONF\_DET

> **SYS\_DP\_EL\_CONF\_DET**: `62`

[WinccoaManager.dpSubStr](#dpsubstr) returns the name path except for
the attribute.

<a id="sys_dp_el_conf_det_att"></a>

##### SYS\_DP\_EL\_CONF\_DET\_ATT

> **SYS\_DP\_EL\_CONF\_DET\_ATT**: `63`

[WinccoaManager.dpSubStr](#dpsubstr) returns the name path with attribute.

***

<a id="winccoaelementtype"></a>

### WinccoaElementType

Enumerates the type of a data point element, as returned by

[WinccoaManager.dpElementType](#dpelementtype).

#### See

[WinccoaManager.dpElementType](#dpelementtype).

#### Enumeration Members

<a id="bit32-1"></a>

##### Bit32

> **Bit32**: `24`

bit pattern

<a id="bit32struct"></a>

##### Bit32Struct

> **Bit32Struct**: `16`

bit pattern structure

<a id="bit64-1"></a>

##### Bit64

> **Bit64**: `50`

bit pattern

<a id="bit64struct"></a>

##### Bit64Struct

> **Bit64Struct**: `52`

bit pattern structure

<a id="blob-1"></a>

##### Blob

> **Blob**: `46`

blob (binary large object)

<a id="blobstruct"></a>

##### BlobStruct

> **BlobStruct**: `47`

blob structure

<a id="bool-1"></a>

##### Bool

> **Bool**: `23`

bit

<a id="boolstruct"></a>

##### BoolStruct

> **BoolStruct**: `15`

bit structure

<a id="char-1"></a>

##### Char

> **Char**: `19`

character

<a id="charstruct"></a>

##### CharStruct

> **CharStruct**: `11`

character structure

<a id="dpid"></a>

##### Dpid

> **Dpid**: `27`

DP-Identifier

<a id="dpidstruct"></a>

##### DpidStruct

> **DpidStruct**: `39`

label structure

<a id="dynbit32"></a>

##### DynBit32

> **DynBit32**: `8`

dynamic array for bit pattern

<a id="dynbit32struct"></a>

##### DynBit32Struct

> **DynBit32Struct**: `35`

dynamic bit-pattern array structure

<a id="dynbit64"></a>

##### DynBit64

> **DynBit64**: `51`

dynamic array for bit pattern

<a id="dynbit64struct"></a>

##### DynBit64Struct

> **DynBit64Struct**: `53`

dynamic bit-pattern array structure

<a id="dynblob"></a>

##### DynBlob

> **DynBlob**: `48`

dynamic blob

<a id="dynblobstruct"></a>

##### DynBlobStruct

> **DynBlobStruct**: `49`

dynamic blob structure

<a id="dynbool"></a>

##### DynBool

> **DynBool**: `7`

dynamic bit array

<a id="dynboolstruct"></a>

##### DynBoolStruct

> **DynBoolStruct**: `34`

dynamic bit array structure

<a id="dynchar"></a>

##### DynChar

> **DynChar**: `3`

dynamic character array

<a id="dyncharstruct"></a>

##### DynCharStruct

> **DynCharStruct**: `30`

dynamic character array structure

<a id="dyndpid"></a>

##### DynDpid

> **DynDpid**: `29`

dynamic DP-Identifier array

<a id="dyndpidstruct"></a>

##### DynDpidStruct

> **DynDpidStruct**: `38`

dynamic DP-Identifier array structure

<a id="dynfloat"></a>

##### DynFloat

> **DynFloat**: `6`

dynamic number array for floating decimal point

<a id="dynfloatstruct"></a>

##### DynFloatStruct

> **DynFloatStruct**: `33`

dynamic number structure for floating decimal point

<a id="dynint"></a>

##### DynInt

> **DynInt**: `5`

dynamic integer array

<a id="dynintstruct"></a>

##### DynIntStruct

> **DynIntStruct**: `32`

dynamic integer structure

<a id="dynlangstring"></a>

##### DynLangString

> **DynLangString**: `44`

multilingual dynamic text array

<a id="dynlangstringstruct"></a>

##### DynLangStringStruct

> **DynLangStringStruct**: `45`

multilingual dynamic text structure

<a id="dynlong"></a>

##### DynLong

> **DynLong**: `55`

dynamic array of Integer values (64 bit)

<a id="dynlongstruct"></a>

##### DynLongStruct

> **DynLongStruct**: `57`

dynamic number structure for integer value (64 bit)

<a id="dynstring"></a>

##### DynString

> **DynString**: `9`

dynamic text array

<a id="dynstringstruct"></a>

##### DynStringStruct

> **DynStringStruct**: `36`

dynamic text-array structure

<a id="dyntime"></a>

##### DynTime

> **DynTime**: `10`

dynamic time array

<a id="dyntimestruct"></a>

##### DynTimeStruct

> **DynTimeStruct**: `37`

dynamic time array structure

<a id="dynuint"></a>

##### DynUInt

> **DynUInt**: `4`

dynamic array of positive whole numbers

<a id="dynuintstruct"></a>

##### DynUIntStruct

> **DynUIntStruct**: `31`

dynamic array of positive integers

<a id="dynulong"></a>

##### DynULong

> **DynULong**: `59`

dynamic array of Positive integer values (64 bit)

<a id="dynulongstruct"></a>

##### DynULongStruct

> **DynULongStruct**: `61`

dynamic number structure for positive integer value (64 bit)

<a id="float-1"></a>

##### Float

> **Float**: `22`

floating point system

<a id="floatstruct"></a>

##### FloatStruct

> **FloatStruct**: `14`

number structure for floating decimal point

<a id="int-1"></a>

##### Int

> **Int**: `21`

integer

<a id="intstruct"></a>

##### IntStruct

> **IntStruct**: `13`

integer structure

<a id="langstring-1"></a>

##### LangString

> **LangString**: `42`

description

<a id="langstringstruct"></a>

##### LangStringStruct

> **LangStringStruct**: `43`

description structure

<a id="long-1"></a>

##### Long

> **Long**: `54`

Integer value (64 bit)

<a id="longstruct"></a>

##### LongStruct

> **LongStruct**: `56`

structure for integer value (64 bit)

<a id="string-1"></a>

##### String

> **String**: `25`

text

<a id="stringstruct"></a>

##### StringStruct

> **StringStruct**: `17`

text structure

<a id="struct"></a>

##### Struct

> **Struct**: `1`

structure

<a id="time-1"></a>

##### Time

> **Time**: `26`

time

<a id="timestruct"></a>

##### TimeStruct

> **TimeStruct**: `18`

time structure

<a id="typeref"></a>

##### Typeref

> **Typeref**: `41`

data point type reference

<a id="uint-1"></a>

##### UInt

> **UInt**: `20`

unsigned integer

<a id="uintstruct"></a>

##### UIntStruct

> **UIntStruct**: `12`

structure of unsigned integers

<a id="ulong-1"></a>

##### ULong

> **ULong**: `58`

Positive integer value (64 bit)

<a id="ulongstruct"></a>

##### ULongStruct

> **ULongStruct**: `60`

structure for positive integer value (64 bit)

***

<a id="winccoaerrorpriority"></a>

### WinccoaErrorPriority

Priority of a WinccoaError.

#### Enumeration Members

<a id="fatal"></a>

##### Fatal

> **Fatal**: `0`

fatal error. kill the program instance!

<a id="info"></a>

##### Info

> **Info**: `3`

info message - hello, here I am!

<a id="severe"></a>

##### Severe

> **Severe**: `1`

severe error, but we can continue

<a id="warning"></a>

##### Warning

> **Warning**: `2`

warning message, something is not as it should be

***

<a id="winccoaerrortype"></a>

### WinccoaErrorType

ErrorType of a WinccoaError.

#### Enumeration Members

<a id="control"></a>

##### Control

> **Control**: `3`

control runtime error

<a id="implementation"></a>

##### Implementation

> **Implementation**: `0`

implementation error

<a id="parameter"></a>

##### Parameter

> **Parameter**: `1`

parametrisation error

<a id="redundancy"></a>

##### Redundancy

> **Redundancy**: `4`

redundancy error

<a id="system-1"></a>

##### System

> **System**: `2`

system error

***

<a id="winccoalangstringformat"></a>

### WinccoaLangStringFormat

Enumerates the formats in which a multi-language strings (CTRL `langString`)
can be returned by the API.

#### See

- [WinccoaOptions.langIdx](#langidx)
- [WinccoaOptions.langStringFormat](#langstringformat)

#### Enumeration Members

<a id="array"></a>

##### Array

> **Array**: `3`

Multi-language strings will be returned as an array, sorted by
language IDs.

###### Example

```ts
['Deutscher Text', 'English text']
```

<a id="object"></a>

##### Object

> **Object**: `2`

Multi-language strings will be returned as an object, locale names
are used as property names.

###### Example

```ts
{ 'de_AT.utf8': 'Deutscher Text', 'en_US.utf8': 'English text' }
```

<a id="stringactivelanguage"></a>

##### StringActiveLanguage

> **StringActiveLanguage**: `0`

Multi-language strings will be returned as a simple sting in the
current language.

<a id="stringfixed"></a>

##### StringFixed

> **StringFixed**: `1`

Multi-language strings will be returned as a single string in the
 language defined with option [WinccoaOptions.langIdx](#langidx).

***

<a id="winccoalangtextformat"></a>

### ~~WinccoaLangTextFormat~~

#### Deprecated

Use [WinccoaLangStringFormat](#winccoalangstringformat) instead.

***

<a id="winccoanamechecktype"></a>

### WinccoaNameCheckType

Enumerates the different types of checks provided by [WinccoaManager.nameCheck](#namecheck).

#### Enumeration Members

<a id="dp-1"></a>

##### Dp

> **Dp**: `1`

Check for valid data point names. Forbidden characters for data point names are:
 `. : , ; * ? [ ] { } $ @` as well as unprintable ASCII characters.

<a id="path-1"></a>

##### Path

> **Path**: `3`

**`Alpha`**

__DO NOT USE__ (not implemented yet): Check for valid file paths.

<a id="project"></a>

##### Project

> **Project**: `2`

Check for valid project names. Forbidden characters for data point names are:
 `\ / " ? < > * | : ;` as well as unprintable ASCII characters.

***

<a id="winccoasecurityeventid"></a>

### WinccoaSecurityEventId

Enumerates the security events that can be reported from this manager.

#### See

- [WinccoaManager.securityEvent](#securityevent)

#### Enumeration Members

<a id="portopened"></a>

##### PortOpened

> **PortOpened**: `1`

Server port has been opened. Required additional parameters when calling
 [WinccoaManager.securityEvent](#securityevent):
- args[0] - port: number
- args[1] - protocolDetails: string (e.g. `'https://'`)

<a id="unknown"></a>

##### Unknown

> **Unknown**: `0`

Unknown ID - do not use

***

<a id="winccoasysconevent"></a>

### WinccoaSysConEvent

Enumerates the event types that can be used with [WinccoaSysConnect](#winccoasysconnect). For each
event, there is a corresponding data type containing the details of the event.

For details of the events, see also
[CTRL function `sysConnect()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlS_Z/sysConnect.html?hl=sysconnect).

> __NOTE__
>
> The following events available in CTRL are not available in TypeScript/JavaScript:
>
> | Event               | Alternative                                        |
> |---------------------|----------------------------------------------------|
> | `"exitRequested"`   | use `process.prependListener('exit', ...)` instead |
> | `"fswPathChanged"`  | use `fs.watch()` or related methods instead        |
> | `"reportRequested"` | not supported                                      |
>
> __NB:__ it is essential to use `process.prependListener()` (and not `process.on()`
> or `process.addListener()`) to ensure that the exit listener is executed before
> the connection to WinCC OA is closed.

#### Enumeration Members

<a id="dist"></a>

##### Dist

> **Dist**: `"dist"`

Get notified when DIST status changed. Listener will be called with
[WinccoaSysConDist](#winccoasyscondist) containing details.

<a id="dpalias"></a>

##### DpAlias

> **DpAlias**: `"dpAlias"`

Get notified when a data point alias changes. Listener will be called with
[WinccoaSysConDpChanged](#winccoasyscondpchanged) containing details.

<a id="dpcreated"></a>

##### DpCreated

> **DpCreated**: `"dpCreated"`

Get notified when a data point has been created. Listener will be called with
[WinccoaSysConDpDetails](#winccoasyscondpdetails) containing details.

<a id="dpdeleted"></a>

##### DpDeleted

> **DpDeleted**: `"dpDeleted"`

Get notified when a data point has been deleted. Listener will be called with
[WinccoaSysConDpDetails](#winccoasyscondpdetails) containing details.

<a id="dpdescription"></a>

##### DpDescription

> **DpDescription**: `"dpDescription"`

Get notified when a data point description changes. Listener will be called with
[WinccoaSysConDpDescription](#winccoasyscondpdescription) containing details.

<a id="dpformatunit"></a>

##### DpFormatUnit

> **DpFormatUnit**: `"dpFormatUnit"`

Get notified when a data point format and/or unit changes. Listener will be
called with [WinccoaSysConDpFormatUnit](#winccoasyscondpformatunit) containing details.

<a id="dprenamed"></a>

##### DpRenamed

> **DpRenamed**: `"dpRenamed"`

Get notified when a data point has been renamed. Listener will be called with
[WinccoaSysConDpChanged](#winccoasyscondpchanged) containing details.

<a id="dptypechanged"></a>

##### DpTypeChanged

> **DpTypeChanged**: `"dpTypeChanged"`

Get notified when a data point type has been changed. Listener will be called with
[WinccoaSysConDpTypeChanged](#winccoasyscondptypechanged) containing details.

<a id="dptypecreated"></a>

##### DpTypeCreated

> **DpTypeCreated**: `"dpTypeCreated"`

Get notified when a data point type has been created. Listener will be called with
[WinccoaSysConDpTypeDetails](#winccoasyscondptypedetails) containing details.

<a id="dptypedeleted"></a>

##### DpTypeDeleted

> **DpTypeDeleted**: `"dpTypeDeleted"`

Get notified when a data point type has been deleted. Listener will be called with
[WinccoaSysConDpTypeDetails](#winccoasyscondptypedetails) containing details.

<a id="redu"></a>

##### Redu

> **Redu**: `"redu"`

Get notified when REDU status changed. Listener will be called with
[WinccoaSysConRedu](#winccoasysconredu) containing details.

***

<a id="winccoatimeformat"></a>

### WinccoaTimeFormat

Enumerates the formats in which a time value (CTRL `time`) can be
returned by the API.

#### See

- [WinccoaOptions.timeFormat](#timeformat)

#### Enumeration Members

<a id="date"></a>

##### Date

> **Date**: `0`

Return time values as JavaScript `Date` objects.

<a id="number"></a>

##### Number

> **Number**: `1`

Return time values as `number` (milliseconds since Epoch).

## Classes

<a id="winccoaalerttime"></a>

### WinccoaAlertTime

Time of the alarm, with extra index for several simultaneous alarms

#### Constructors

<a id="constructor"></a>

##### Constructor

> **new WinccoaAlertTime**(`time`, `count`, `dpe`): [`WinccoaAlertTime`](#winccoaalerttime)

Constructor.

###### Parameters

###### time

[`WinccoaTime`](#winccoatime)

Time of alarm occurrence

###### count

`number`

Serial number

###### dpe

`string`

Data point element name

###### Returns

[`WinccoaAlertTime`](#winccoaalerttime)

###### See

- [WinccoaManager.alertSet](#alertset)
- [WinccoaManager.alertSetWait](#alertsetwait)
- [WinccoaManager.alertSetTimed](#alertsettimed)
- [WinccoaManager.alertSetTimedWait](#alertsettimedwait)

###### Example

#### TypeScript
``` ts
import { WinccoaManager, WinccoaAlertTime } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function alertTest() {
  const dpeWithAlert = 'ExampleDP_AlertHdl1.'; // assuming alert is triggered
  const result = await winccoa.dpQuery(
    "SELECT ALERT '_alert_hdl.._act_state', '_alert_hdl.._value' FROM '" +
      dpeWithAlert +
      "'",
  );

  const ts = result[result.length - 1][1] as WinccoaAlertTime;
  const alertTime = new WinccoaAlertTime(
    ts.time,
    ts.count,
    ts.dpe + '._comment',
  );
}
```
#### JavaScript
``` js
const { WinccoaManager, WinccoaAlertTime } = require('winccoa-manager');
const winccoa = new WinccoaManager();

async function alertTest() {
  const dpeWithAlert = 'ExampleDP_AlertHdl1.'; // assuming alert is triggered
  const result = await winccoa.dpQuery(
    "SELECT ALERT '_alert_hdl.._act_state', '_alert_hdl.._value' FROM '" +
      dpeWithAlert +
      "'",
  );

  const ts = result[result.length - 1][1];
  const alertTime = new WinccoaAlertTime(
    ts.time,
    ts.count,
    ts.dpe + '._comment',
  );
}
```

#### Properties

<a id="count"></a>

##### count

> **count**: `number`

Serial number

<a id="dpe"></a>

##### dpe

> **dpe**: `string`

Data point element name

<a id="time-2"></a>

##### time

> **time**: [`WinccoaTime`](#winccoatime)

Time of alarm occurrence

#### Accessors

<a id="date-1"></a>

##### date

###### Get Signature

> **get** **date**(): [`WinccoaTime`](#winccoatime)

###### Deprecated

Use [time](#time-2) instead.

###### Returns

[`WinccoaTime`](#winccoatime)

###### Set Signature

> **set** **date**(`value`): `void`

###### Deprecated

Use [time](#time-2) instead.

###### Parameters

###### value

[`WinccoaTime`](#winccoatime)

###### Returns

`void`

***

<a id="winccoacnsaccessright"></a>

### WinccoaCnsAccessRight

CNS Access right.

If the AccessRight is not defined at the node itself but inherited from
a parent node instead, the node ID of the parent node is returned for inheritedNode.
If the AccessRight is defined at the node itself, an empty string is defined for inheritedNode.

#### Constructors

<a id="constructor-1"></a>

##### Constructor

> **new WinccoaCnsAccessRight**(`accessRight`, `inheritedNode`): [`WinccoaCnsAccessRight`](#winccoacnsaccessright)

Constructor.

###### Parameters

###### accessRight

`number`

AccessRight as number

###### inheritedNode

`string`

Node from which the AccessRight is inherited

###### Returns

[`WinccoaCnsAccessRight`](#winccoacnsaccessright)

###### See

- [WinccoaManager.cnsGetAccessRight](#cnsgetaccessright)
- [WinccoaManager.cnsGetOPCAccessRight](#cnsgetopcaccessright)

###### Example

#### TypeScript
``` ts
import { WinccoaManager, WinccoaCnsAccessRight } from 'winccoa-manager';
const winccoa = new WinccoaManager();

function test() {
  const accessRight = winccoa.cnsGetOPCAccessRight('System1.View1:Node1');
  console.log(accessRight);
}
```

#### Properties

<a id="accessright"></a>

##### accessRight

> **accessRight**: `number`

AccessRight as number

<a id="inheritednode"></a>

##### inheritedNode

> **inheritedNode**: `string`

Node from which the AccessRight is inherited

***

<a id="winccoacnstreenode"></a>

### WinccoaCnsTreeNode

CNS Tree Node for a CNS tree.

#### Constructors

<a id="constructor-2"></a>

##### Constructor

> **new WinccoaCnsTreeNode**(`name`, `displayName`, `dp`, `children?`): [`WinccoaCnsTreeNode`](#winccoacnstreenode)

Constructor.

###### Parameters

###### name

`string`

Name as string

###### displayName

`unknown` = `''`

Display name of the new node as multi-language string.

###### dp

`string` = `''`

The data point (element) which is linked to the node as string.
       If no data point shall be linked an empty string can be defined.

###### children?

[`WinccoaCnsTreeNode`](#winccoacnstreenode)[]

Optional children which define subtree of the current tree node.

###### Returns

[`WinccoaCnsTreeNode`](#winccoacnstreenode)

###### See

- [WinccoaManager.cnsAddTree](#cnsaddtree)
- [WinccoaManager.cnsChangeTree](#cnschangetree)

###### Example

#### TypeScript
``` ts
import { WinccoaManager, WinccoaCnsTreeNode } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function test() {
  const tree = new WinccoaCnsTreeNode('CarTree', {'en': 'Car', 'de': 'Auto'}, '', [
    new WinccoaCnsTreeNode('B', 'B', '', [
      new WinccoaCnsTreeNode('dp', 'ExampleDP_Rpt1', 'System1:ExampleDP_Rpt1.')
    ]),
    new WinccoaCnsTreeNode('C')
  ]);

  try {
    await winccoa.cnsAddTree('System1.View1', tree);
  } catch(exc) {
    console.error(exc);
  }
}
```

#### Properties

<a id="children"></a>

##### children?

> `optional` **children**: [`WinccoaCnsTreeNode`](#winccoacnstreenode)[]

Optional children which define subtree of the current tree node.

<a id="displayname-1"></a>

##### displayName

> **displayName**: `unknown` = `''`

Display name of the new node as multi-language string.

<a id="dp-2"></a>

##### dp

> **dp**: `string` = `''`

The data point (element) which is linked to the node as string.
       If no data point shall be linked an empty string can be defined.

<a id="name-1"></a>

##### name

> **name**: `string`

Name as string

***

<a id="winccoaconfig"></a>

### WinccoaConfig

Helper class that simplifies access to data read from config files.
To be used together with [WinccoaManager.cfgReadContent](#cfgreadcontent).

#### Constructors

<a id="constructor-3"></a>

##### Constructor

> **new WinccoaConfig**(`data`): [`WinccoaConfig`](#winccoaconfig)

Constructor, to be called with the output of  [WinccoaManager.cfgReadContent](#cfgreadcontent).

###### Parameters

###### data

`object`

Configuration data as read by [WinccoaManager.cfgReadContent](#cfgreadcontent).

###### Returns

[`WinccoaConfig`](#winccoaconfig)

###### See

- [getString](#getstring) for an example.
- [WinccoaManager.cfgReadContent](#cfgreadcontent)

#### Properties

<a id="data-1"></a>

##### data

> `readonly` **data**: `object`

Configuration data that has been created by reading a config file with
[WinccoaManager.cfgReadContent](#cfgreadcontent). All getter methods of this instance
return setting from this object.

#### Methods

<a id="getnumber"></a>

##### getNumber()

> **getNumber**(`section`, `setting`): `undefined` \| `number`

Gets the numeric value of a single config setting as stored in [data](#data-1).

###### Parameters

###### section

`string`

Name of the config section.

###### setting

`string`

Name of the setting.

###### Returns

`undefined` \| `number`

Numeric value of the requested config setting. If __section__ or
         __setting__ are not found in [data](#data-1), `undefined` is returned.
         If __setting__ is contained in [data](#data-1) more than once, the
         last value is returned.
```ts
import { WinccoaConfig, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

function portNumbers() {
  const config = new WinccoaConfig(winccoa.cfgReadContent());
  const httpPort = config.getNumber('webClient', 'httpPort');
  const httpsPort = config.getNumber('webClient', 'httpsPort');
  return [httpPort, httpsPort];
}
```

<a id="getstring"></a>

##### getString()

> **getString**(`section`, `setting`): `undefined` \| `string`

Gets the string value of a single config setting as stored in [data](#data-1).

###### Parameters

###### section

`string`

Name of the config section.

###### setting

`string`

Name of the setting.

###### Returns

`undefined` \| `string`

String value of the requested config setting. If __section__ or
         __setting__ are not found in [data](#data-1), `undefined` is returned.
         If __setting__ is contained in [data](#data-1) more than once, the
         last value is returned.

###### See

- [getStringArray](#getstringarray)
 - [getNumber](#getnumber)

###### Example

```ts
import { WinccoaConfig, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

function langInfo() {
  const config = new WinccoaConfig(winccoa.cfgReadContent());
  const projLanguage = config.getString('general', 'lang');
  const allLanguages = config.getStringArray('general', 'langs');
  console.log(`Using ${projLanguage} from [${allLanguages}]`);
}
```

<a id="getstringarray"></a>

##### getStringArray()

> **getStringArray**(`section`, `setting`): `undefined` \| `string`[]

Gets the string value of a config setting as stored in [data](#data-1)
that can occur more than once in a config file (e.g. `langs`).

###### Parameters

###### section

`string`

Name of the config section.

###### setting

`string`

Name of the setting.

###### Returns

`undefined` \| `string`[]

One or more string values of the requested config setting.
         If __section__ or __setting__ are not found in [data](#data-1),
         `undefined` is returned.

###### See

- [getString](#getstring) for an example.
 - [getNumber](#getnumber)

***

<a id="winccoactrlscript"></a>

### WinccoaCtrlScript

Class that represents a CTRL script that can be called from JavaScript/TypeScript.
The necessary steps to call a CTRL function are:
1. Create an instance of [WinccoaCtrlScript](#winccoactrlscript).
2. Call a function in the script with [start](#start). This can be done several times,
   also for different functions contained in the script.

#### Example

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function ctrlScriptExample() {
  // create instance of script with CTRL code to execute
  const script = new WinccoaCtrlScript(
    winccoa,
    `dyn_string main(string pattern, bool empty = true)
     {
       return dpTypes(pattern, getSystemId(), empty);
     }`,
     'example script'
  );

  try {
    // call the script with two parameters
    const types = await script.start(
      'main',
      ['Ex*', false],
      [WinccoaCtrlType.string, WinccoaCtrlType.bool]
    ) as string[];

    // show result
    console.warn(types);
  } catch (exc) {
    console.error(exc);
  }
}
```

#### Constructors

<a id="constructor-4"></a>

##### Constructor

> **new WinccoaCtrlScript**(`manager`, `ctrlCode`, `name?`, `callback?`): [`WinccoaCtrlScript`](#winccoactrlscript)

Constructor. Creates an instance and initializes it with the CTRL code that will
be executed. A function in the script must then be started with a call to [start](#start).
For an example, see [WinccoaCtrlScript](#winccoactrlscript).

###### Parameters

###### manager

[`WinccoaManager`](#winccoamanager)

Manager instance that is used for getting the user ID and options
               to use for the subsequent call of [start](#start)

###### ctrlCode

`string`

CTRL code for the script. Must contain at least one CTRL function.

###### name?

`string`

Optional name for the script that will be shown in error messages.

###### callback?

[`WinccoaCtrlCallback`](#winccoactrlcallback)

If given, this function can be called from the CTRL script
                by using the CTRL function `callbackToJavaScript()`. See
                [WinccoaCtrlCallback](#winccoactrlcallback) for details and examples.

###### Returns

[`WinccoaCtrlScript`](#winccoactrlscript)

###### Throws

[WinccoaError](#winccoaerror) when `manager` is not the correct type or ctrlCode
                contains a syntax error.

###### See

WinccoaOptions

#### Properties

<a id="ctrlcode"></a>

##### ctrlCode

> `readonly` **ctrlCode**: `string`

CTRL code for the script. Must contain at least one CTRL function.

<a id="name-2"></a>

##### name?

> `optional` **name**: `string`

Optional name for the script that will be shown in error messages.

#### Methods

<a id="openpromisecount"></a>

##### openPromiseCount()

> **openPromiseCount**(): `number`

Returns the number of currently open Promises.

###### Returns

`number`

Number of Promises currently waiting for a function call to terminate.

<a id="start"></a>

##### start()

> **start**(`functionName`, `functionParams`, `paramTypes`, `callback?`): `Promise`\<`unknown`\>

Calls a CTRL function in the script set with the constructor. For each call,
a new CTRL thread is created.
For an example, see [WinccoaCtrlScript](#winccoactrlscript).

###### Parameters

###### functionName

`string` = `'main'`

Name of the CTRL function to call.

###### functionParams

`unknown`[] = `[]`

Parameters for the CTRL function.

###### paramTypes

Types of the parameters as expected by the CTRL function.
                  Note that in this context, it is not possible to determine
                  the required parameter types automatically, therefore it
                  is necessary to specify them explicitely.

For CTRL types that can contain different types (e.g. anytype, mixed, mapping),
the concrete types to which the values have to be converted before they are passed to
CTRL have to be provided.

For dynamic arrays containing a single datatype, it is recommended and more
efficient to use the specific type, e.g. [WinccoaCtrlType.dyn\_float](#dyn_float).

`unknown`[] | [`WinccoaCtrlType`](#winccoactrltype)[]

###### callback?

[`WinccoaCtrlCallback`](#winccoactrlcallback)

If given, this function can be called from the CTRL script
                by using the CTRL function `callbackToJavaScript()`. See
                [WinccoaCtrlCallback](#winccoactrlcallback) for details and examples.
> __NOTE__
>
> In general, it is preferable to use the __callback__ parameter of
> [WinccoaCtrlScript.constructor](#constructor-4) instead of this parameter.
>
> While this parameter here allows you to have different callback functions when
> [start](#start) is called more than once, this callback will only work when
> `callbackToJavaScript()` is called in the CTRL thread that has been
> created by the corresponding call to [start](#start).
>
> In particular, calling `callbackToJavaScript()` in a CTRL callback function
> (e.g. from `dpConnect()`) will only work when the __callback__ parameter of
> [WinccoaCtrlScript.constructor](#constructor-4) is used, but not with this function.

###### Returns

`Promise`\<`unknown`\>

Promise for the return value. Resolved when the function returns or
         rejected when the script is stopped (see [stop](#stop)).

###### Throws

[WinccoaError](#winccoaerror) when parameters cannot be properly converted or
        when a severe error happened in the script (which also stops the
        execution of the script). Note that CTRL warnings are only logged, but
        do not stop the execution of a script.

###### See

- [WinccoaCtrlType](#winccoactrltype)
- [WinccoaCtrlCallback](#winccoactrlcallback)

###### Examples

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

// for a simple argument list, just list the argument types
const ctrlCode = `double simpleArgs(int x, double y, string s)
{
  return (x * y) + s.length();
}`;
const script = new WinccoaCtrlScript(winccoa, ctrlCode, 'simple argument');
const result = await script.start(
  'simpleArgs',
  [12, 34.56, 'some text'],
  [WinccoaCtrlType.int, WinccoaCtrlType.double, WinccoaCtrlType.string]
) as number;
```

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

// for a dynamic array with a fixed type, use the corresponding type.
const ctrlCode = `int dynArg(dyn_string strings)
{
  for (int i = 0; i < strings.count(); i++)
    if (strings.at(i) == "found")
      return i;
  return -1;
}`;
const script = new WinccoaCtrlScript(winccoa, ctrlCode, 'dynamic arrays');
const result = await script.start(
  'dynArg',
  [['can', 'this', 'thing', 'be', 'found', 'in', 'here']],
  [WinccoaCtrlType.dyn_string]
) as number;
```

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

// for a dyn_anytype or dyn_mixed, list the types of all items
const ctrlCode = `string dynAnytypeArg(dyn_anytype things, bool other)
{
  if (!ignore)
    return "[" + things.count() + "] " + things;
  else
    return "";
}`;
const script = new WinccoaCtrlScript(winccoa, ctrlCode, 'dynamic arrays, variable types');
const result = await script.start(
  'dynAnytypeArg',
  [['title', 4711], false],
  [[WinccoaCtrlType.string, WinccoaCtrlType.int], WinccoaCtrlType.bool]
) as string;
```

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

// for a mapping, list the types of all fields
const ctrlCode = `mapping mappingArg(mapping values)
{
  values["square"] = values["a"] * values["a"];
  values["result"] = values["title"] + ": " + values["square"];
  return values;
}`;
const script = new WinccoaCtrlScript(winccoa, ctrlCode, 'mapping arguments');
const result = await script.start(
  'mappingArg',
  [{ title: 'This is the square', a: 3.01 }],
  [{ title: WinccoaCtrlType.string, a: WinccoaCtrlType.float }]
);
```

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

// for nested arguments, repeat the structure of the arguments,
replacing the values with their types
const ctrlCode = `void nestedArg(dyn_anytype things)
{
  DebugTN(things);
}`;
const script = new WinccoaCtrlScript(winccoa, ctrlCode, 'nested arguments');
await script.start(
  'nestedArg',
  [
    [
      [1, 2, 3],
      { a: 4.3, b: 'text' },
      ['something', 12.34, { yes: true, no: false }],
    ],
  ],
  [
    [
      WinccoaCtrlType.dyn_int,
      { a: WinccoaCtrlType.float, b: WinccoaCtrlType.string },
      [
        WinccoaCtrlType.string,
        WinccoaCtrlType.float,
        { yes: WinccoaCtrlType.bool, no: WinccoaCtrlType.bool },
      ],
    ],
  ]
);
```

```ts
import {
  WinccoaManager,
  WinccoaCtrlScript,
  WinccoaCtrlType,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function parallelCtrlThreads() {
  const script = new WinccoaCtrlScript(
    winccoa,
    `int countMilliSeconds(int count, int delayMs)
     {
       for (int i = 1; i <= count; i++)
         delay(0, delayMs);
       return count * delayMs;
     }

     int countSeconds(int count, int delaySec)
     {
       for (int i = 1; i <= count; i++)
         delay(delaySec);
        return count * delaySec * 1000;
    }`,
    'parallel CTRL threads'
  );

  // start three parallel CTRL threads and collect all results
  const result = await Promise.allSettled([
    script.start(
      'countMilliSeconds',
      [10, 250],
      [WinccoaCtrlType.int, WinccoaCtrlType.int],
    ),
    script.start(
      'countSeconds',
      [5, 1],
      [WinccoaCtrlType.int, WinccoaCtrlType.int],
    ),
    script.start(
      'countSeconds',
      [3, 2],
      [WinccoaCtrlType.int, WinccoaCtrlType.int],
    ),
  ]);

  console.info(result);
}
```

<a id="stop"></a>

##### stop()

> **stop**(): `void`

Stops all threads currently running in this instance.

For stopping running threads, the call to [stop](#stop) must come
from a different part of the code than the `await` [start](#start).
(e.g. from a `setTimeout` callback). An alternative to that is
to use [start](#start) without `await` and handle the Promise later
(e. g. with `Promise.allSettled()`);

###### Returns

`void`

###### Example

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

const ctrlScript = `int count(int tenths)
{
  int i;
  for(i = 1; i <= tenths; i++)
     delay(0, 100);
  return i - 1;
}`;
const script = new WinccoaCtrlScript(winccoa, ctrlScript, 'stop example');

// stop script after 2 seconds
setTimeout(() => script.stop(), 2000);

try {
  result = await script.start('count', [500], [WinccoaCtrlType.int]) as number;
} catch (exc) {
  // interrupted
}
```

<a id="fromfile"></a>

##### fromFile()

> `static` **fromFile**(`manager`, `fileName`, `name?`, `callback?`): `Promise`\<[`WinccoaCtrlScript`](#winccoactrlscript)\>

Creates an instance of [WinccoaCtrlScript](#winccoactrlscript) containing CTRL code loaded from a file.

###### Parameters

###### manager

[`WinccoaManager`](#winccoamanager)

Manager instance that is used for getting the user ID and options
               to use for the subsequent call of [start](#start)

###### fileName

`string`

Name of the CTRL file to load. If this is a relative path, `fileName`
                is searched in all script directories in the usual order. If this is
                an absolute path, it is used unchanged. The content of the CTRL file
                must be encoded using UTF-8. If `fileName` has no extension, `.ctl`
                will be appended.
> Note that the CTRL code must not be encyrpted (files with extension `.ctc` cannot be loaded).

###### name?

`string`

Optional name for the script that will be shown in error messages. If not
            given, `fileName` is used in error messages.

###### callback?

[`WinccoaCtrlCallback`](#winccoactrlcallback)

If given, this function can be called from the CTRL script
                by using the CTRL function `callbackToJavaScript()`. See
                [WinccoaCtrlCallback](#winccoactrlcallback) for details and examples.

###### Returns

`Promise`\<[`WinccoaCtrlScript`](#winccoactrlscript)\>

Instance containing the CTRL code loaded from `fileName`.

###### Throws

- [WinccoaError](#winccoaerror) when `manager` is not the correct type or ctrlCode
                contains a syntax error.
- Errors from `node:fs` when `fileName` cannot be found or opened.

###### Example

```ts
import { WinccoaCtrlScript, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function loadScriptTest() {
  const script = await WinccoaCtrlScript.fromFile(
    winccoa,
    'myScript'  // CTRL file myScript.ctl must exist in a script directory
  );
  ...
}
```

***

<a id="winccoactrlscriptcache"></a>

### WinccoaCtrlScriptCache

Helper class for caching multiple instances of a CTRL script (initialized
for different users if necessary). This helps improving performance when
the same CTRL script is called multiple times by the same or different users.

#### Constructors

<a id="constructor-5"></a>

##### Constructor

> **new WinccoaCtrlScriptCache**(`manager`, `ctrlCode`, `name?`, `callback?`): [`WinccoaCtrlScriptCache`](#winccoactrlscriptcache)

Constructor.

###### Parameters

###### manager

[`WinccoaManager`](#winccoamanager)

Manager instance which is used for two things:
- Getting [WinccoaOptions](#winccoaoptions) for converting return values.
- Getting the current user for [getScript](#getscript).
> Note that this instance only keeps a weak reference to __manager__
> which can become invalid if __manager__ gets freed by the
> garbage collector (see [isValid](#isvalid)).

###### ctrlCode

`string`

CTRL code of the scripts that will be
                returned by [getScript](#getscript).

###### name?

`string`

Optional name for the script that will be shown in error messages.

###### callback?

[`WinccoaCtrlCallback`](#winccoactrlcallback)

If given, this function can be called from the CTRL script
                by using the CTRL function `callbackToJavaScript()`. See
                [WinccoaCtrlCallback](#winccoactrlcallback) for details and examples.

###### Returns

[`WinccoaCtrlScriptCache`](#winccoactrlscriptcache)

###### See

- [WinccoaCtrlScript](#winccoactrlscript)

###### Example

```ts
import {
  WinccoaCtrlScriptCache,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function scriptCacheTest() {
  // store the script in a cache for repeated use
  const cache = new WinccoaCtrlScriptCache(
    winccoa,
    `double simpleArgs(int x, double y, string s)
     {
       return (x * y) + s.length();
     }`,
    'simple args cache example'
  );

  for (let i = 1; i <= 20; i++) {
    const result = (await cache
      .getScript()
      .start(
        'simpleArgs',
        [i, 34.56, 'some text'],
        [WinccoaCtrlType.int, WinccoaCtrlType.double, WinccoaCtrlType.string],
      )) as number;
    console.log(result);
  }
}

void scriptCacheTest();
```

#### Properties

<a id="ctrlcode-1"></a>

##### ctrlCode

> `readonly` **ctrlCode**: `string`

CTRL code of the scripts that will be
                returned by [getScript](#getscript).

<a id="name-3"></a>

##### name?

> `readonly` `optional` **name**: `string`

Optional name for the script that will be shown in error messages.

#### Methods

<a id="getscript"></a>

##### getScript()

> **getScript**(): [`WinccoaCtrlScript`](#winccoactrlscript)

Returns an instance of [WinccoaCtrlScript](#winccoactrlscript) initialized with __ctrlCode__
for __manager__'s current user.

###### Returns

[`WinccoaCtrlScript`](#winccoactrlscript)

Cached (possibly newly created) instance of a [WinccoaCtrlScript](#winccoactrlscript).

###### See

- [constructor](#constructor-5) for an example.

<a id="isvalid"></a>

##### isValid()

> **isValid**(): `boolean`

Indicates whether this instance is valid (that is, whether the weak reference
to its __manager__ is still valid).

###### Returns

`boolean`

<a id="fromfile-2"></a>

##### fromFile()

> `static` **fromFile**(`manager`, `fileName`, `name?`, `callback?`): `Promise`\<[`WinccoaCtrlScriptCache`](#winccoactrlscriptcache)\>

Creates an instance of [WinccoaCtrlScriptCache](#winccoactrlscriptcache) containing CTRL code loaded from a file.

###### Parameters

###### manager

[`WinccoaManager`](#winccoamanager)

Manager instance which is used for two things:
- Getting [WinccoaOptions](#winccoaoptions) for converting return values.
- Getting the current user for [getScript](#getscript).
> Note that this instance only keeps a weak reference to __manager__
> which can become invalid if __manager__ gets freed by the
> garbage collector (see [isValid](#isvalid)).

###### fileName

`string`

Name of the CTRL file to load. If this is a relative path, `fileName`
                is searched in all script directories in the usual order. If this is
                an absolute path, it is used unchanged. The content of the CTRL file
                must be encoded using UTF-8. If `fileName` has no extension, `.ctl`
                will be appended.
> Note that the CTRL code must not be encyrpted (files with extension `.ctc` cannot be loaded).

###### name?

`string`

Optional name for the script that will be shown in error messages. If not
            given, `fileName` is used in error messages.

###### callback?

[`WinccoaCtrlCallback`](#winccoactrlcallback)

If given, this function can be called from the CTRL script
                by using the CTRL function `callbackToJavaScript()`. See
                [WinccoaCtrlCallback](#winccoactrlcallback) for details and examples.

###### Returns

`Promise`\<[`WinccoaCtrlScriptCache`](#winccoactrlscriptcache)\>

Instance containing the CTRL code loaded from `fileName`.

###### Throws

- [WinccoaError](#winccoaerror) when `manager` is not the correct type or ctrlCode
                contains a syntax error.
- Errors from `node:fs` when `fileName` cannot be found or opened.

###### Example

```ts
import { WinccoaCtrlScriptCache, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function loadScriptTest() {
  const script = await WinccoaCtrlScriptCache.fromFile(
    winccoa,
    'myScript'  // CTRL file myScript.ctl must exist in a script directory
  );
  ...
}
```

***

<a id="winccoadptypenode"></a>

### WinccoaDpTypeNode

Tree Node for a Data point Type tree.

#### See

- [WinccoaManager.dpTypeGet](#dptypeget)
- [WinccoaManager.dpTypeChange](#dptypechange)
- [WinccoaManager.dpTypeCreate](#dptypecreate)
- [WinccoaElementType](#winccoaelementtype)

#### Example

``` ts
const tree =
  new WinccoaDpTypeNode('MyType1', WinccoaElementType.Struct, '', [
    new WinccoaDpTypeNode('id', WinccoaElementType.Int),
    new WinccoaDpTypeNode('text', WinccoaElementType.String),
    new WinccoaDpTypeNode('typeRef', WinccoaElementType.Typeref, 'ExampleDP_Float'),
    new WinccoaDpTypeNode('struct', WinccoaElementType.Struct, '', [
      new WinccoaDpTypeNode('id2', WinccoaElementType.Int),
      new WinccoaDpTypeNode('text2', WinccoaElementType.String)
    ])
  ]);
console.log(await winccoa.dpTypeChange(tree));
```

#### Constructors

<a id="constructor-6"></a>

##### Constructor

> **new WinccoaDpTypeNode**(`name`, `type`, `refName`, `children`, `newName`): [`WinccoaDpTypeNode`](#winccoadptypenode)

Constructor.

###### Parameters

###### name

`string`

The Data point Type name.

###### type

[`WinccoaElementType`](#winccoaelementtype)

The Data point Type data type ([WinccoaElementType](#winccoaelementtype)).

###### refName

`string` = `''`

Optional reference Data point Type name.

###### children

[`WinccoaDpTypeNode`](#winccoadptypenode)[] = `[]`

Optional children which define subtree of the current tree node.

###### newName

`string` = `''`

Optional new name (only for [WinccoaManager.dpTypeChange](#dptypechange)).

###### Returns

[`WinccoaDpTypeNode`](#winccoadptypenode)

#### Properties

<a id="children-1"></a>

##### children

> **children**: [`WinccoaDpTypeNode`](#winccoadptypenode)[] = `[]`

Optional children which define subtree of the current tree node.

<a id="name-4"></a>

##### name

> **name**: `string`

The Data point Type name.

<a id="newname"></a>

##### newName

> **newName**: `string` = `''`

Optional new name (only for [WinccoaManager.dpTypeChange](#dptypechange)).

<a id="refname"></a>

##### refName

> **refName**: `string` = `''`

Optional reference Data point Type name.

<a id="type"></a>

##### type

> **type**: [`WinccoaElementType`](#winccoaelementtype)

The Data point Type data type ([WinccoaElementType](#winccoaelementtype)).

***

<a id="winccoaerror"></a>

### WinccoaError

Error class that contains additional information found in WinCC OA errors, like
the WinCC OA error code.

#### Examples

```ts
import { WinccoaManager, WinccoaError } from 'winccoa-manager';
const winccoa = new WinccoaManager();

try {
   ...
} catch(exc) {
  // standard reporting
  console.error(exc);

  // access the details
  var oaError = exc as WinccoaError;
  console.warn('Error code    : ' + oaError.code);
  console.warn('Error message : ' + oaError.message);
  console.warn('Catalogue     : ' + oaError.catalog);
  console.warn('Details       : ' + oaError.details);
}
```

```js
const { WinccoaManager } = require('winccoa-manager');
const winccoa = new WinccoaManager();

try {
   ...
} catch(exc) {
  // standard reporting
  console.error(exc);

  // access the details
  console.warn('Error code    : ' + exc.code);
  console.warn('Error message : ' + exc.message);
  console.warn('Catalogue     : ' + exc.catalog);
  console.warn('Details       : ' + exc.details);
}
```

#### Extends

- `Error`

#### Constructors

<a id="constructor-7"></a>

##### Constructor

> **new WinccoaError**(`code`, `message`, `catalog?`, `details?`, `priority?`, `errorType?`, `dpe?`, `userId?`, `errorTime?`): [`WinccoaError`](#winccoaerror)

Constructor. This constructor is also used by the [WinccoaManager](#winccoamanager) to create
[WinccoaError](#winccoaerror) instances.

###### Parameters

###### code

WincCC OA error code. This can either be a number (like 71 for "DP does
            not exist") or a string. The meaning of string error codes can be found
            in the corresponding __catalog__.

`string` | `number`

###### message

`string`

Error message corresponding to __code__.

###### catalog?

`string`

Name of the error catalog where the error message can be found. If
               empty, this refers to catalog `_errors.cat`.

###### details?

`unknown`

Additional details specific to that error. Not all errors provide
               this information.

###### priority?

`number`

Optional priority.

###### errorType?

`number`

Optional errorType.

###### dpe?

`string`

Optional data point.

###### userId?

`number`

Optional userId.

###### errorTime?

[`WinccoaTime`](#winccoatime)

Optional time when error occured in milliseconds since 1.1.1970.

###### Returns

[`WinccoaError`](#winccoaerror)

###### Overrides

`Error.constructor`

##### Constructor

> **new WinccoaError**(`code`): [`WinccoaError`](#winccoaerror)

Constructor. This constructor is also used by the [WinccoaManager](#winccoamanager) to create
[WinccoaError](#winccoaerror) instances.
The __code__ member will be set to MULTIPLE_ERRORS_CODE and __Error.message__ contains at most 10 errors ordered by importance.
An error is important if the priority is <= WinccoaErrorPriority.Severe (see [WinccoaErrorPriority](#winccoaerrorpriority)).

###### Parameters

###### code

[`WinccoaError`](#winccoaerror)[]

Array of WincCC OA errors which are in the __details__ member.

###### Returns

[`WinccoaError`](#winccoaerror)

###### See

[multipleErrors](#multipleerrors)

###### Overrides

`Error.constructor`

#### Properties

<a id="catalog"></a>

##### catalog

> **catalog**: `string` = `''`

<a id="code"></a>

##### code

> **code**: `string` \| `number` \| [`WinccoaError`](#winccoaerror)[]

<a id="details"></a>

##### details?

> `optional` **details**: `unknown`

<a id="dpe-1"></a>

##### dpe?

> `optional` **dpe**: `string`

<a id="errortime"></a>

##### errorTime?

> `optional` **errorTime**: [`WinccoaTime`](#winccoatime)

<a id="errortype"></a>

##### errorType?

> `optional` **errorType**: [`WinccoaErrorType`](#winccoaerrortype)

<a id="message"></a>

##### message

> **message**: `string`

###### Inherited from

`Error.message`

<a id="name-5"></a>

##### name

> **name**: `string`

###### Inherited from

`Error.name`

<a id="priority"></a>

##### priority?

> `optional` **priority**: [`WinccoaErrorPriority`](#winccoaerrorpriority)

<a id="stack"></a>

##### stack?

> `optional` **stack**: `string`

###### Inherited from

`Error.stack`

<a id="userid"></a>

##### userId?

> `optional` **userId**: `number`

<a id="multiple_errors_code"></a>

##### MULTIPLE\_ERRORS\_CODE

> `readonly` `static` **MULTIPLE\_ERRORS\_CODE**: `10000` = `10000`

Code for multiple errors in details.
__details__ is in that case an array of WinccoaError instances.

<a id="stacktracelimit"></a>

##### stackTraceLimit

> `static` **stackTraceLimit**: `number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured _after_ the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

###### Inherited from

`Error.stackTraceLimit`

#### Accessors

<a id="multipleerrors"></a>

##### multipleErrors

###### Get Signature

> **get** **multipleErrors**(): `boolean`

###### Returns

`boolean`

true if details contains multiple (at least 2) WinccoaError instances.

#### Methods

<a id="tostring"></a>

##### toString()

> **toString**(): `string`

###### Returns

`string`

code and message from all errors

<a id="capturestacktrace"></a>

##### captureStackTrace()

> `static` **captureStackTrace**(`targetObject`, `constructorOpt?`): `void`

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack;  // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

###### Parameters

###### targetObject

`object`

###### constructorOpt?

`Function`

###### Returns

`void`

###### Inherited from

`Error.captureStackTrace`

<a id="preparestacktrace"></a>

##### prepareStackTrace()

> `static` **prepareStackTrace**(`err`, `stackTraces`): `any`

###### Parameters

###### err

`Error`

###### stackTraces

`CallSite`[]

###### Returns

`any`

###### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

###### Inherited from

`Error.prepareStackTrace`

***

<a id="winccoamanager"></a>

### WinccoaManager

Main class of the TypeScript/JavaScript API to the __WinCC OA JavaScript Manager for Node.js&#174;__.

> **IMPORTANT**
>
> All methods described in this documentation must be __called from code inside a
> method or function__ to prevent unexpected or undefined behavior.

To use the API, an instance of this class needs to be created, e. g.:

#### Example

```ts
import { WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();
```

#### Constructors

##### Constructor

> **new WinccoaManager**(`options?`): [`WinccoaManager`](#winccoamanager)

Constructor - creates new instance of an API object.

###### Parameters

###### options?

`Partial`\<`Omit`\<[`WinccoaOptions`](#winccoaoptions), `"userId"`\>\>

Options that are used to initialize the instance, see [setOptions](#setoptions) for details.

###### Returns

[`WinccoaManager`](#winccoamanager)

###### See

- [WinccoaOptions](#winccoaoptions)
- [setOptions](#setoptions)

###### Examples

```ts
import { WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();
```

```ts
import {
  WinccoaLangStringFormat,
  WinccoaManager,
  WinccoaTimeFormat,
} from 'winccoa-manager';
const winccoa = new WinccoaManager({
  timeFormat: WinccoaTimeFormat.Number,
  langStringFormat: WinccoaLangStringFormat.Object,
  longAsBigInt: true,
});
```

#### Alert

<a id="alertget"></a>

##### alertGet()

> **alertGet**(`alertsTime`, `dpeNames`, `alertCount?`): `Promise`\<`unknown`\>

The function does the query only of the last alert attributes of a data point.

###### Parameters

###### alertsTime

Alert(s) time of type [WinccoaAlertTime](#winccoaalerttime).

[`WinccoaAlertTime`](#winccoaalerttime) | [`WinccoaAlertTime`](#winccoaalerttime)[]

###### dpeNames

Data point element name(s) with the alert config.

`string` | `string`[]

###### alertCount?

Serial number of alert (optional).

`number` | `number`[]

###### Returns

`Promise`\<`unknown`\>

Promise that resolves to the requested value(s) of the DPE(s). The received values
         must be cast to their expected types before they can be used.

> __NOTE__
>
> The function can accept a list of data points for a single alert time.
> In this case, the data point should be the same, but the alert configs are different:
>
>`winccoa.alertGet(alertTime, [dpe + ':_alert_hdl.._value', dpe + ':_alert_hdl.._text']);`.
>
> The function can accept a list of alert times and a list of data points.
> In this case all lists must have the same length:
>
>`winccoa.alertGet([alertTime1, alertTime2], ['dpe1', 'dpe2']);`

###### Throws

[WinccoaError](#winccoaerror) when DPE does not exist or current user has no read access to it.

###### See

- [CTRL function `alertGet()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/alertGet.html)
- [alertSet](#alertset)

###### Examples

```ts
import { WinccoaManager, WinccoaAlertTime } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function alertGetTest() {
  const dpe = 'ExampleDP_AlertHdl1.';
  try {
    await winccoa.dpSet(dpe, true);  // trigger alert on the dpe
    const result = await winccoa.dpQuery(
      "SELECT ALERT '_alert_hdl.._value' FROM '" +
      dpe +
      "'",
    );

    for (let i = 1; i < result.length; i++) {
      const alertTime = result[i][1];
      const values = (await winccoa.alertGet(alertTime,
                     [dpe + ':_alert_hdl.._value', dpe + ':_alert_hdl.._text'])) as [boolean, WinccoaLangString];
      console.info(dpe, values);
    }
  } catch (exc) {
    console.error(exc);
  }
}
```

```ts
import { WinccoaManager, WinccoaAlertTime } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function alertGetTest() {
  const dpes = ['ExampleDP_AlertHdl1.', 'ExampleDP_AlertHdl2.'];
 try {
   await winccoa.dpSet(dpes, [true, true]);  // trigger alert on the dpes
   let alertTimes: WinccoaAlertTime[] = [];
   for (let d = 0; d < dpes.length; d++)
   {
     const result = await winccoa.dpQuery(
       "SELECT ALERT '_alert_hdl.._value' FROM '" +
       dpes[d] +
       "'",
     );

     if (result.length > 1)
       alertTimes.push(result[1][1]);
   }

   if (dpes.length == alertTimes.length)
   {
     const values = await winccoa.alertGet(alertTimes, [dpes[0] + ':_alert_hdl.._value', dpes[1] + ':_alert_hdl.._value']);
     console.info(dpes, values);
   }
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="alertgetperiod"></a>

##### alertGetPeriod()

> **alertGetPeriod**(`startTime`, `endTime`, `names`): `Promise`\<\{ `alertTimes`: [`WinccoaAlertTime`](#winccoaalerttime)[]; `values`: `unknown`[]; \}\>

The function returns the values of the specified alert attributes of the data point elements
for which alerts were triggered.

###### Parameters

###### startTime

[`WinccoaTime`](#winccoatime)

The start time for reading alerts.

###### endTime

[`WinccoaTime`](#winccoatime)

The end time for reading alerts.

###### names

Alert handling attribute names.

`string` | `string`[]

###### Returns

`Promise`\<\{ `alertTimes`: [`WinccoaAlertTime`](#winccoaalerttime)[]; `values`: `unknown`[]; \}\>

Promise that resolves to an object containing two arrays, one containing [WinccoaAlertTime](#winccoaalerttime)s
         with the alert details and the other the corresponding values.

###### Throws

[WinccoaError](#winccoaerror) when alert attribute name does not exist or in case of an invalid argument type.

###### See

- [CTRL function `alertGetPeriod()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/alertGetPeriod.html)
- [alertGet](#alertget)
- [alertSet](#alertset)

###### Example

```ts
const startTime = new Date('2024-10-25T12:00:00.789Z');
const currentTime = new Date();
const dpes = [':_alert_hdl.._value', ':_alert_hdl.._text']

const { alertTimes, values } = await winccoa.alertGetPeriod(
  startTime,
  currentTime,
  dpes,
);

for (let i = 0; i < alertTimes.length; i++) {
  const alertTime: WinccoaAlertTime = alertTimes[i];
  console.info(
    '#' + i,
    'alertTime: ' + alertTime.time,
    alertTime.count,
    alertTime.dpe,
  );
  console.info('#' + i, 'value: ' + values[i]);
}
```

<a id="alertset"></a>

##### alertSet()

> **alertSet**(`alerts`, `values`): `boolean`

Allows to set data point alert attributes.

###### Parameters

###### alerts

Alert(s) of type [WinccoaAlertTime](#winccoaalerttime) to be set.

[`WinccoaAlertTime`](#winccoaalerttime) | [`WinccoaAlertTime`](#winccoaalerttime)[]

###### values

`unknown`

Attribute value(s) to be set. Must have the same size as __alerts__. If __alerts__ is a
              single string and not an array, this parameter must also be a single value and not an array.

###### Returns

`boolean`

Boolean `true` in case of a success, otherwise [WinccoaError](#winccoaerror) wil be thrown instead.

###### Remarks

The attributes and their constants which can be set with this method are described in the chapter
[_alert_hdl](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Notes/dpconfig_alert_hdl.html)

###### Throws

[WinccoaError](#winccoaerror) when DPE does not exist, mismatch number of DPs and values,
invalid argument type, etc.

###### See

- [alertSetWait](#alertsetwait)
- [alertSetTimed](#alertsettimed)
- [alertSetTimedWait](#alertsettimedwait)
- [WinccoaAlertTime](#winccoaalerttime)
- [_alert_hdl](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Notes/dpconfig_alert_hdl.html)

###### Example

```ts
import { WinccoaManager, WinccoaAlertTime } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function alertSetTest() {
  const dpeWithAlert = 'ExampleDP_AlertHdl1.';  // assuming alert is triggered
  const result = await winccoa.dpQuery(
    "SELECT ALERT '_alert_hdl.._act_state', '_alert_hdl.._value' FROM '" +
    dpeWithAlert +
    "'",
  );

  const ts = result[result.length - 1][1] as WinccoaAlertTime;
  const alertTime = new WinccoaAlertTime(ts.time, ts.count, ts.dpe + '._comment');
  let isSuccess = false;
  try {
    isSuccess = winccoa.alertSet(alertTime, 'Alert comment text from winccoa node manager.');
  } catch (exc) {
    console.error(exc);
  }

  console.info("AlertSet is called successfully - " + isSuccess);
}
```

<a id="alertsettimed"></a>

##### alertSetTimed()

> **alertSetTimed**(`time`, `alerts`, `values`): `boolean`

Allows to set data point alert attributes with a given timestamp.

###### Parameters

###### time

[`WinccoaTime`](#winccoatime)

Source time for the attribute change.

###### alerts

Alert(s) of type [WinccoaAlertTime](#winccoaalerttime) to be set.

[`WinccoaAlertTime`](#winccoaalerttime) | [`WinccoaAlertTime`](#winccoaalerttime)[]

###### values

`unknown`

Attribute value to be set. Must have the same size as __alerts__. If __alerts__ is a
              single string and not an array, this parameter must also be a single value and not an array.

###### Returns

`boolean`

Boolean `true` in case of a success, otherwise [WinccoaError](#winccoaerror) wil be thrown instead.

###### Remarks

The attributes and their constants which can be set with this method are described in the chapter
[_alert_hdl](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Notes/dpconfig_alert_hdl.html)

###### Throws

[WinccoaError](#winccoaerror) when DPE does not exist, mismatch number of DPs and values,
invalid argument type, etc.

###### See

- [alertSet](#alertset)
- [alertSetWait](#alertsetwait)
- [alertSetTimedWait](#alertsettimedwait)
- [WinccoaAlertTime](#winccoaalerttime)
- [_alert_hdl](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Notes/dpconfig_alert_hdl.html)

###### Example

```ts
import { WinccoaManager, WinccoaAlertTime } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function alertSetTimedTest() {
  const dpeWithAlert = 'ExampleDP_AlertHdl1.';  // assuming alert is triggered
  const result = await winccoa.dpQuery(
    "SELECT ALERT '_alert_hdl.._act_state', '_alert_hdl.._value' FROM '" +
    dpeWithAlert +
    "'",
  );

  const timeStamp = new Date('2024-03-19T04:05:06.789Z');
  const ts = result[result.length - 1][1] as WinccoaAlertTime;
  const alertTime = new WinccoaAlertTime(ts.time, ts.count, ts.dpe + '._ack_state');
  let isSuccess = false;
  try {
    isSuccess = winccoa.alertSetTimed(timeStamp, alertTime, 1);
  } catch (exc) {
    console.error(exc);
  }

  console.info("AlertSet is called successfully - " + isSuccess);
}
```

<a id="alertsettimedwait"></a>

##### alertSetTimedWait()

> **alertSetTimedWait**(`time`, `alerts`, `values`): `Promise`\<`unknown`\>

Allows to set data point alert attributes with a given timestamp.

###### Parameters

###### time

[`WinccoaTime`](#winccoatime)

Source time for the attribute change.

###### alerts

Alert(s) of type [WinccoaAlertTime](#winccoaalerttime) to be set.

[`WinccoaAlertTime`](#winccoaalerttime) | [`WinccoaAlertTime`](#winccoaalerttime)[]

###### values

`unknown`

Attribute value to be set. Must have the same size as __alerts__. If __alerts__ is a
              single string and not an array, this parameter must also be a single value and not an array.

###### Returns

`Promise`\<`unknown`\>

Promise that resolves to `true` if successful. If not successful,
         a [WinccoaError](#winccoaerror) wil be thrown instead.

###### Remarks

The attributes and their constants which can be set with this method are described in the chapter
[_alert_hdl](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Notes/dpconfig_alert_hdl.html)

###### Throws

[WinccoaError](#winccoaerror) when DPE does not exist, mismatch number of DPs and values,
invalid argument type, etc.

###### See

- [alertSet](#alertset)
- [alertSetWait](#alertsetwait)
- [alertSetTimed](#alertsettimed)
- [WinccoaAlertTime](#winccoaalerttime)
- [_alert_hdl](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Notes/dpconfig_alert_hdl.html)

###### Example

```ts
import { WinccoaManager, WinccoaAlertTime } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function alertSetTimedWaitTest() {
  const dpeWithAlert = 'ExampleDP_AlertHdl1.'; // assuming alert is triggered
  const result = await winccoa.dpQuery(
    `SELECT ALERT '_alert_hdl.._act_state', '_alert_hdl.._value' FROM '${dpeWithAlert}'`,
  );

  const timeStamp = new Date('2024-03-19T04:05:06.789Z');
  const ts = result[result.length - 1][1] as WinccoaAlertTime;
  const alertTime = new WinccoaAlertTime(
    ts.time,
    ts.count,
    ts.dpe + '._ack_state',
  );

  try {
    await winccoa.alertSetTimedWait(timeStamp, alertTime, 1);
    console.info(`Alert is acknowledged at ${timeStamp}`);
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="alertsetwait"></a>

##### alertSetWait()

> **alertSetWait**(`alerts`, `values`): `Promise`\<`unknown`\>

Allows to set data point alert attributes.

###### Parameters

###### alerts

Alert(s) of type [WinccoaAlertTime](#winccoaalerttime) to be set.

[`WinccoaAlertTime`](#winccoaalerttime) | [`WinccoaAlertTime`](#winccoaalerttime)[]

###### values

`unknown`

Attribute value(s) to be set. Must have the same size as __alerts__. If __alerts__ is a
              single string and not an array, this parameter must also be a single value and not an array.

###### Returns

`Promise`\<`unknown`\>

Promise that resolves to `true` if successful. If not successful,
         a [WinccoaError](#winccoaerror) wil be thrown instead.

###### Remarks

The attributes and their constants which can be set with this method are described in the chapter
[_alert_hdl](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Notes/dpconfig_alert_hdl.html)

###### Throws

[WinccoaError](#winccoaerror) when DPE does not exist, mismatch number of DPs and values,
invalid argument type, etc.

###### See

- [alertSet](#alertset)
- [alertSetTimed](#alertsettimed)
- [alertSetTimedWait](#alertsettimedwait)
- [WinccoaAlertTime](#winccoaalerttime)
- [_alert_hdl](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Notes/dpconfig_alert_hdl.html)

###### Example

```ts
import { WinccoaManager, WinccoaAlertTime } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function alertSetWaitTest() {
  const dpeWithAlert = 'ExampleDP_AlertHdl1.'; // assuming alert is triggered
  const result = await winccoa.dpQuery(
    `SELECT ALERT '_alert_hdl.._act_state', '_alert_hdl.._value' FROM '${dpeWithAlert}'`,
  );

  const ts = result[result.length - 1][1] as WinccoaAlertTime;
  const alertTime = new WinccoaAlertTime(
    ts.time,
    ts.count,
    ts.dpe + '._comment',
  );

  try {
    await winccoa.alertSetWait(
      alertTime,
      'Alert comment text from winccoa node manager.',
    );
    console.info(`Comment for alert of '${dpeWithAlert}' is successfully set`);
  } catch (exc) {
    console.error(exc);
  }
}
```

#### CNS

<a id="cns_checkid"></a>

##### cns\_checkId()

> **cns\_checkId**(`id`): `Promise`\<`boolean`\>

Checks whether __id__ is a vaild CNS ID.

###### Parameters

###### id

`string`

ID to check

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if __id__ is a
         valid ID or to `false` if not.

###### See

[CTRL function `cns_checkId()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_checkId.html)

###### Example

```ts
const isValid = await winccoa.cns_checkId('someId');
```

<a id="cns_checkname"></a>

##### cns\_checkName()

> **cns\_checkName**(`name`): `Promise`\<`number`\>

Checks whether __name__ is a valid display name for CNS.

###### Parameters

###### name

[`WinccoaLangString`](#winccoalangstring)

Display name to check.

###### Returns

`Promise`\<`number`\>

Promise - will be resolved to:
- ` 0` - valid name
- `-1` - incomplete `langString`
- `-2` - contains invalid characters

###### See

[CTRL function `cns_checkName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_checkName.html)

###### Example

```ts
import { WinccoaLangString, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function test(name: WinccoaLangString) {
  switch (await winccoa.cns_checkName(name)) {
    case 0:
      console.info('valid CNS display name');
      break;
    case -1:
      console.error('incomplete langString');
      break;
    case -2:
      console.error('contains invalid characters');
      break;
  }
}
```

<a id="cns_checkseparator"></a>

##### cns\_checkSeparator()

> **cns\_checkSeparator**(`separator`): `Promise`\<`boolean`\>

Checks whether __separator__ is a vaild CNS separator.

###### Parameters

###### separator

`string`

Separator to check

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if __separator__ is a
         valid separator or to `false` if not.

###### See

[CTRL function `cns_checkSeparator()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_checkSeparator.html)

###### Example

```ts
const isValid = await winccoa.cns_checkSeparator('.');
```

<a id="cns_getnodeicon"></a>

##### cns\_getNodeIcon()

> **cns\_getNodeIcon**(`id`): `Promise`\<`string`\>

Returns the path of the icon defined for given __id__.

###### Parameters

###### id

`string`

CNS ID.

###### Returns

`Promise`\<`string`\>

Promise - will be resolved to the path of the icon or empty string if
         no icon is defined for __id__.

###### See

[CTRL function `cns_getNodeIcon()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_getNodeIcon.html)

###### Example

```ts
const iconPath = await winccoa.cns_getNodeIcon('System1.View1:Node1.Rpt2');
```

<a id="cns_getnodetypedisplayname"></a>

##### cns\_getNodeTypeDisplayName()

> **cns\_getNodeTypeDisplayName**(`typeName`): `Promise`\<[`WinccoaLangString`](#winccoalangstring)\>

Returns the display name of the given CNS node type.

###### Parameters

###### typeName

`string`

Name of the CNS node type.

###### Returns

`Promise`\<[`WinccoaLangString`](#winccoalangstring)\>

Promise - will be resolved to the display name of the node type in
         the current multi-language string format or empty string if node
         type does not exist.

###### See

[CTRL function `cns_getNodeTypeDisplayName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_getNodeTypeDisplayName.html)

###### Example

```ts
const displayName = await winccoa.cns_getNodeTypeDisplayName('struct');
```

<a id="cns_getnodetypes"></a>

##### cns\_getNodeTypes()

> **cns\_getNodeTypes**(): `Promise`\<\{ `icons`: `string`[]; `typeIds`: `string`[]; `typeNames`: `string`[]; `values`: `number`[]; \}\>

Gets all CNS node type details.

###### Returns

`Promise`\<\{ `icons`: `string`[]; `typeIds`: `string`[]; `typeNames`: `string`[]; `values`: `number`[]; \}\>

Promise for an object containing arrays with details for all defined CNS node types.
         All arrays have the same size.

###### See

[CTRL function `cns_getNodeTypes()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_getNodeTypes.html)

###### Example

```ts
const { typeIds, typeNames, values, icons } = await winccoa.cns_getNodeTypes();
for (let i = 0; i < typeIds.length; ++i)
  console.info(typeIds[i], typeNames[i], values[i], icons[i]);
```

<a id="cns_getnodetypevalue"></a>

##### cns\_getNodeTypeValue()

> **cns\_getNodeTypeValue**(`typeName`): `Promise`\<`number`\>

Returns the numerical value for the given CNS node type.

###### Parameters

###### typeName

`string`

Name of the CNS node type.

###### Returns

`Promise`\<`number`\>

Promise - will be resolved to the numerical value for the node type
         or `-1` if type does not exist.

###### See

[CTRL function `cns_getNodeTypeValue()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_getNodeTypeValue.html)

###### Example

```ts
const typeNum = await winccoa.cns_getNodeTypeValue('struct');
```

<a id="cns_getreadableviews"></a>

##### cns\_getReadableViews()

> **cns\_getReadableViews**(`systemName`): `Promise`\<`string`[]\>

Returns a list with all views (for which the current permission is sufficient) of the given system.

###### Parameters

###### systemName

`string`

System name

###### Returns

`Promise`\<`string`[]\>

Promise - will be resolved to an array containing the names of all readable views.

###### See

[CTRL function `cns_getReadableViews()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_getReadableViews.html)

###### Example

```ts
const views = await winccoa.cns_getReadableViews('System1');
```

<a id="cns_getviewpermission"></a>

##### cns\_getViewPermission()

> **cns\_getViewPermission**(`viewName`): `Promise`\<`number`\>

Returns the permission bits for the given view.

###### Parameters

###### viewName

`string`

View name.

###### Returns

`Promise`\<`number`\>

Promise - will be resolved to a number containing the permission bits.

###### See

[CTRL function `cns_getViewPermission`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_getViewPermission.html)

###### Example

```ts
const views = await winccoa.cns_getViewPermission('System1.View1:');
```

<a id="cns_isnode"></a>

##### cns\_isNode()

> **cns\_isNode**(`path`): `Promise`\<`boolean`\>

Checks whether the given CNS ID __path__ is a node.

###### Parameters

###### path

`string`

CNS ID path.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if __path__ is a node.

###### See

[CTRL function `cns_isNode`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_isNode.html)

###### Example

```ts
const isNode = await winccoa.cns_isNode('System1.View1::Node1');
```

<a id="cns_istree"></a>

##### cns\_isTree()

> **cns\_isTree**(`path`): `Promise`\<`boolean`\>

Checks whether the given CNS ID __path__ is a tree.

###### Parameters

###### path

`string`

CNS ID path.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if __path__ is a tree.

###### See

[CTRL function `cns_isTree`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_isTree.html)

###### Example

```ts
const isTree = await winccoa.cns_isTree('System1.View1:Node1');
```

<a id="cns_isview"></a>

##### cns\_isView()

> **cns\_isView**(`path`): `Promise`\<`boolean`\>

Checks whether the given CNS ID __path__ is a view.

###### Parameters

###### path

`string`

CNS ID path.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if __path__ is a view.

###### See

[CTRL function `cns_isView`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_isView.html)

###### Example

```ts
const isView = await winccoa.cns_isView('System1.View1:');
```

<a id="cns_nodeexists"></a>

##### cns\_nodeExists()

> **cns\_nodeExists**(`path`): `Promise`\<`boolean`\>

Checks whether the node with the given CNS ID __path__ exists.

###### Parameters

###### path

`string`

CNS ID path.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if node with __path__ exists.

###### See

[CTRL function `cns_nodeExists`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_nodeExists.html)

###### Example

```ts
const exists = await winccoa.cns_nodeExists('System1.View1::Node1');
```

<a id="cns_treeexists"></a>

##### cns\_treeExists()

> **cns\_treeExists**(`path`): `Promise`\<`boolean`\>

Checks whether the tree with the given CNS ID __path__ exists.

###### Parameters

###### path

`string`

CNS ID path.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if tree with __path__ exists.

###### See

[CTRL function `cns_treeExists`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_treeExists.html)

###### Example

```ts
const exists = await winccoa.cns_treeExists('System1.View1::Node1');
```

<a id="cns_viewdptoname"></a>

##### cns\_viewDpToName()

> **cns\_viewDpToName**(`dpName`): `Promise`\<`string`\>

Returns the name of the CNS view linked to given __dpName__, if any.

###### Parameters

###### dpName

`string`

Data point name.

###### Returns

`Promise`\<`string`\>

Name of the view linked to __dpName__ or empty
         string if not found.

###### See

- [CTRL function `cns_viewDpToName`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_viewDpToName.html)
- [cns\_viewNameToDpName](#cns_viewnametodpname)

###### Example

```ts
const viewName = winccoa.cns_viewDpToName('System1:_CNS_View_00002');
```

<a id="cns_viewexists"></a>

##### cns\_viewExists()

> **cns\_viewExists**(`path`): `Promise`\<`boolean`\>

Checks whether the view with the given CNS ID __path__ exists.

###### Parameters

###### path

`string`

CNS ID path.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if view with __path__ exists.

###### See

[CTRL function `cns_viewExists`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_viewExists.html)

###### Example

```ts
const exists = await winccoa.cns_viewExists('System1.View1::Node1');
```

<a id="cns_viewnametodpname"></a>

##### cns\_viewNameToDpName()

> **cns\_viewNameToDpName**(`viewName`, `createNonExistingViewDp`): `Promise`\<`string`\>

Returns the name of the data point linked to given CNS __viewName__.

###### Parameters

###### viewName

`string`

CNS view name.

###### createNonExistingViewDp

`boolean` = `true`

If `true` (default), a linked data point is
       created if it does not already exist. If `false`, an empty string
       is returned if no linked data point exists.

###### Returns

`Promise`\<`string`\>

Name of the data point linked to __dpName__ or empty string if
         not found.

###### See

- [CTRL function `cns_viewNameToDpName`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cns_viewNameToDpName.html)
- [cns\_viewDpToName](#cns_viewdptoname)

###### Example

```ts
const viewName = winccoa.cns_viewNameToDpName('System1.View1:');
```

<a id="cnsaddnode"></a>

##### cnsAddNode()

> **cnsAddNode**(`cnsParentPath`, `name`, `displayName`, `dp`): `Promise`\<`boolean`\>

Adds a new node to a tree or sub-tree.

###### Parameters

###### cnsParentPath

`string`

The ID path of the parent node of the new node.
> __Note:__ You must specify a node and not a view.

###### name

`string`

ID of the new node

###### displayName

`unknown`

Display name of the new node as multi-language string

###### dp

`string` = `''`

The optional data point (element) which is linked to the node.
          If no data point shall be linked an empty string can be defined (= default).

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- Wrong or missing parameters
- The defined node __cnsParentPath__ could not be found
- Illegal characters in name

###### See

- [CTRL function `cnsAddNode()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsAddNode.html)

###### Example

```ts
try {
  await winccoa.cnsAddNode('System1.View1:Node1', 'A', 'A', 'System1:ExampleDP_Trend1.');
} catch(exc) {
  console.error(exc);
}
```
 - [WinccoaLangStringFormat](#winccoalangstringformat)

<a id="cnsaddobserver"></a>

##### cnsAddObserver()

> **cnsAddObserver**(`callback`): `number`

Registers a callback for notification of CNS changes.

###### Parameters

###### callback

[`WinccoaCnsObserverCallback`](#winccoacnsobservercallback)

Callback function that will be registered.

###### Returns

`number`

ID of the callback.

###### See

- [CTRL function `cnsAddObserver()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsAddObserver.html)
- [cnsRemoveObserver](#cnsremoveobserver)
- [WinccoaCnsObserverCallback](#winccoacnsobservercallback)

###### Example

```ts
import {
  WinccoaManager,
  WinccoaCnsAction,
  WinccoaCnsChangeType,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function cnsCB(
  path: string,
  changeType: WinccoaCnsChangeType,
  action: WinccoaCnsAction,
) {
  console.log(path, changeType, action);
}

const cbId = winccoa.cnsAddObserver(cnsCb);
```

<a id="cnsaddtree"></a>

##### cnsAddTree()

> **cnsAddTree**(`cnsParentPath`, `tree`): `Promise`\<`boolean`\>

Create a tree or sub-tree.

###### Parameters

###### cnsParentPath

`string`

The path of the parent element (view, tree or node)

###### tree

[`WinccoaCnsTreeNode`](#winccoacnstreenode)

Details of the tree to create

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- Wrong or missing parameters
- The defined view, tree or node __cnsParentPath__ could not be found
- Illegal characters in [WinccoaCnsTreeNode.name](#name-1)
- Data point in [WinccoaCnsTreeNode.dp](#dp-2) not found

###### See

- [CTRL function `cnsAddTree()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsAddTree.html)

###### Example

```ts
try {
  let tree = new WinccoaCnsTreeNode('MyTree', 'MyTree', '', [
    new WinccoaCnsTreeNode('B', 'B', '', [
      new WinccoaCnsTreeNode('dp', 'ExampleDP_Rpt1', 'System1:ExampleDP_Rpt1.')
    ]),
    new WinccoaCnsTreeNode('C', {'de_AT.utf8': 'deC', 'en_US.utf8': 'enC'})
  ]);

  await winccoa.cnsAddTree('System1.View1', tree);
} catch(exc) {
  console.error(exc);
}
```

<a id="cnschangetree"></a>

##### cnsChangeTree()

> **cnsChangeTree**(`cnsPath`, `tree`): `Promise`\<`boolean`\>

Replaces a tree or sub-tree with a new tree.

###### Parameters

###### cnsPath

`string`

The ID path of the tree (or node) that shall be replaced.

###### tree

[`WinccoaCnsTreeNode`](#winccoacnstreenode)

Details of the tree to create

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- Wrong or missing parameters
- The defined node or tree __cnsPath__ could not be found
- Illegal characters in [WinccoaCnsTreeNode.name](#name-1)
- Data point in [WinccoaCnsTreeNode.dp](#dp-2) not found

###### See

- [CTRL function `cnsChangeTree()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsChangeTree.html)

###### Example

```ts
try {
  let tree = new WinccoaCnsTreeNode('MyTree2', 'MyTree2', '', [
    new WinccoaCnsTreeNode('B', 'B', '', [
      new WinccoaCnsTreeNode('dp', 'ExampleDP_Rpt1', 'System1:ExampleDP_Rpt1.')
    ]),
    new WinccoaCnsTreeNode('C', {'de_AT.utf8': 'deC', 'en_US.utf8': 'enC'})
  ]);

  await winccoa.cnsChangeTree('System1.View1:MyTree', tree);
} catch(exc) {
  console.error(exc);
}
```

<a id="cnscreateview"></a>

##### cnsCreateView()

> **cnsCreateView**(`view`, `displayName`, `separator`): `Promise`\<`boolean`\>

Creates a new view with the given display name.

###### Parameters

###### view

`string`

The ID path of the new view

###### displayName

`unknown`

The display name of the new view as multi-language string

###### separator

`unknown` = `'.'`

The optional separator for the new view as multi-language string
> __Note:__ The following characters are not allowed for separators: __\'__ (single quotation mark),
> __"__ (quotation marks), __*__ (asterisk), __?__ (question mark).
> Moreover, numbers and letters which are already used in the view or node name must not be used.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- invalid argument type is given
- invalid __view__, or __separator__ is given
- view with the given __view__ already exists

###### See

- [CTRL function `cnsCreateView()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsCreateView.html)

###### Example

```ts
try {
  await winccoa.cnsCreateView('System1.View123:', 'View123', '/');
} catch(exc) {
  console.error(exc);
}
```
 - [WinccoaLangStringFormat](#winccoalangstringformat)

<a id="cnsdeletetree"></a>

##### cnsDeleteTree()

> **cnsDeleteTree**(`cnsPath`): `Promise`\<`boolean`\>

Delete a tree, sub-tree or node.

###### Parameters

###### cnsPath

`string`

The ID path of the element that shall be deleted.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- Wrong or missing parameters
- The defined tree __cnsPath__ could not be found

###### See

- [CTRL function `cnsDeleteTree()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsDeleteTree.html)

###### Example

```ts
try {
  await winccoa.cnsDeleteTree('System1.View1:MyTree');
} catch(exc) {
  console.error(exc);
}
```

<a id="cnsdeleteview"></a>

##### cnsDeleteView()

> **cnsDeleteView**(`view`): `Promise`\<`boolean`\>

Delete a view with all its trees.

###### Parameters

###### view

`string`

ID path of the view

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- invalid argument type is given
- invalid __view__

###### See

- [CTRL function `cnsDeleteView()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsDeleteView.html)

###### Example

```ts
try {
  await winccoa.cnsDeleteView('System1.View123:');
} catch(exc) {
  console.error(exc);
}
```

<a id="cnsgetaccessright"></a>

##### cnsGetAccessRight()

> **cnsGetAccessRight**(`cnsPath`, `propertyKey`): [`WinccoaCnsAccessRight`](#winccoacnsaccessright)

Returns the AccessRight for the given node.
Note: the CNS property must be an uint.

###### Parameters

###### cnsPath

`string`

ID path of the node

###### propertyKey

`string`

The cns property key which is used for getting the AccessRight

###### Returns

[`WinccoaCnsAccessRight`](#winccoacnsaccessright)

accessRight of type [WinccoaCnsAccessRight](#winccoacnsaccessright)

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ does not exist).

###### See

- [CTRL function `cnsGetAccessRight()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetAccessRight.html)

###### Example

```ts
console.log(winccoa.cnsGetAccessRight('System1.View1:Node1', 'OA:OPC'));
```

<a id="cnsgetchildren"></a>

##### cnsGetChildren()

> **cnsGetChildren**(`cnsPath`): `string`[]

Returns the paths of all children nodes for the given __cnsPath__.

###### Parameters

###### cnsPath

`string`

ID path of the node.

###### Returns

`string`[]

Array of paths for all children nodes for __cnsPath__.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ or child for the given __cnsPath__ does not exist).

###### See

- [CTRL function `cnsGetChildren()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetChildren.html)
 - [cnsGetParent](#cnsgetparent)

###### Example

```ts
const children = winccoa.cnsGetChildren('System1.View1:Node1');
console.log(children);
```

<a id="cnsgetdisplaynames"></a>

##### cnsGetDisplayNames()

> **cnsGetDisplayNames**(`cnsPath`): [`WinccoaLangString`](#winccoalangstring)

Returns the display names for node with given __cnsPath__.

###### Parameters

###### cnsPath

`string`

CNS path for the node.

###### Returns

[`WinccoaLangString`](#winccoalangstring)

Display names in the current multi-language string format.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ does not exist).

###### See

- [CTRL function `cnsGetDisplayNames()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetDisplayNames.html)
 - [WinccoaLangStringFormat](#winccoalangstringformat)

###### Example

```ts
console.log(winccoa.cnsGetDisplayNames('System1.View1:Node1.Rpt1'));
```

<a id="cnsgetdisplaypath"></a>

##### cnsGetDisplayPath()

> **cnsGetDisplayPath**(`cnsPath`): [`WinccoaLangString`](#winccoalangstring)

Returns the display path for node with given __cnsPath__.

###### Parameters

###### cnsPath

`string`

CNS path for the node.

###### Returns

[`WinccoaLangString`](#winccoalangstring)

Display path in the current multi-language string format.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ does not exist).

###### See

- [CTRL function `cnsGetDisplayPath()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetDisplayPath.html)
 - [WinccoaLangStringFormat](#winccoalangstringformat)

###### Example

```ts
console.log(winccoa.cnsGetDisplayPath('System1.View1:Node1.Rpt1'));
```

<a id="cnsgetid"></a>

##### cnsGetId()

> **cnsGetId**(`cnsPath`, `typeOutput?`): `string`

Returns the data point element name (and optionally type) linked with given __cnsPath__.

###### Parameters

###### cnsPath

`string`

CNS path of the data point element.

###### typeOutput?

If given, the property `type` will be set to the (customizable) ID of the CNS node.

###### type

`number`

###### Returns

`string`

Data point element name or empty string.

###### Throws

[WinccoaError](#winccoaerror) when __cnsPath__ does not exist.

###### See

- [CTRL function `cnsGetId()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetId.html)

###### Example

```ts
const details = { type: 0 };
const dpeName = winccoa.cnsGetId('System1.vvv:n1.nn1', details);
console.log(`DPE name: ${dpeName}, type: ${details.type}`);
```

<a id="cnsgetidset"></a>

##### cnsGetIdSet()

> **cnsGetIdSet**(`pattern`, `viewPath`, `searchMode`, `langIdx`, `type`): `string`[]

Returns a list of data point element names linked to nodes matching given __pattern__ and
additional criteria.

###### Parameters

###### pattern

`string`

Search pattern for the paths, can use wildcards `**`, `*` and `?`. See
[`cnsGetIdSet()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetIdSet.html)
for details.

###### viewPath

`string` = `''`

Path to the view to be searched (optional, default: search all views).

###### searchMode

[`WinccoaCnsSearchMode`](#winccoacnssearchmode) = `...`

Search mode (optional, default: search all names, case insensitive).

###### langIdx

`number` = `WinccoaCnsConstants.AllLanguages`

Index of the language to search when __searchMode__ includes display names
(optional, default: search all languages).

###### type

`number` = `WinccoaCnsNodeType.All`

Type of the nodes to search (optional, default: search all types).

###### Returns

`string`[]

Array of data point element names linked to the matching nodes.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters.

###### See

- [CTRL function `cnsGetIdSet()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetIdSet.html)

###### Example

```ts
import { WinccoaManager, WinccoaCnsSearchMode } from 'winccoa-manager';
const winccoa = new WinccoaManager();

// using default parameters
let dpeNames = winccoa.cnsGetIdSet('**1');
console.log(dpeNames);

// using explicit parameters
dpeNames = winccoa.cnsGetIdSet(
  '**Report*',
  'System1.View1:',
  WinccoaCnsSearchMode.DisplayName | WinccoaCnsSearchMode.CaseInsensitive,
  0,  // first project language
  55, // custom node type
);
console.log(dpeNames);
```

<a id="cnsgetnodesbydata"></a>

##### cnsGetNodesByData()

> **cnsGetNodesByData**(`dpName`, `type`, `viewPath`): `string`[]

Returns all CNS paths for nodes that are linked to a given data point (element).

###### Parameters

###### dpName

`string`

Name of the data point (element).

###### type

`number` = `WinccoaCnsNodeType.All`

Type of the nodes to search (optional, default: search all types).

###### viewPath

`string` = `''`

Path to the view to be searched (optional, default: search all views).

###### Returns

`string`[]

Array of matching CNS paths.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters.

###### See

- [CTRL function `cnsGetNodesByData()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetNodesByData.html)

###### Example

```ts
// default parameters
let result = winccoa.cnsGetNodesByData('ExampleDP_Rpt1.');
console.log(result);

// custom type, single view
result = winccoa.cnsGetNodesByData('ExampleDP_Rpt1.', 55, 'System1.View1:');
console.log(result);
```

<a id="cnsgetnodesbyname"></a>

##### cnsGetNodesByName()

> **cnsGetNodesByName**(`pattern`, `viewPath`, `searchMode`, `langIdx`, `type`): `string`[]

Returns a CNS paths matching given __pattern__ and additional criteria.

###### Parameters

###### pattern

`string`

Search pattern for the paths, can use wildcards `**`, `*` and `?`. See
[`cnsGetNodesByName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetNodesByName.html)
for details.

###### viewPath

`string` = `''`

Path to the view to be searched (optional, default: search all views).

###### searchMode

[`WinccoaCnsSearchMode`](#winccoacnssearchmode) = `...`

Search mode (optional, default: search all names, case insensitive).

###### langIdx

`number` = `WinccoaCnsConstants.AllLanguages`

Index of the language to search when __searchMode__ includes display names
(optional, default: search all languages).

###### type

`number` = `WinccoaCnsNodeType.All`

Type of the nodes to search (optional, default: search all types).

###### Returns

`string`[]

Array of matching CNS paths.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters.

###### See

- [CTRL function `cnsGetNodesByName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetNodesByName.html)

###### Example

```ts
import { WinccoaManager, WinccoaCnsSearchMode } from 'winccoa-manager';
const winccoa = new WinccoaManager();

// using default parameters
let paths = winccoa.cnsGetNodesByName('**1');
console.log(paths);

// using explicit parameters
paths = winccoa.cnsGetNodesByName(
  '**Report*',
  'System1.View1:',
  WinccoaCnsSearchMode.DisplayName | WinccoaCnsSearchMode.CaseInsensitive,
  0,  // first project language
  55, // custom node type
);
console.log(paths);
```

<a id="cnsgetopcaccessright"></a>

##### cnsGetOPCAccessRight()

> **cnsGetOPCAccessRight**(`cnsPath`): [`WinccoaCnsAccessRight`](#winccoacnsaccessright)

Returns the OPC AccessLevel for the given node.

###### Parameters

###### cnsPath

`string`

ID path of the node

###### Returns

[`WinccoaCnsAccessRight`](#winccoacnsaccessright)

accessRight of type [WinccoaCnsAccessRight](#winccoacnsaccessright)

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ does not exist).

###### See

- [CTRL function `cnsGetOPCAccessRight()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetOPCAccessRight.html)

###### Example

```ts
console.log(winccoa.cnsGetOPCAccessRight('System1.View1:Node1'));
```

<a id="cnsgetparent"></a>

##### cnsGetParent()

> **cnsGetParent**(`cnsPath`): `string`

Returns the path of the parent node for the given __cnsPath__.

###### Parameters

###### cnsPath

`string`

ID path of the node

###### Returns

`string`

The ID path of the parent node for the given __cnsPath__.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ or parent for the given __cnsPath__ does not exist).

###### See

- [CTRL function `cnsGetParent()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetParent.html)
- [cnsGetChildren](#cnsgetchildren)

###### Example

```ts
const parent = winccoa.cnsGetParent('System1.View1:Node1.Node1');
console.log(parent);
```

<a id="cnsgetproperty"></a>

##### cnsGetProperty()

> **cnsGetProperty**(`cnsPath`, `key`): `unknown`

Returns the value of the property with given __key__ from node with given __cnsPath__.

###### Parameters

###### cnsPath

`string`

CNS path of the node for which the property value should be returned.

###### key

`string`

Key of the property

###### Returns

`unknown`

Value of the property

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ or __key__ does not exist).

###### See

- [CTRL function `cnsGetProperty()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetProperty.html)

###### Example

```ts
const key = 'stringProperty';
const value = winccoa.cnsGetProperty('System1.View1:Node1.Rpt1', key);
console.log(`value of property '${key}' is '${value}'`);
```

<a id="cnsgetpropertykeys"></a>

##### cnsGetPropertyKeys()

> **cnsGetPropertyKeys**(`cnsPath`): `string`[]

Returns a list of the property keys existing for node with given __cnsPath__.

###### Parameters

###### cnsPath

`string`

CNS path of the node for which the property keys should be returned.

###### Returns

`string`[]

List of property keys (possibly empty).

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ does not exist).

###### See

- [CTRL function `cnsGetPropertyKeys()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetPropertyKeys.html)

###### Example

```ts
console.log(winccoa.cnsGetPropertyKeys('System1.View1:Node1.Rpt1'));
```

<a id="cnsgetroot"></a>

##### cnsGetRoot()

> **cnsGetRoot**(`cnsNodePath`): `string`

Returns the ID path of the root node of the tree which contains the given node.

###### Parameters

###### cnsNodePath

`string`

The ID path of the node

###### Returns

`string`

ID path of the root node

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsNodePath__ does not exist).

###### See

- [CTRL function `cnsGetRoot()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetRoot.html)

###### Example

```ts
console.log(winccoa.cnsGetRoot('System1.View1:Node1.Rpt1'));
```

<a id="cnsgetsystemnames"></a>

##### cnsGetSystemNames()

> **cnsGetSystemNames**(`systemName`): [`WinccoaLangString`](#winccoalangstring)

Returns the display names of the given system.

###### Parameters

###### systemName

`string`

System name in the current multi-language string format.

###### Returns

[`WinccoaLangString`](#winccoalangstring)

display names of the system

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__systemName__ does not exist).

###### See

- [CTRL function `cnsGetSystemNames()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetSystemNames.html)
 - [WinccoaLangStringFormat](#winccoalangstringformat)

###### Example

```ts
console.log(winccoa.cnsGetSystemNames('System1'));
```

<a id="cnsgettrees"></a>

##### cnsGetTrees()

> **cnsGetTrees**(`view`): `string`[]

Returns the ID paths of all trees of the given view.

###### Parameters

###### view

`string`

Name of the view

###### Returns

`string`[]

The ID paths of all trees of the given view

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__view__ does not exist).

###### See

- [CTRL function `cnsGetTrees()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetTrees.html)

###### Example

```ts
console.log(winccoa.cnsGetTrees('System1.View1:'));
```

<a id="cnsgetuserdata"></a>

##### cnsGetUserData()

> **cnsGetUserData**(`cnsPath`): `Buffer`

Returns the user data stored in a node.

###### Parameters

###### cnsPath

`string`

ID path of the node

###### Returns

`Buffer`

the user data stored in the node

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__cnsPath__ does not exist).

###### See

- [CTRL function `cnsGetUserData()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetUserData.html)

###### Example

```ts
console.log(winccoa.cnsGetUserData('System1.View1:Node1'));
```

<a id="cnsgetviewdisplaynames"></a>

##### cnsGetViewDisplayNames()

> **cnsGetViewDisplayNames**(`viewPath`): [`WinccoaLangString`](#winccoalangstring)

Returns the display names for given __viewPath__.

###### Parameters

###### viewPath

`string`

ID path of the view.

###### Returns

[`WinccoaLangString`](#winccoalangstring)

Display names in the current multi-language string format.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__viewPath__ does not exist).

###### See

- [CTRL function `cnsGetViewDisplayNames()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetViewDisplayNames.html)
 - [WinccoaLangStringFormat](#winccoalangstringformat)

###### Example

```ts
console.log(winccoa.cnsGetViewDisplayNames('System1.View1:'));
```

<a id="cnsgetviews"></a>

##### cnsGetViews()

> **cnsGetViews**(`systemName`): `string`[]

Returns the paths of all views for the given __systemName__.

###### Parameters

###### systemName

`string`

System name.

###### Returns

`string`[]

Array of paths for all found views for __systemName__.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__systemName__ does not exist).

###### See

- [CTRL function `cnsGetViews()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetViews.html)

###### Example

```ts
const result = winccoa.cnsGetViews('System1');
console.log(result);
```

<a id="cnsgetviewseparators"></a>

##### cnsGetViewSeparators()

> **cnsGetViewSeparators**(`viewPath`): [`WinccoaLangString`](#winccoalangstring)

Returns the separators for given __viewPath__.

###### Parameters

###### viewPath

`string`

ID path of the view.

###### Returns

[`WinccoaLangString`](#winccoalangstring)

Separators in the current multi-language string format.

###### Throws

[WinccoaError](#winccoaerror) for invalid parameters (__viewPath__ does not exist).

###### See

- [CTRL function `cnsGetViewSeparators()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsGetViewSeparators.html)
 - [WinccoaLangStringFormat](#winccoalangstringformat)

###### Example

```ts
console.log(winccoa.cnsGetViewSeparators('System1.View1:'));
```

<a id="cnsremoveobserver"></a>

##### cnsRemoveObserver()

> **cnsRemoveObserver**(`id`): `number`

Unregisters a callback for notification of CNS changes.

###### Parameters

###### id

`number`

ID of the callback to unregister as returned by [cnsAddObserver](#cnsaddobserver).

###### Returns

`number`

Callback ID.

###### Throws

[WinccoaError](#winccoaerror) when __id__ is not registered.

###### See

- [CTRL function `cnsRemoveObserver()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsRemoveObserver.html)
- [cnsAddObserver](#cnsaddobserver)

###### Example

```ts
const id = winccoa.cnsAddObserver(cnsCb);
...

try {
  winccoa.cnsRemoveObserver(id);
} catch (exc) {
  console.error(exc);
}
```

<a id="cnssetproperty"></a>

##### cnsSetProperty()

> **cnsSetProperty**(`cnsPath`, `key`, `value`, `valueType`): `Promise`\<`boolean`\>

Sets or add the property for the given node as key/value pair.
The following keys are already used by WinCC OA internally:
- OA:ICON Name of the icon (including the path relative to the pictures folder) that shall be set for the node.
- OA:OPC Appropriate bit pattern to define the AccessLevel. E.g. 3 to set the bits for read & write.
- OA:MOD Number of used registers (see Modbus/TCP server details or Plantmodel Editor - Modbus)
- OA:DMOD Number of dyn elements (see Modbus/TCP server details or Plantmodel Editor - Modbus)
> __Note:__ A maximum of 256 byte (sum of length of key, value and internal control characters) can be stored per node.

###### Parameters

###### cnsPath

`string`

ID path of the node

###### key

`string`

name

###### value

`unknown`

value

###### valueType

[`WinccoaCtrlType`](#winccoactrltype)

Type of value (see [WinccoaCtrlType](#winccoactrltype)).

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- Wrong or missing parameters
- The defined node __cnsPath__ could not be found
- The key/value pair exceeds the maximum length for node properties (256 bytes).
           Therefore, the pair cannot be added.

###### See

- [CTRL function `cnsSetProperty()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsSetProperty.html)

###### Example

```ts
try {
  await winccoa.cnsSetProperty('System1.View1:Node1', 'OA:OPC', 5, WinccoaCtrlType.int);
} catch(exc) {
  console.error(exc);
}
```

<a id="cnssetuserdata"></a>

##### cnsSetUserData()

> **cnsSetUserData**(`cnsPath`, `userData`): `Promise`\<`boolean`\>

Stores user data in a node.

###### Parameters

###### cnsPath

`string`

ID path of the node

###### userData

`Buffer`

User data which shall be stored in the node.
       The blob is truncated to 255 bytes if it is too long.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- invalid argument type is given
- invalid __cnsPath__

###### See

- [CTRL function `cnsSetUserData()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsSetUserData.html)

###### Example

```ts
try {
  // v- Sample data in hex: 00 01 02 03  41 42 43 44  61 62 63 64  FC FB FE FF
  const userData = Buffer.alloc(16, 'AAECA0FCQ0RhYmNk/Pv+/w==', 'base64');

  await winccoa.cnsSetUserData('System1.View1:Node1', userData);
} catch(exc) {
  console.error(exc);
}
```

<a id="cnssubstr"></a>

##### cnsSubStr()

> **cnsSubStr**(`cnsPath`, `flags`, `resolvePath`): `string`

Returns a sub-string of __cnsPath__.

###### Parameters

###### cnsPath

`string`

ID path.

###### flags

[`WinccoaCnsSubStrFlags`](#winccoacnssubstrflags)

Flag(s) that determine which part(s) of __cnsPath__ should be included
       in the sub-string. Can be combined with a binary OR (`|`).

###### resolvePath

`boolean` = `true`

If `true`, __cnsPath__ is resolved and existing elements
       will be used to determine the system name and separate the path from the tail.
       If `false` or no elements of __cnsPath__ can be found, the specified parts will
       be extracted by parsing the path string. Disabling path resolution is mainly
       useful when you already know whether the path exists, so that you can avoid
       the overhead of accessing CNS.

###### Returns

`string`

Sub-string of __cnsPath__.

###### See

- [CTRL function `cnsSubStr()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/CNS_Ctrl/cnsSubStr.html)

###### Example

```ts
const path = 'System1.View1:Node1.Rpt99';
console.log(winccoa.cnsSubStr(path, WinccoaCnsSubStrFlags.View));
console.log(
  winccoa.cnsSubStr(
    path,
    WinccoaCnsSubStrFlags.System | WinccoaCnsSubStrFlags.View,
    false,
  ),
);
```

#### Cryptography

<a id="checkcrypt"></a>

##### checkCrypt()

> **checkCrypt**(`text`, `hash`): `Promise`\<`boolean`\>

Checks whether __hash__ is a valid hash value for __text__.

> __Note:__
> This works only when __hash__ has been created with [crypt](#crypt) using version 3 or higher.

###### Parameters

###### text

`string`

Plain text to check.

###### hash

`string`

Hash created with [crypt](#crypt) unsing version 3 or higher.

###### Returns

`Promise`\<`boolean`\>

Promise that resolves to `true` if __hash__ is a valid hash for __text__.

###### See

- [CTRL function `checkCrypt()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/checkCrypt.html)
- [crypt](#crypt) - also for an example.

<a id="crypt"></a>

##### crypt()

> **crypt**(`text`, `version`, `iterations`): `Promise`\<`string`\>

Creates a cryptographic hash value for __text__ (e.g. for password hashing).

###### Parameters

###### text

`string`

Text for which a hash should be generated.

###### version

`number` = `-1`

Version of the hash algorithm:
- -1: always use latest version (default)
- ~~1:~~ _deprecated_
- ~~2:~~ _deprecated_
- ~~3:~~ _deprecated_
- 4: PKCS5 using SHA256

###### iterations

`number` = `0`

Number of iterations (default: 100000).

###### Returns

`Promise`\<`string`\>

Promise that resolves to a hash string for __text__ in the specified format.

###### See

- [CTRL function `crypt()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/crypt.html)
- [checkCrypt](#checkcrypt)

###### Example

```ts
async function verifyCrypt(plaintext: string) {
  const hash = await winccoa.crypt(plaintext);
  console.info(hash);

  if (await winccoa.checkCrypt(plaintext, hash))
    console.info('Hash matches plaintext');
}
```

<a id="decrypttobuffer"></a>

##### decryptToBuffer()

> **decryptToBuffer**(`ciphertext`, `passphrase`): `Promise`\<`Buffer`\<`ArrayBufferLike`\>\>

Decrypts __ciphertext__ to a `Buffer` using __passphrase__.

###### Parameters

###### ciphertext

`Buffer`

Ciphertext to be decrypted.

###### passphrase

`string`

Passphrase to be used for decryption.

###### Returns

`Promise`\<`Buffer`\<`ArrayBufferLike`\>\>

Promise for the decrypted data.

###### Throws

[WinccoaError](#winccoaerror) when decryption fails.

###### See

- [CTRL function `decrypt()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/decrypt.html)
- [encrypt](#encrypt)
- [decryptToString](#decrypttostring)

###### Example

```ts
async function verifyEncryptBuffer(data: Buffer, passphrase: string) {
  const ciphertext = await winccoa.encrypt(data, passphrase);
  console.info(ciphertext);

  const decrypted = await winccoa.decryptToBuffer(ciphertext, passphrase);
  if (decrypted.equals(data)) console.info('Decryption successful');
}
```

<a id="decrypttostring"></a>

##### decryptToString()

> **decryptToString**(`ciphertext`, `passphrase`): `Promise`\<`string`\>

Decrypts __ciphertext__ to a `string` using __passphrase__.

###### Parameters

###### ciphertext

`Buffer`

Ciphertext to be decrypted.

###### passphrase

`string`

Passphrase to be used for decryption.

###### Returns

`Promise`\<`string`\>

Promise for the decrypted data.

###### Throws

[WinccoaError](#winccoaerror) when decryption fails.

###### See

- [CTRL function `decrypt()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/decrypt.html)
- [encrypt](#encrypt)
- [decryptToBuffer](#decrypttobuffer)

###### Example

```ts
async function verifyEncrypt(plaintext: string, passphrase: string) {
  const ciphertext = await winccoa.encrypt(plaintext, passphrase);
  console.info(ciphertext);

  const decrypted = await winccoa.decryptToString(ciphertext, passphrase);
  if (decrypted == plaintext) console.info('Decryption successful');
}
```

<a id="encrypt"></a>

##### encrypt()

> **encrypt**(`plaintext`, `passphrase`, `cipherConfig`): `Promise`\<`Buffer`\<`ArrayBufferLike`\>\>

Encrypts __plaintext__ using __passphrase__.

###### Parameters

###### plaintext

Plain text or data to encrypt.

`string` | `Buffer`\<`ArrayBufferLike`\>

###### passphrase

`string`

Passphrase to use for encrypting.

###### cipherConfig

`string` = `''`

Cipher configuration - allows to specify the encryption algorithm, see
       [CTRL function `encrypt()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/encrypt.html)
       for details.

###### Returns

`Promise`\<`Buffer`\<`ArrayBufferLike`\>\>

Encrypted text or data.

###### Throws

[WinccoaError](#winccoaerror) when encryption fails (typically invalid
        settings in __cipherConfig__).

###### See

- [CTRL function `encrypt()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/encrypt.html)
- [decryptToBuffer](#decrypttobuffer)
- [decryptToString](#decrypttostring)

###### Example

```ts
async function verifyEncrypt(plaintext: string, passphrase: string) {
  const ciphertext = await winccoa.encrypt(plaintext, passphrase);
  console.info(ciphertext);

  const decrypted = await winccoa.decryptToString(ciphertext, passphrase);
  if (decrypted == plaintext) console.info('Decryption successful');
}
```

#### Data Point

<a id="dpaliastoname"></a>

##### dpAliasToName()

> **dpAliasToName**(`alias`): `string`

Returns the data point name for the specified __alias__.

###### Parameters

###### alias

`string`

Data point alias to look up

###### Returns

`string`

Data point name for given __alias__.

###### Throws

[WinccoaError](#winccoaerror) when __alias__ is not found or invalid argument type.

###### See

- [dpSetAlias](#dpsetalias)
- [dpGetAlias](#dpgetalias)
- [CTRL function `dpAliasToName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpAliasToName.html)

###### Example

```ts
const alias = 'aliasReport1';
const dpName = winccoa.dpAliasToName(alias);
console.info(`DP for alias ${alias}: ${dpName}`);
```

<a id="dpattributetype"></a>

##### dpAttributeType()

> **dpAttributeType**(`dpAttributeName`): [`WinccoaCtrlType`](#winccoactrltype)

Returns the data type of a given data point attribute.

###### Parameters

###### dpAttributeName

`string`

The data point attribute name.

###### Returns

[`WinccoaCtrlType`](#winccoactrltype)

Returns the data type as a [WinccoaCtrlType](#winccoactrltype).

###### Throws

[WinccoaError](#winccoaerror) when the data point attribute does not exist or in case of an invalid argument type.

###### See

- [WinccoaCtrlType](#winccoactrltype)
- [CTRL function `dpAttributeType()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpAttributeType.html)

###### Example

```ts
import { WinccoaManager, WinccoaCtrlType } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function dpAttributeType() {
  console.info(winccoa.dpAttributeType('ExampleDP_AlertHdl1.:_original.._value') == WinccoaCtrlType.bool);
}
```

<a id="dpcancelsplitrequest"></a>

##### dpCancelSplitRequest()

> **dpCancelSplitRequest**(`id`): `boolean`

Cancel dpQuerySplit request.

###### Parameters

###### id

`number`

from [dpQuerySplit](#dpquerysplit) request.

###### Returns

`boolean`

boolean true

###### Throws

Various argument errors.

###### See

- [dpQuerySplit](#dpquerysplit)
- [CTRL function `dpCancelSplitRequest()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpCancelSplitRequest.html)

<a id="dpconnect"></a>

##### dpConnect()

> **dpConnect**(`callback`, `dpeNames`, `answer`): `number`

Creates a connection for being notified of data point element updates.

###### Parameters

###### callback

[`WinccoaDpConnectCallback`](#winccoadpconnectcallback)

Function that is called whenever a connected value changes.

###### dpeNames

DPE name(s) to connect to.
> - Each update will contain updates for all elements in __dpeNames__, not only
  the changed values.
  - Each update will contain an array of values, also if only a single data point element
    name is given.

`string` | `string`[]

###### answer

`boolean` = `true`

if `true`, __callback__ is called with the initial values right away, if `false`,
              callback is only called after an actual value change.

###### Returns

`number`

ID of the new connection (>= 0). This can be used to disconnect from
         updates if required with [dpDisconnect](#dpdisconnect). Otherwise the connection will be closed
         when the manager exits.

###### Throws

[WinccoaError](#winccoaerror) when invalid parameter types, unknown data point element names etc.

###### Remarks

For an example describing how to pass user data to a callback, see the second example
         for [WinccoaDpQueryConnectCallback](#winccoadpqueryconnectcallback).

###### See

- [dpDisconnect](#dpdisconnect)
- [WinccoaDpConnectCallback](#winccoadpconnectcallback)
- [WinccoaConnectUpdateType](#winccoaconnectupdatetype)

###### Example

``` ts
import {
  WinccoaManager,
  WinccoaConnectUpdateType,
  WinccoaError
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function connectCB(
  names: string[],
  values: unknown[],
  type: WinccoaConnectUpdateType,
  error?: WinccoaError
) {
  if (error) {
    console.log(error);
    return;
  }

  if (type == WinccoaConnectUpdateType.Answer)
    console.warn('--- Initial update ---');

  for (let i = 0; i < names.length; i++)
    console.info(`[${i}] '${names[i]}' : ${values[i]}`);
}

function connect() {
  let id = -1;
  try {
    id = winccoa.dpConnect(
      connectCB,
      ['ExampleDP_Arg1.', 'ExampleDP_Arg2.'],
      true
    );
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="dpcopy"></a>

##### dpCopy()

> **dpCopy**(`source`, `destination`, `driver?`): `Promise`\<`boolean`\>

Copies a data point including its configuration.

###### Parameters

###### source

`string`

Name of the data point to copy.

###### destination

`string`

Name of the new copied data point. Must not exist yet.

###### driver?

`number`

Optional driver number (default 1).

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful or rejected with an error.
         In case of an error, `error.details` will contain the same error code
         that CTRL function dpCopy() would return (see there).

###### Throws

[WinccoaError](#winccoaerror) when given source data point does not exist, when data point is copied into itself, invalid argument given, etc.

###### See

- [CTRL function `dpCopy()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpCopy.html)

###### Example

```ts
async function dpCopyTest() {
  let isSuccess = false;
  try {
    isSuccess = await winccoa.dpCopy('ExampleDP_Arg1', 'ExampleDP_Arg3');
  } catch (exc) {
    console.error(exc);
  }

  console.info("DP ExampleDP_Arg1 is copied to ExampleDP_Arg3 successfully - " + isSuccess);
}
```

<a id="dpcreate"></a>

##### dpCreate()

> **dpCreate**(`dpeName`, `dpType`, `systemId?`, `dpId?`): `Promise`\<`boolean`\>

Creates a data point.

###### Parameters

###### dpeName

`string`

Name of the data point to be created.

###### dpType

`string`

Type of data point to be created.

###### systemId?

`number`

To create a data point on a remote system in a distributed system,
                this parameter must contain the system number.

###### dpId?

`number`

The ID of the data point. If a data point with the given ID already
            exists, a random ID is chosen.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful or rejected with an error.

###### Throws

[WinccoaError](#winccoaerror) in case of:
- invalid argument type is given,
- invalid __dpeName__, __dpType__ or non-existing __systemId__ is given,
- data point with the given __dpeName__ is already exist.

###### See

- [dpDelete](#dpdelete)
- [CTRL function `dpCreate()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpCreate.html)

###### Example

```ts
let dpCreated = false;
try {
  dpCreated = await winccoa.dpCreate('newFloatDpe', 'ExampleDP_Float');
} catch (exc) {
  console.error(exc);
}

console.info("DP newFloatDpe is created - " + dpCreated);
```

<a id="dpdelete"></a>

##### dpDelete()

> **dpDelete**(`dpName`): `Promise`\<`boolean`\>

Deletes a data point.

###### Parameters

###### dpName

`string`

Name of the data point to be deleted.
           In case of a distributed system the name of the data point
           to be deleted must contain the system name.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful or rejected with an error.

###### Throws

[WinccoaError](#winccoaerror) when data point with the given name does not exist or current user has no privileges to delete a DP.

###### See

- [dpCreate](#dpcreate)
- [CTRL function `dpDelete()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpDelete.html)

###### Example

```ts
let isSuccess = false;
try {
  isSuccess = await winccoa.dpCreate('newDpe', 'ExampleDP_Float');
} catch (exc) {
  console.error(exc);
}

if (isSuccess)
{
  try {
    isSuccess = await winccoa.dpDelete('newDpe');
  } catch (exc) {
    console.error(exc);
  }
}

console.info("DP newDpe was deleted successfully - " + isSuccess);
```

<a id="dpdisconnect"></a>

##### dpDisconnect()

> **dpDisconnect**(`id`): `number`

Disconnect from data point element update connections established with [dpConnect](#dpconnect).

###### Parameters

###### id

`number`

ID of the connection to close as returned by [dpConnect](#dpconnect).

###### Returns

`number`

ID of the connection that has been closed (>= 0).

###### Throws

[WinccoaError](#winccoaerror) when __id__ is not found or invalid.

###### See

- [dpConnect](#dpconnect)

###### Example

```ts
function connect() {
  let id = -1;
  try {
    id = winccoa.dpConnect(
      connectCB,
      ['ExampleDP_Arg1.', 'ExampleDP_Arg2.'],
      true
    );
  } catch (exc) {
    console.error(exc);
  }
}

function disconnect() {
  try {
    winccoa.dpDisconnect(id);
  } catch (exc) {
   console.error(exc);
  }
}
```

<a id="dpelementtype"></a>

##### dpElementType()

> **dpElementType**(`dpeName`): [`WinccoaElementType`](#winccoaelementtype)

Returns the data typeof a data point element.

###### Parameters

###### dpeName

`string`

Name of the data point element

###### Returns

[`WinccoaElementType`](#winccoaelementtype)

Type of a data point element

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type.

###### See

- [WinccoaElementType](#winccoaelementtype)
- [CTRL function `dpElementType()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpElementType.html)

###### Example

```ts
import { WinccoaManager, WinccoaElementType } from 'winccoa-manager';
const winccoa = new WinccoaManager();

function dpElementTypeTest() {
  try {
    let dpType = winccoa.dpElementType('ExampleDP_Arg1.');
    console.info('The type of ExampleDP_Arg1 is float - ' + (dpType == WinccoaElementType.Float));
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="dpexists"></a>

##### dpExists()

> **dpExists**(`dpeName`): `boolean`

Checks the existence of a valid data point identifier.

###### Parameters

###### dpeName

`string`

A data point identifier: a sys, a DPT, a DP, a DPE, a config, a detail or an attr.

###### Returns

`boolean`

true if at least one part of a data point identifier can be resolved correctly, otherwise false.

###### Throws

[WinccoaError](#winccoaerror) when invalid argument type is given.

###### See

- [CTRL function `dpExists()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpExists.html)

###### Example

```ts
let isDpExists = false;
try {
  isDpExists = winccoa.dpExists('ExampleDP_Arg1.');
} catch (exc) {
  console.error(exc);
}
console.info("Is ExampleDP_Arg1 exists - " + isDpExists);
```

<a id="dpget"></a>

##### dpGet()

> **dpGet**(`dpeNames`): `Promise`\<`unknown`\>

Get the current values of one or more data point elements.

###### Parameters

###### dpeNames

Data point element name(s) of the values to get.

`string` | `string`[]

###### Returns

`Promise`\<`unknown`\>

Promise that resolves to the current value(s) of the DPE(s). The received values
         must be cast to their expected types before they can be used.

###### Throws

[WinccoaError](#winccoaerror) when DPE does not exist or current user has no read access to it.

###### See

[CTRL function `dpGet()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGet.html)

###### Example

```ts
const dpes = ['ExampleDP_Arg1.', 'ExampleDP_DDE.b1'];
try {
  const values = (await winccoa.dpGet(dpes)) as [number, boolean];
  for (let i = 0; i < dpes.length; i++) {
    console.info(`${dpes[i]}: ${values[i]}`);
  }
} catch (exc) {
  console.error(exc);
}
```

<a id="dpgetalias"></a>

##### dpGetAlias()

> **dpGetAlias**(`dpeName`): `string`

Returns the alias for the specified data point.

###### Parameters

###### dpeName

`string`

Data point element

###### Returns

`string`

the appropriate alias in the language. Note that the alias can be only unilingual.

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type.

###### See

- [dpSetAlias](#dpsetalias)
- [dpAliasToName](#dpaliastoname)
- [CTRL function `dpGetAlias()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetAlias.html)

###### Example

```ts
try {
  const alias = winccoa.dpGetAlias('ExampleDP_Rpt1.');
  console.info('DP alias: ' + alias);
} catch (exc) {
  console.error(exc);
}
```

<a id="dpgetallaliases"></a>

##### dpGetAllAliases()

> **dpGetAllAliases**(`aliasFilter`, `dpeFilter`): `object`

Returns data points and their aliases with the possibility to filter by data point element and/or alias.

###### Parameters

###### aliasFilter

`string` = `''`

Pattern string for filtering the aliases (for example,`'Engine*'`, `'*'`).

###### dpeFilter

`string` = `''`

Pattern string for filtering data point elements (for example `'*.para'`).
                 An empty dpe pattern (`''`) and a `'*'` are treated like ALL DPEs. Also queries on
                 remote systems can be executed. The system is part of the dpeFilter (for example,
                 `'Sys23:*.**'` - returns all aliases of a specific system; `'*:*.**'` would return
                 the aliases of all systems. you can use it e.g. in a distributed system). Several
                 systems can be defined with a list (for example, `'Sys{1,2,3,45}:Ex*'`).

###### Returns

Object containing two arrays with DPE names and their aliases that matching filter criteria.
        Both arrays have the same size.

###### aliases

> **aliases**: `string`[]

Aliases corresponding to the DPEs in __dpNames__.

###### dpNames

> **dpNames**: `string`[]

Data point elements.

###### See

- [dpGetAlias](#dpgetalias)
- [CTRL function `dpGetAllAliases()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetAllAliases.html)
```ts
const { aliases, dpNames } = winccoa.dpGetAllAliases('*Pub*', '*Group*.');
for (let i = 0; i < aliases.length; i++)
  console.info(`${aliases[i]} --> ${dpNames[i]}`);
```

<a id="dpgetallattributes"></a>

##### dpGetAllAttributes()

> **dpGetAllAttributes**(`configName`): `string`[]

Returns all attributes for the given config name.

###### Parameters

###### configName

`string`

Name of the config.

###### Returns

`string`[]

Array of attributes of a config.

###### Throws

[WinccoaError](#winccoaerror) in case of an invalid argument type.

###### See

- [dpGetAllConfigs](#dpgetallconfigs)
- [CTRL function `dpGetAllAttributes()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetAllAttributes.html)

###### Example

```ts
function getAllDetails() {
  try {
    const atts = winccoa.dpGetAllAttributes('_original');
    console.info(atts, 'number of attributes = ' + atts.length);
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="dpgetallconfigs"></a>

##### dpGetAllConfigs()

> **dpGetAllConfigs**(`dpNameOrType`): `string`[]

Returns all possible configs, which are allowed to configure for the given data point element or data point type.

###### Parameters

###### dpNameOrType

Name of the data point element or data point type. See [WinccoaElementType](#winccoaelementtype).

`string` | [`WinccoaElementType`](#winccoaelementtype)

###### Returns

`string`[]

Array of configs for __dpNameOrType__.

###### Throws

[WinccoaError](#winccoaerror) when data point or type with the given __dpNameOrType__ is not found or invalid argument type.

###### See

- [WinccoaElementType](#winccoaelementtype)
- [CTRL function `dpGetAllConfigs()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetAllConfigs.html)

###### Example

```ts
import { WinccoaManager, WinccoaElementType } from 'winccoa-manager';
const winccoa = new WinccoaManager();

function getAllConfigs() {
  try {
    const configs = winccoa.dpGetAllConfigs(WinccoaElementType.String);
    console.info(configs);
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="dpgetalldescriptions"></a>

##### dpGetAllDescriptions()

> **dpGetAllDescriptions**(`descriptionFilter?`, `dpeFilter?`, `mode?`): `object`

Returns all data points and all descriptions that correspond to the given filters.

###### Parameters

###### descriptionFilter?

`string`

Pattern string for filtering the descriptions (optional, default: `*`).

###### dpeFilter?

`string`

Pattern string for filtering data point elements (optional, default: `*.**`).
       An empty pattern ("") and a `*` are treated like `*.**`.

###### mode?

`number`

Mode of functionality.
       For more details on all modes description see
       [CTRL function `dpGetAllDescriptions()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetAllDescriptions.html).

###### Returns

Object containing two arrays with data point names and their corresponding description.

###### descriptions

> **descriptions**: [`WinccoaLangString`](#winccoalangstring)[]

Descriptions corresponding to the DPEs in __dpNames__

###### dpNames

> **dpNames**: `string`[]

Data point names.

###### See

- [dpGetDescription](#dpgetdescription)
- [CTRL function `dpGetAllDescriptions()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetAllDescriptions.html)

###### Example

```ts
const { dpNames, descriptions } = winccoa.dpGetAllDescriptions('*', 'Example*');
for (let i = 0; i < dpNames.length; i++)
  console.info(`Description for ${dpNames[i]}: ${descriptions[i]}`);
```

<a id="dpgetalldetails"></a>

##### dpGetAllDetails()

> **dpGetAllDetails**(`configName`): `string`[]

Returns all details of a given config name.

###### Parameters

###### configName

`string`

Name of the config.

###### Returns

`string`[]

Array of details of a config.

###### Throws

[WinccoaError](#winccoaerror) in case of an invalid argument type.

###### See

- [dpGetAllConfigs](#dpgetallconfigs)
- [CTRL function `dpGetAllDetails()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetAllDetails.html)

###### Example

```ts
try {
  const details = winccoa.dpGetAllDetails('_auth');
  console.info(details);
} catch (exc) {
  console.error(exc);
}
```

<a id="dpgetdescription"></a>

##### dpGetDescription()

> **dpGetDescription**(`dpeName`, `mode?`): [`WinccoaLangString`](#winccoalangstring)

Returns the comment (description) for the data point.

###### Parameters

###### dpeName

`string`

Data point element or data point

###### mode?

`number`

Mode of functionality.
For more details on all modes description see
[CTRL function `dpGetDescription()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetDescription.html).

###### Returns

[`WinccoaLangString`](#winccoalangstring)

Description in all available languages as or empty strings in all languages.
> The returned data type can be defined with [setOptions](#setoptions).

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type.

###### See

- [dpSetDescription](#dpsetdescription)
- [CTRL function `dpGetDescription()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetDescription.html)

###### Example

```ts
let description;
try {
  description = winccoa.dpGetDescription('ExampleDP_Rpt1.');
} catch (exc) {
  console.error(exc);
  description = null;
}

if (description)
  console.info('DP description: ' + description);
```

<a id="dpgetformat"></a>

##### dpGetFormat()

> **dpGetFormat**(`dpeName`): [`WinccoaLangString`](#winccoalangstring)

This function returns the numerical format(s) of a data point.

###### Parameters

###### dpeName

`string`

Data point element

###### Returns

[`WinccoaLangString`](#winccoalangstring)

Returns a string that contains the format (for example, '%6.2f') in one or several
         languages or an empty string if an error occured.
> The returned data type can be defined with [setOptions](#setoptions).

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type.

###### See

- [dpSetFormat](#dpsetformat)
- [CTRL function `dpGetFormat()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetFormat.html)

###### Example

```ts
let formats;
try {
  formats = winccoa.dpGetFormat('ExampleDP_Rpt1.');
} catch (exc) {
  console.error(exc);
  formats = null;
}

if (formats)
  console.info('DP formats: ' + formats);
```

<a id="dpgetid"></a>

##### dpGetId()

> **dpGetId**(`dpName`): `number`[]

Returns the data point ID and the element ID of the given data point.

###### Parameters

###### dpName

`string`

Name of the data point.

###### Returns

`number`[]

Array of size 2 with the first value - data point ID and the second value - element ID.

###### Throws

[WinccoaError](#winccoaerror) in case of an invalid argument type or data point does not exist.

###### See

- [dpGetName](#dpgetname)
- [CTRL function `dpGetId()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetId.html)

###### Example

```ts
const dpe = 'ExampleDP_DDE.f1';
try {
  const dpEl_id = winccoa.dpGetId(dpe);
  console.info('data point ID = ' + dpEl_id[0], 'element id = ' + dpEl_id[1]);
} catch (exc) {
  console.error(exc);
}
```

<a id="dpgetmaxage"></a>

##### dpGetMaxAge()

> **dpGetMaxAge**(`age`, `dpeNames`): `Promise`\<`unknown`\>

The function returns the value(s) of one or more data point elements from the driver.
This function is available for the OPC UA Client, Modbus, S7Plus, SNMP, OPC drivers and S-Bus driver.
The use of this function is only useful if an input or input/output peripheral address exists for a data point element.
If a peripheral address exists, the function triggers a singleQuery for a driver
if the value of the data point element __dpName__ is older than the parameter __age__.
The function returns the value from the driver.
If a peripheral address does not exist,
the function works as the function [dpGet](#dpget) meaning that the function returns a value immediately irrespective of how old the value is.

###### Parameters

###### age

`number`

The maximum age of the value in milliseconds. When value is older than age, then value from the driver is returned.

###### dpeNames

Data point element name(s) whose value is queried.

`string` | `string`[]

###### Returns

`Promise`\<`unknown`\>

Promise that resolves to the current value(s) of the DPE(s). The received values
         must be cast to their expected types before they can be used.

###### Throws

[WinccoaError](#winccoaerror) when DPE does not exist or current user has no read access to it.

###### See

- [CTRL function `dpGetMaxAge()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetMaxAge.html)
- [dpGet](#dpget)

###### Example

```ts
const dpes = ['EIPtestCompactIN.BOOL', 'EIPtestCompactIN.INT', 'EIPtestCompactIN.STRING'];
try {
  // get value with the max age less than 5 seconds
  const values = (await winccoa.dpGetMaxAge(5000, dpes)) as [boolean, number, string];
  for (let i = 0; i < dpes.length; i++) {
    console.info(`${dpes[i]}: ${values[i]}`);
  }
} catch (exc) {
  console.error(exc);
}
```

<a id="dpgetname"></a>

##### dpGetName()

> **dpGetName**(`dpId`, `elemId`, `systemId?`): `string`

Returns the data point name for the given data point ID and element ID.

###### Parameters

###### dpId

`number`

Data point ID.

###### elemId

`number`

Element ID.

###### systemId?

`number`

System ID (optional). When not specified - own system.

###### Returns

`string`

The data point name.

###### Throws

[WinccoaError](#winccoaerror) in case of an invalid argument type or data point does not exist with the given ID.

###### See

- [dpGetId](#dpgetid)
- [getSystemId](#getsystemid)
- [CTRL function `dpGetName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetName.html)

###### Example

```ts
try {
  const dpName = winccoa.dpGetName(1, 1);
  console.info('data point with id 1 and element id 1 =' + dpName);
} catch (exc) {
  console.error(exc);
}
```

<a id="dpgetperiod"></a>

##### dpGetPeriod()

> **dpGetPeriod**(`startTime`, `endTime`, `dpeList`, `count`): `Promise`\<`object`[]\>

Queries DP attributes over a specified period of time.

###### Parameters

###### startTime

[`WinccoaTime`](#winccoatime)

The start time of the interval from which values should be returned.

###### endTime

[`WinccoaTime`](#winccoatime)

The end time of the interval from which values should be returned.

###### dpeList

`string`[]

Single or multiple Data Points in an array.

###### count

`number` = `0`

Optional number of values before startTime and after endTime that will
              also be returned.

###### Returns

`Promise`\<`object`[]\>

Promise will be resolved to data for the given DPEs if successful. It
         consists of an array of results (one for each DPE, in the order they are
         given in __dpeList__), each result contains two arrays, one for the
         values and one for the corresponding value change timestamps).

###### Throws

Promise will be rejected with [WinccoaError](#winccoaerror) in case of:
- empty data point list __dpList__
- data point not found
- invalid __requestId__

###### See

- [CTRL function `dpGetPeriod()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetPeriod.html)
- [dpGetPeriodSplit](#dpgetperiodsplit)

###### Example

```ts
const dpe = 'System1:ExampleDP_Trend1.';
  const startTime = new Date(2023);
  const endTime = new Date(2025);
  console.log(await winccoa.dpGetPeriod(startTime, endTime, [dpe]));
```

<a id="dpgetperiodsplit"></a>

##### dpGetPeriodSplit()

###### Call Signature

> **dpGetPeriodSplit**(`startTime`, `endTime`, `dpeList`, `count?`): `Promise`\<\{ `answerId`: `number`; `data`: `object`[]; `id`: `number`; `progress`: `number`; \}\>

Queries DP attributes over a specified period of time.
There are two calls, the first call described below and
subsequent calls with __requestId__.

###### Parameters

###### startTime

[`WinccoaTime`](#winccoatime)

The start time of the interval from which values should be returned.

###### endTime

[`WinccoaTime`](#winccoatime)

The end time of the interval from which values should be returned.

###### dpeList

`string`[]

Single or multiple Data Points in an array.

###### count?

`number`

Optional number of values before startTime and after endTime that also
              have to be read out.

###### Returns

`Promise`\<\{ `answerId`: `number`; `data`: `object`[]; `id`: `number`; `progress`: `number`; \}\>

Promise will be resolved to an object containing:
- __id__ Unique ID which must be used in subsequent calls (this is invalid when __progress__ is 100)
- __answerId__ Request or answer ID from data manager.
- __progress__ Shows how much of the function was executed. 100 means that the function was executed completely.
- __data__ Data identically to the result of [dpGetPeriod](#dpgetperiod),

###### Remarks

Use this function signature for the first call.

###### Throws

Promise will be rejected with [WinccoaError](#winccoaerror) in case of:
- empty data point list __dpList__
- data point not found
- invalid __requestId__

###### See

- [CTRL function `dpGetPeriodSplit()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetPeriodSplit.html)
- [dpGetPeriod](#dpgetperiod)
- [dpQuerySplit](#dpquerysplit)
- [dpCancelSplitRequest](#dpcancelsplitrequest)

###### Example

```ts
async function test() {
 const dpe = 'System1:ExampleDP_Trend1.';
 const startTime = new Date(2023);
 const endTime = new Date(2025);

 const showResult = function (data: { times: WinccoaTime[]; values: unknown[] }[]) {
   if (data.length > 0) {
     const { times, values } = data[0];
     for (let i = 0; i < data[0].times.length; i++) {
       console.info(
         `query line - timestamp = '${times[i]}' - value = ${values[i]}`,
       );
     }
   }
 };

let result = await winccoa.dpGetPeriodSplit(startTime, endTime, [dpe]);
 showResult(result.data);
 while (result.progress != 100) {
   result = await winccoa.dpGetPeriodSplit(result.id);
   showResult(result.data);
 }
}

await test();
```

###### Call Signature

> **dpGetPeriodSplit**(`requestId`): `Promise`\<\{ `answerId`: `number`; `data`: `object`[]; `id`: `number`; `progress`: `number`; \}\>

Queries DP attributes over a specified period of time.

###### Parameters

###### requestId

`number`

ID, only, subsequent calls.

###### Returns

`Promise`\<\{ `answerId`: `number`; `data`: `object`[]; `id`: `number`; `progress`: `number`; \}\>

Promise as described in [dpGetPeriodSplit](#dpgetperiodsplit) above.

###### Remarks

Use this function signature for subsequent call.

###### See

- [CTRL function `dpGetPeriodSplit()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetPeriodSplit.html)
- [dpQuerySplit](#dpquerysplit)

<a id="dpgetunit"></a>

##### dpGetUnit()

> **dpGetUnit**(`dpeName`): [`WinccoaLangString`](#winccoalangstring)

This function returns the unit(s) of a data point.

###### Parameters

###### dpeName

`string`

Data point element

###### Returns

[`WinccoaLangString`](#winccoalangstring)

Returns the unit in one or several languages. In the event of an
         error, an empty string is returned.
> The returned data type can be defined with [setOptions](#setoptions).

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type.

###### See

- [dpSetUnit](#dpsetunit)
- [setOptions](#setoptions)
- [CTRL function `dpGetUnit()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetUnit.html)

###### Example

```ts
try {
  let units = winccoa.dpGetUnit('ExampleDP_Rpt1.');
  console.info('DP units: ' + units);
} catch (exc) {
  console.error(exc);
}
```

<a id="dpnames"></a>

##### dpNames()

> **dpNames**(`dpPattern`, `dpType`, `ignoreCase`): `string`[]

Returns all the data point names or the data point element names that match a pattern in alphabetical order.

###### Parameters

###### dpPattern

`string` = `''`

Serach pattern. When an empty pattern is given (=default), then returns all data points.
<br>Wildcards are used to filter data point name.
The charcters `*` and `?` are used for the purpose,
where the asterisk (`*`) replaces any number of characters and the question mark `?` stands for just one character.
Only data points that have the same number of levels as specified are found.
Levels are separated by a period. `dpNames(**)` is equivalent to `dpNames(*.*)`.
<br>Furthermore:
- `:*` returns all configs, `:config.*` returns all details, `:config.detail.*` returns all attributes
- `dp.el:*` returns only the configs according to the DPE. , for example, no `_original` for a node.

<br>Wildcards can be used in arrays (square brackets , e.g.: `[0,3,5-7]` - numbers 0,3,5,6,7) or outside arrays in option lists (in curly brackets `{}`).
<br>Example of wildcards in lists of options:
```
winccoa.dpNames('{*.Ala.*,*.Ala*}', dpType);
winccoa.dpNames('*{.Ala.,.Ala}*', dpType);
winccoa.dpNames('*.A{la.,la}*', dpType);
winccoa.dpNames('*.Al{a.,a}*', dpType);
winccoa.dpNames('*.Ala{.,}*', dpType);
winccoa.dpNames('*.Ala{.}*', dpType);
winccoa.dpNames('*.Ala.*', dpType);
winccoa.dpNames('*.Ala*', dpType);
```

###### dpType

`string` = `''`

Data point type. Allows to restrict the returned data points to a specific data point type.
When using the parameter only data points that match the pattern and the selected data point type will be returned.

###### ignoreCase

`boolean` = `false`

Defines if the search should ignore the casing of the search pattern (=true) or not (=false, default)

###### Returns

`string`[]

List with data points or data point element names.

###### Throws

[WinccoaError](#winccoaerror) when invalid argument type is given.

###### See

- [CTRL function `dpNames()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpNames.html)

###### Example

```ts
let foundDpNames: string[] = [];
try {
  foundDpNames = winccoa.dpNames('ExampleDP*', 'ExampleDP_Float');
} catch (exc) {
  console.error(exc);
}

for (let i = 0; i < foundDpNames.length; i++) {
  console.info("DPE name: " + foundDpNames.at(i));
}
```

<a id="dpquery"></a>

##### dpQuery()

> **dpQuery**(`query`): `Promise`\<`unknown`[][]\>

Retrieves attribute values with the help of SQL statements.

###### Parameters

###### query

`string`

SQL statement.

###### Returns

`Promise`\<`unknown`[][]\>

Promise - will be resolved to `true` if successful or rejected with an error.

###### Remarks

The query result has a table-like structure:
[0][0] (empty)    | [0][1] column header   |         ...
----------------- | ---------------------- | ----------------------
[1][0] line name  | [1][0] content of line |         ...
[2][0] line name  | [2][1] content of line |         ...
...               | ...                    |         ...

e.g. this is the output for the query `"SELECT '_original.._value' FROM 'ExampleDP_Arg*'"` converted
to JSON:
```
[
  ["",":_original.._value"],
  ["System1:ExampleDP_Arg1.",2.43],
  ["System1:ExampleDP_Arg2.",5.76]
]
```

###### Throws

[WinccoaError](#winccoaerror) when invalid parameter or query string is given.

###### See

- [dpQueryConnectSingle](#dpqueryconnectsingle)
- [dpQueryConnectAll](#dpqueryconnectall)
- [CTRL function `dpQuery()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpQuery.html)

###### Example

```ts
let result;
try {
  result = await winccoa.dpQuery(
    `SELECT '_original.._stime', '_original.._value' FROM 'ExampleDP_Arg*'`,
  );
} catch (exc) {
  console.error(exc);
  result = null;
}
if (result) {
  const queryTable: string[][] = result as string[][];
  for (let i = 0; i < queryTable.length; i++) {
    console.info(
      `query line - name: '%s' - timestamp = %s - value = %s`,
      ...queryTable[i],
    );
  }
}
 ```

<a id="dpqueryconnectall"></a>

##### dpQueryConnectAll()

> **dpQueryConnectAll**(`callback`, `answer`, `query`, `blockingTime`): `number`

Calls __callback__ whenever one or more DPEs which meet the query condition change.

> It is recommended to use [dpQueryConnectSingle](#dpqueryconnectsingle) if possible from the
> performance point of view.

###### Parameters

###### callback

[`WinccoaDpQueryConnectCallback`](#winccoadpqueryconnectcallback)

Function that is called whenever a subscribed DPE value changes.
                The update message will contain all subscribed DPEs.

###### answer

`boolean`

if true, callback is called with the initial DPE values right away, if false,
              callback is only called for an actual value change.

###### query

`string`

query as an SQL statement.

###### blockingTime

`number` = `-1`

Time in milli-seconds when the call of the callback function is blocked by an
                    open query. In this time, query results are collected and then returned after
                    __blockingTime__ in a single callback. If __blockingTime__ is set to 0, the
                    callback function is called immediately when a value is updated. If not given,
                    the blocking time is read from the config entry `queryHLBlockedTime`.

###### Returns

`number`

ID of the new connection (>= 0). This can be used to disconnect from
         updates if required with [dpQueryDisconnect](#dpquerydisconnect). Otherwise the connection will be closed
         when the manager exits.

###### Throws

[WinccoaError](#winccoaerror) when invalid parameter types, empty or invalid query, etc.
> When the query passed to this method is invalid, no exception is thrown,
> but the first (and only) callback will contain a [WinccoaError](#winccoaerror) instead.

###### Remarks

For an example describing how to pass user data to a callback, see the second example
         for [WinccoaDpQueryConnectCallback](#winccoadpqueryconnectcallback).

###### See

- [dpQuery](#dpquery)
- [dpQueryConnectSingle](#dpqueryconnectsingle)
- [dpQueryDisconnect](#dpquerydisconnect)
- [WinccoaConnectUpdateType](#winccoaconnectupdatetype)
- [CTRL function `dpQueryConnectAll()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpQueryConnectAll.html)

###### Example

```ts
import {
  WinccoaManager,
  WinccoaConnectUpdateType,
  WinccoaError
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function  queryConnectCB (
  values: unknown[][],
  type: WinccoaConnectUpdateType,
  error?: WinccoaError
) {
  if (error) {
    console.log(error);
    return;
  }

  if (type == WinccoaConnectUpdateType.Answer)
    console.warn('--- Initial update ---');

  for (let i = 0; i < values.length; i++) {
    console.info(`DPE = '%s', value = %s`, ...values[i]);
  }
}

function connect() {
  let id = -1;
  try {
    id = winccoa.dpQueryConnectAll(
      queryConnectCB,
      true,
      `SELECT '_online.._value' FROM '*' WHERE _DPT="ExampleDP_Float"`
    );
  } catch (exc) {
    console.error(exc);
  }
}
 ```

<a id="dpqueryconnectsingle"></a>

##### dpQueryConnectSingle()

> **dpQueryConnectSingle**(`callback`, `answer`, `query`, `blockingTime`): `number`

Calls __callback__ whenever one or more DPEs which meet the query condition are changed.

###### Parameters

###### callback

[`WinccoaDpQueryConnectCallback`](#winccoadpqueryconnectcallback)

Function that is called whenever a subscribed DPE value changes.
                The update message will contain only changed DPEs.

###### answer

`boolean`

if true, callback is called with the initial DPE values right away, if false,
              callback is only called for an actual value change.

###### query

`string`

query as an SQL statement.

###### blockingTime

`number` = `-1`

Time in milli-seconds when the call of the callback function is blocked by an
                    open query. In this time, query results are collected and then returned after
                    __blockingTime__ in a single callback. If __blockingTime__ is set to 0, the
                    callback function is called immediately when a value is updated. If not given,
                    the blocking time is read from the config entry `queryHLBlockedTime`.

###### Returns

`number`

ID of the new connection (>= 0). This can be used to disconnect from
         updates if required with [dpQueryDisconnect](#dpquerydisconnect). Otherwise the connection will be closed
         when the manager exits.

###### Throws

[WinccoaError](#winccoaerror) when invalid parameter types, empty query, etc.
> When the query passed to this method is invalid, no exception is thrown,
> but the first (and only) callback will contain a [WinccoaError](#winccoaerror) instead.

###### Remarks

For an example describing how to pass user data to a callback, see the second example
         for [WinccoaDpQueryConnectCallback](#winccoadpqueryconnectcallback).

###### See

- [dpQuery](#dpquery)
- [dpQueryConnectAll](#dpqueryconnectall)
- [dpQueryDisconnect](#dpquerydisconnect)
- [WinccoaConnectUpdateType](#winccoaconnectupdatetype)
- [CTRL function `dpQueryConnectSingle()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpQueryConnectSingle.html)

###### Example

```ts
import {
  WinccoaManager,
  WinccoaConnectUpdateType,
  WinccoaError
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function  queryConnectCB (
  values: unknown[][],
  type: WinccoaConnectUpdateType,
  error?: WinccoaError
) {
  if (error) {
    console.log(error);
    return;
  }

  if (type == WinccoaConnectUpdateType.Answer)
    console.warn('--- Initial update ---');

  for (let i = 0; i < values.length; i++) {
    console.info(`DPE = '%s', value = %s`, ...values[i]);
  }
}

function connect() {
  let id = -1;
  try {
    id = winccoa.dpQueryConnectSingle(
      queryConnectCB,
      true,
      `SELECT '_online.._value' FROM '*' WHERE _DPT="ExampleDP_Float"`
    );
  } catch (exc) {
    console.error(exc);
  }
}
 ```

<a id="dpquerydisconnect"></a>

##### dpQueryDisconnect()

> **dpQueryDisconnect**(`id`): `number`

Disconnect from [dpQueryConnectSingle](#dpqueryconnectsingle) (or [dpQueryConnectAll](#dpqueryconnectall)) .

###### Parameters

###### id

`number`

ID of the connection to close as returned by [dpQueryConnectAll](#dpqueryconnectall) or [dpQueryConnectSingle](#dpqueryconnectsingle).

###### Returns

`number`

ID of the closed connection (>= 0).

###### Throws

[WinccoaError](#winccoaerror) when __id__ is not found or invalid.

###### See

- [dpQueryConnectAll](#dpqueryconnectall)
 - [dpQueryConnectSingle](#dpqueryconnectsingle)

###### Example

```ts
import {
  WinccoaManager,
  WinccoaConnectUpdateType,
  WinccoaError
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function connect() {
let id = -1;
  try {
    id = winccoa.dpQueryConnectSingle(
      function (
        values: unknown[][],
        type: WinccoaConnectUpdateType,
        error?: WinccoaError
      ) {
        if (error) {
          console.log(error);
          return;
        }

        console.info(values)
      },
      true,
      "SELECT '_online.._value' FROM '*' WHERE _DPT= \"ExampleDP_Float\""
      );
  } catch (exc) {
    console.error(exc);
  }
}

function disconnect() {
  try {
    winccoa.dpQueryDisconnect(id);
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="dpquerysplit"></a>

##### dpQuerySplit()

> **dpQuerySplit**(`queryOrId`): `Promise`\<\{ `answerId`: `number`; `data?`: `unknown`[][]; `id`: `number`; `progress`: `number`; \}\>

Query attributes of a set of data points as an SQL-like query string.
Use the function when you query a large amount of data.
The function reduces the system load and offers a considerable advantage when dealing with a large amount of data.
To cancel a dpQuerySplit use [dpCancelSplitRequest](#dpcancelsplitrequest).
After [WinccoaOptions.splitTimeout](#splittimeout) milliseconds, the __id__ is invalid.

###### Parameters

###### queryOrId

First call: SQL statement, subsequent calls: ID.

`string` | `number`

###### Returns

`Promise`\<\{ `answerId`: `number`; `data?`: `unknown`[][]; `id`: `number`; `progress`: `number`; \}\>

Promise will be resolved to an object containing:
- __id__ Unique ID which must be used in subsequent calls (this is invalid when __progress__ is 100)
- __answerId__ Request or answer ID from data manager.
- __progress__ Shows how much of the function was executed. 100 means that the function was executed completely.
- __data__ Data identically to the result of [dpQuery](#dpquery).

###### Throws

Promise will be rejected with [WinccoaError](#winccoaerror) in case of:
- query is invalid
- id is invalid
- dpQuerySplit is called again without waiting for previous dpQuerySplit promise to be resolved or rejected.

###### Throws

Various argument errors.

###### See

- [CTRL function `dpQuerySplit()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpQuerySplit.html)
- [dpQuery](#dpquery)
- [dpCancelSplitRequest](#dpcancelsplitrequest)

###### Example

```ts
async function test() {
  // TIMERANGE: use historic data, otherwise no split occur
   const query = `SELECT '_original.._stime', '_original.._value' FROM '_*' TIMERANGE("1970-01-01T00:00:00.000Z", "2060-01-01T00:00:00.000Z", 0, 0)`;
 let result;

  const showResult = function (queryTable: string[][]) {
    for (let i = 0; i < queryTable.length; i++) {
      console.info(
        `query line - name: '%s' - timestamp = %s - value = %s`,
        ...queryTable[i],
      );
    }
  };

  result = await winccoa.dpQuerySplit(query);
  showResult(result.data as string[][]);
  while (result.progress != 100) {
    result = await winccoa.dpQuerySplit(result.id);
    showResult(result.data as string[][]);
  }
}
await test();
 ```

<a id="dpset"></a>

##### dpSet()

> **dpSet**(`dpeNames`, `values`): `boolean`

Set the value of one or more data point element(s).

###### Parameters

###### dpeNames

Data point element name(s) of the values to set.

`string` | `string`[]

###### values

`unknown`

Values to set. Must have the same size as __dpeNames__. If __dpeNames__ is a
              single string and not an array, this parameter must also be a single value
              and not an array.

###### Returns

`boolean`

`true` if successful, otherwise [WinccoaError](#winccoaerror) wil be thrown instead.
> Since this method does not wait for the actual value update
> in the database, __the update can still fail__ after this method returned `true`. Use
[dpSetWait](#dpsetwait) to also get informed about these errors.

###### Throws

[WinccoaError](#winccoaerror) when DPE names do not exist, values cannot be converted, array
        sizes mismatch etc.

###### See

- [dpSetWait](#dpsetwait)
- [dpSetTimed](#dpsettimed)
- [dpSetTimedWait](#dpsettimedwait)
- [CTRL function `dpSet()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSet.html)

###### Example

```ts
const dpes = ['ExampleDP_Arg1.', 'ExampleDP_DDE.b1'];
const values = [123.456, false];
try {
  winccoa.dpSet(dpes, values); // Two arrays of size 2
  winccoa.dpSet('ExampleDP_Arg2.', 2); // single value
} catch (exc) {
  console.error(exc);
}
```

<a id="dpsetalias"></a>

##### dpSetAlias()

> **dpSetAlias**(`dpeName`, `alias`): `Promise`\<`boolean`\>

Sets the alias for the specified data point element.

###### Parameters

###### dpeName

`string`

Data point element

###### alias

`string`

Alias to be set. Note that the alias can be set only unilingual.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to true if successful or rejected with an error.

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type, etc.

###### See

- [dpGetAlias](#dpgetalias)
- [CTRL function `dpSetAlias()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSetAlias.html)

###### Example

```ts
let isSuccess = false;
try {
  isSuccess = await winccoa.dpSetAlias('ExampleDP_Rpt1.', 'rpt1Alias');
} catch (exc) {
  console.error(exc);
}

console.info('DP alias is set successfully - ' + isSuccess);
```

<a id="dpsetandwaitforvalue"></a>

##### dpSetAndWaitForValue()

> **dpSetAndWaitForValue**(`dpNamesSet`, `dpValuesSet`, `dpNamesWait`, `conditions`, `dpNamesReturn`, `timeoutMs`): `Promise`\<`unknown`\>

This function sets the data points listed in __dpNamesSet__ to the values
given in __dpValuesSet__ and waits for another set of data points to change their
values until all specified __conditions__ are met (that is, all values of the data
points listed in __dpNamesWait__ are equal to the values given in __conditions__).
Once __conditions__ are fulfilled, it returns the values of another set of data
points (given in __dpNamesReturn__). If the conditions are not met within the
specified __timeoutMs__ period, the promise is rejected.

> __NOTE__
>
> The values in __conditions__ are compared directly in TypeScript, not by WinCC OA.
> Therefore the comparision is not as strict as it would be when using the CTRL
> function `dpSetAndWaitForValue()`, which also checks the type of the values. For
> example, in CTRL an integer value will never match a float value, also if both have
> the same numeric value, while in JavaScript the comparision will only based on the
> numeric value.

###### Parameters

###### dpNamesSet

`string`[]

Names of the data points to set.

###### dpValuesSet

`unknown`[]

Values to set, must have the same size as __dpNamesSet__.

###### dpNamesWait

`string`[]

Names of the data points to wait for a value change.

###### conditions

`unknown`[]

Expected values for the data points in __dpNamesWait__ to
                  wait for. Must have the same size as __dpNamesWait__.

###### dpNamesReturn

`string`[]

Names of the data points whose values will be
                  returned in the Promise.

###### timeoutMs

`number` = `0`

Optional timeout for waiting on __conditions__.

###### Returns

`Promise`\<`unknown`\>

Promise containing the values for __dpNamesReturn__ .

###### Throws

[WinccoaError](#winccoaerror) when timeout expired, DPE names do not exist,
        values cannot be converted, array sizes mismatch, no write access etc.

###### See

- [dpWaitForValue](#dpwaitforvalue)
- [dpSetWait](#dpsetwait)
- [CTRL function `dpSetAndWaitForValue()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSetAndWaitForValue.html)

###### Example

```ts
const argNames = ['ExampleDP_Arg1.', 'ExampleDP_Arg2.'];
const resultName = ['ExampleDP_Result.'];

console.log(
  await winccoa.dpSetAndWaitForValue(
    argNames,
    [3, 7],
    resultName,
    [10],
    argNames.concat(resultName),
    1000,
  ),
);
```

<a id="dpsetdescription"></a>

##### dpSetDescription()

> **dpSetDescription**(`dpeName`, `comment`): `Promise`\<`boolean`\>

Sets a comment (description) for the data point.

###### Parameters

###### dpeName

`string`

Data point element to be commented on.

###### comment

[`WinccoaLangString`](#winccoalangstring)

Comment in one or all languages.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful or rejected with an error.

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type, etc.

###### See

- [dpGetDescription](#dpgetdescription)
- [CTRL function `dpSetDescription()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSetDescription.html)

###### Example

```ts
let isSuccess = false;
try {
  isSuccess = await winccoa.dpSetDescription('ExampleDP_Rpt1.', {
     'de_AT.utf8': 'German description',
     'en_US.utf8': 'English description',
     'ru_RU.utf8': 'Russian description',
   });
} catch (exc) {
  console.error(exc);
}

console.info('DP description is set successfully - ' + isSuccess);
```

<a id="dpsetformat"></a>

##### dpSetFormat()

> **dpSetFormat**(`dpeName`, `format`): `Promise`\<`boolean`\>

Sets the numerical format(s) of a data point.

###### Parameters

###### dpeName

`string`

Data point element

###### format

[`WinccoaLangString`](#winccoalangstring)

A string that contains the format (for example, '%6.2f') in one or several
               languages.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful or rejected with an error.

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type, etc.

###### See

- [dpGetFormat](#dpgetformat)
- [CTRL function `dpSetFormat()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSetFormat.html)

###### Example

```ts
let isSuccess = false;
try {
  isSuccess = await winccoa.dpSetFormat('ExampleDP_Rpt1.', {
     'de_AT.utf8': '%.4f',
     'en_US.utf8': '%.4f',
     'ru_RU.utf8': '%.2f',
   });
} catch (exc) {
  console.error(exc);
}

  console.info('DP formats are set successfully - ' + isSuccess);
```

<a id="dpsettimed"></a>

##### dpSetTimed()

> **dpSetTimed**(`time`, `dpeNames`, `values`): `boolean`

Set values of one or more data point element(s) with a given source time.

###### Parameters

###### time

[`WinccoaTime`](#winccoatime)

Source time for the value change.

###### dpeNames

Data point element name(s) of the values to set.

`string` | `string`[]

###### values

`unknown`

Values to set. Must have the same size as __dpeNames__. If __dpeNames__ is a
              single string and not an array, this parameter must also be a single value
              and not an array.

###### Returns

`boolean`

Boolean `true` in case of a success, otherwise `false`.
> Since this method does not wait for the actual value update
> in the database, __the update can still fail__ after this method returned `true`. Use
[dpSetTimedWait](#dpsettimedwait) to also get informed about these errors.

###### Throws

[WinccoaError](#winccoaerror) when DPE names do not exist, values cannot be converted, array
        sizes mismatch etc.

###### See

- [dpSet](#dpset)
- [dpSetWait](#dpsetwait)
- [dpSetTimedWait](#dpsettimedwait)
- [CTRL function `dpSetTimed()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSetTimed.html)

###### Example

```ts
const timeStamp = new Date('2023-01-03T04:05:06.789Z');
let isSuccess = false;
try {
  isSuccess = winccoa.dpSetTimed(timeStamp, 'ExampleDP_Arg1.', 2);
} catch (exc) {
  console.error(exc);
}

console.info("dpSetTimed call is successed - " + isSuccess);
```

<a id="dpsettimedwait"></a>

##### dpSetTimedWait()

> **dpSetTimedWait**(`time`, `dpeNames`, `values`): `Promise`\<`boolean`\>

Set values of one or more data point element(s) with a given source time.

###### Parameters

###### time

[`WinccoaTime`](#winccoatime)

Source time for the value change.

###### dpeNames

Data point element name(s) of the values to set.

`string` | `string`[]

###### values

`unknown`

Values to set. Must have the same size as __dpeNames__. If __dpeNames__ is a
              single string and not an array, this parameter must also be a single value
              and not an array.

###### Returns

`Promise`\<`boolean`\>

Promise that resolves to `true` if succesful. If not successful,
         a [WinccoaError](#winccoaerror) wil be thrown instead.

###### Throws

[WinccoaError](#winccoaerror) when DPE names do not exist, values cannot be converted, array
        sizes mismatch, no write access etc.

###### See

- [dpSet](#dpset)
- [dpSetTimed](#dpsettimed)
- [dpSetWait](#dpsetwait)
- [CTRL function `dpSetTimedWait()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSetTimedWait.html)

###### Example

```ts
const timeStamp = new Date('2023-01-03T04:05:06.789Z');
let isSuccess = false;
try {
  isSuccess = await winccoa.dpSetTimedWait(timeStamp, 'ExampleDP_Arg1.', 2);
} catch (exc) {
  console.error(exc);
}

console.info("Time and value are set for ExampleDP_Arg1 - " + isSuccess);
```

<a id="dpsetunit"></a>

##### dpSetUnit()

> **dpSetUnit**(`dpeName`, `unit`): `Promise`\<`boolean`\>

Sets the unit(s) for a data point.

###### Parameters

###### dpeName

`string`

Data point

###### unit

[`WinccoaLangString`](#winccoalangstring)

Unit (for example, kg) in one or several languages.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful or rejected with an error.

###### Throws

[WinccoaError](#winccoaerror) when data point with the given __dpeName__ is not found or invalid argument type, etc.

###### See

- [dpGetUnit](#dpgetunit)
- [CTRL function `dpSetUnit()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSetUnit.html)

###### Example

```ts
let isSuccess = false;
try {
  isSuccess = await winccoa.dpSetUnit('ExampleDP_Rpt1.', {
     'de_AT.utf8': 's',
     'en_US.utf8': 's',
     'ru_RU.utf8': 'c',
   });
} catch (exc) {
  console.error(exc);
}

  console.info('DP units are set successfully - ' + isSuccess);
```

<a id="dpsetwait"></a>

##### dpSetWait()

> **dpSetWait**(`dpeNames`, `values`): `Promise`\<`boolean`\>

Set the value of one or more data point element(s).

###### Parameters

###### dpeNames

Data point element name(s) of the values to set.

`string` | `string`[]

###### values

`unknown`

Values to set. Must have the same size as __dpeNames__. If __dpeNames__ is a
              single string and not an array, this parameter must also be a single value
              and not an array.

###### Returns

`Promise`\<`boolean`\>

Promise that resolves to `true` if succesful. If not successful,
         a [WinccoaError](#winccoaerror) wil be thrown instead.

###### Throws

[WinccoaError](#winccoaerror) when DPE names do not exist, values cannot be converted, array
        sizes mismatch, no write access etc.

###### See

- [dpSet](#dpset)
- [dpSetTimed](#dpsettimed)
- [dpSetTimedWait](#dpsettimedwait)
- [CTRL function `dpSetWait()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSetWait.html)

###### Example

```ts
const dpes = ['ExampleDP_Arg1.', 'ExampleDP_DDE.b1'];
const values = [123.456, false];
try {
  await winccoa.dpSetWait(dpes, values); // Two arrays of size 2
  await winccoa.dpSetWait('ExampleDP_Arg2.', 2); // single value
} catch (exc) {
  console.error(exc);
}
```

<a id="dpsubstr"></a>

##### dpSubStr()

> **dpSubStr**(`dp`, `pattern`): `string`

Gets the part (sub-string) of a data point name given by __pattern__. The neutral form
of configs and attributes is returned.

###### Parameters

###### dp

`string`

Date point element name.

###### pattern

[`WinccoaDpSub`](#winccoadpsub)

Pattern describing the sub-string to select.

###### Returns

`string`

Sub-string given by __pattern__.

###### Throws

[WinccoaError](#winccoaerror) when __dp__ is not a valid data point (element) name.

###### See

- [CTRL function `dpSubStr()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpSubStr.html)
- [WinccoaDpSub](#winccoadpsub)

###### Example

```ts
const dp = '_mp_PUMP1.alert.motorSwitch:_alert_hdl';
console.log(winccoa.dpSubStr(dp, WinccoaDpSub.SYS_DP_EL));
```

<a id="dptypes"></a>

##### dpTypes()

> **dpTypes**(`pattern`, `systemId`, `includeEmpty`): `string`[]

Returns all or selected data point types from the current project.

###### Parameters

###### pattern

`string` = `''`

Pattern for the returned DPTs. When an empty pattern is given (=default), then returns all DP types.
<br>Wildcards are used to filter data point type name.
The charcters `*` and `?` are used for the purpose,
where the asterisk (`*`) replaces any number of characters and the question mark `?` stands for just one character.
<br>Wildcards can be used in arrays (square brackets , e.g.: `[0,3,5-7]` - numbers 0,3,5,6,7) or outside arrays in option lists (in curly brackets `{}`).
<br>Example of wildcards in lists of options:
```
winccoa.dpTypes('{*.Ala.*,*.Ala*}');
winccoa.dpTypes('*{.Ala.,.Ala}*');
winccoa.dpTypes('*.A{la.,la}*');
winccoa.dpTypes('*.Al{a.,a}*');
winccoa.dpTypes('*.Ala{.,}*');
winccoa.dpTypes('*.Ala{.}*');
winccoa.dpTypes('*.Ala.*');
winccoa.dpTypes('*.Ala*');
```

###### systemId

`number` = `-1`

The desired system if querying from other systems. Optional parameter.
                If this parameter is not defined, the own system is queried.

###### includeEmpty

`boolean` = `true`

When this is set to false, data point types without existing
                    data points will be ignored.

###### Returns

`string`[]

String array with all DP type names.

###### Throws

[WinccoaError](#winccoaerror) when invalid argument type or non-existing __systemId__ is given.

###### See

- [CTRL function `dpTypes()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpTypes.html)

###### Example

```ts
try {
  const foundDpTypes = winccoa.dpTypes('ExampleDP*', 1, true);
  for (let i = 0; i < foundDpTypes.length; i++) {
    console.info("DP type: " + foundDpTypes.at(i));
  }
} catch (exc) {
  console.error(exc);
}
```

<a id="dpwaitforvalue"></a>

##### dpWaitForValue()

> **dpWaitForValue**(`dpNamesWait`, `conditions`, `dpNamesReturn`, `timeoutMs`): `Promise`\<`unknown`\>

This function waits for a set of data points to change their values until all
specified  __conditions__ are met (that is, all values of the data points listed in
__dpNamesWait__ are equal to the values given in __conditions__). Once __conditions__
 are fulfilled, it returns the values of another set of data points (given in
__dpNamesReturn__). If the conditions are not met within the specified __timeoutMs__
period, the promise is rejected.

> __NOTE__
>
> The values in __conditions__ are compared directly in TypeScript, not by WinCC OA.
> Therefore the comparision is not as strict as it would be when using the CTRL
> function `dpWaitForValue()`, which also checks the type of the values. For example,
> in CTRL an integer value will not match a float value, also if both have the same
> numeric value, while in JavaScript the comparision will only based on the numeric
> value.

###### Parameters

###### dpNamesWait

`string`[]

Names of the data points to wait for a value change.

###### conditions

`unknown`[]

Expected values for the data points in __dpNamesWait__ to
                  wait for. Must have the same size as __dpNamesWait__.

###### dpNamesReturn

`string`[]

Names of the data points whose values will be
                  returned in the Promise.

###### timeoutMs

`number` = `0`

Optional timeout for waiting on __conditions__.

###### Returns

`Promise`\<`unknown`\>

Promise containing the values for __dpNamesReturn__ .

###### Throws

[WinccoaError](#winccoaerror) when timeout expired, DPE names do not exist,
        values cannot be converted, array sizes mismatch etc.

###### See

- [dpSetAndWaitForValue](#dpsetandwaitforvalue)
- [dpSetWait](#dpsetwait)
- [CTRL function `dpWaitForValue()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpWaitForValue.html)

###### Example

```ts
const argNames = ['ExampleDP_Arg1.', 'ExampleDP_Arg2.'];
const resultName = ['ExampleDP_Result.'];

setTimeout(() => winccoa.dpSet(argNames, [6, 4]), 100);

console.log(
  await winccoa.dpWaitForValue(resultName, [10], argNames.concat(resultName)),
);
```

<a id="namecheck"></a>

##### nameCheck()

> **nameCheck**(`name`, `nameType`): `Promise`\<\{ `name`: `string`; `valid`: `boolean`; \}\>

Checks if a given __name__ contains invalid characters for a specific use (e. g. as
data point or project name) and also provides a version of that name with invalid
characters removed.

###### Parameters

###### name

`string`

The name to check

###### nameType

[`WinccoaNameCheckType`](#winccoanamechecktype)

The type of check to perform, there is a different set of invalid
                characters for each type.

###### Returns

`Promise`\<\{ `name`: `string`; `valid`: `boolean`; \}\>

Promise for an object containing a __valid__ flag and a version of __name__
         without invalid characters.

###### Throws

[WinccoaError](#winccoaerror) in case of an invalid arguments.

###### See

- [WinccoaNameCheckType](#winccoanamechecktype)
- [CTRL function `nameCheck()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/nameCheck.html)

###### Example

```ts
import { WinccoaManager, WinccoaNameCheckType } from 'winccoa-manager';
const winccoa = new WinccoaManager();

...

// checking if a name is valid
if (
  !(await winccoa.nameCheck(nameToCheck, WinccoaNameCheckType.Project)).valid
)
  console.error(`Invalid project name: ${nameToCheck}`);

// automatically correct name if necessary
const name = (await winccoa.nameCheck(nameToCheck, WinccoaNameCheckType.Dp)).name;
```

#### Data Point Type

<a id="dpgetdptyperefs"></a>

##### dpGetDpTypeRefs()

> **dpGetDpTypeRefs**(`dpt`): `object`

Returns all references to other DPTs in a DPT.

###### Parameters

###### dpt

`string`

Name of the data point type to be checked for references (for example,
            "PUMP1")

###### Returns

Object containing two array with references and their corresponding data point element path.

###### dpePaths

> **dpePaths**: `string`[]

Data point element paths corresponding to the references in __refNames__.

###### refNames

> **refNames**: `string`[]

Reference names.

###### Throws

[WinccoaError](#winccoaerror) in case of:
- an invalid argument type or
- __dpt__ does not exist

###### See

- [CTRL function `dpGetDpTypeRefs()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetDpTypeRefs.html)

###### Example

```ts
console.log(winccoa.dpGetDpTypeRefs('PUMP1'));
```

<a id="dpgetrefstodptype"></a>

##### dpGetRefsToDpType()

> **dpGetRefsToDpType**(`reference`): `object`

Returns all DPTs and DPs that contain the specified DPT as a reference.

###### Parameters

###### reference

`string`

Name of the DPT reference to check data point types and data points
                  for (for example, "_MyReference" or "_ValueArchive").

###### Returns

Object containing two arrays with DPT names and the corresponding data point
         element path.

###### dpePaths

> **dpePaths**: `string`[]

Data point element names corresponding to the the DPTs in __dptNames__.

###### dptNames

> **dptNames**: `string`[]

DPT names.

###### Throws

[WinccoaError](#winccoaerror) in case of:
- an invalid argument type

###### Remarks

__reference__ is only a filter and its content causes never an error.

###### See

- [CTRL function `dpGetRefsToDpType()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpGetRefsToDpType.html)

###### Example

```ts
console.log(winccoa.dpGetRefsToDpType('MODE_STATE'));
```

<a id="dptypechange"></a>

##### dpTypeChange()

> **dpTypeChange**(`startNode`): `Promise`\<`boolean`\>

Change an existing data point type tree.
The __startNode__.__name__ must be an existing Data point type name.
The complete type structure under __startNode__ will be replaced.
Use [WinccoaDpTypeNode.newName](#newname) to rename an existing name.

###### Parameters

###### startNode

[`WinccoaDpTypeNode`](#winccoadptypenode)

the top data point type node of the tree.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- invalid argument type is given
- [WinccoaDpTypeNode.name](#name-4) contains invalid characters or is empty
- [WinccoaDpTypeNode.newName](#newname) contains invalid characters or
- [WinccoaDpTypeNode.refName](#refname) is neither empty nor a valid data point

###### See

- [CTRL function `dpTypeChange()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpTypeChange.html)
- [dpTypeCreate](#dptypecreate)
- [dpTypeDelete](#dptypedelete)
- [WinccoaDpTypeNode](#winccoadptypenode)
- [WinccoaElementType](#winccoaelementtype)

###### Example

```ts
import { WinccoaDpTypeNode,  WinccoaElementType, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function test1() {
  const tree =
    new WinccoaDpTypeNode('MyType1', WinccoaElementType.Struct, '', [
      new WinccoaDpTypeNode('text', WinccoaElementType.String, '', [], 'string'),
      new WinccoaDpTypeNode('typeRef', WinccoaElementType.Typeref, 'ExampleDP_Int'),
      new WinccoaDpTypeNode('struct', WinccoaElementType.Struct, '', [
        new WinccoaDpTypeNode('id2', WinccoaElementType.Float)
      ])
    ]);
  console.log(await winccoa.dpTypeChange(tree));
}
test1();
```

<a id="dptypecreate"></a>

##### dpTypeCreate()

> **dpTypeCreate**(`startNode`): `Promise`\<`boolean`\>

Creates a new data point type tree.

###### Parameters

###### startNode

[`WinccoaDpTypeNode`](#winccoadptypenode)

the first data point type node of the tree.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- invalid argument type is given or
- [WinccoaDpTypeNode.name](#name-4) contains invalid characters or is empty
- [WinccoaDpTypeNode.refName](#refname) is neither empty nor a valid data point

###### See

- [CTRL function `dpTypeCreate()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpTypeCreate.html)
- [dpTypeChange](#dptypechange)
- [dpTypeDelete](#dptypedelete)
- [WinccoaDpTypeNode](#winccoadptypenode)
- [WinccoaElementType](#winccoaelementtype)

###### Example

```ts
import { WinccoaDpTypeNode,  WinccoaElementType, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function test1() {
  const tree =
    new WinccoaDpTypeNode('MyType1', WinccoaElementType.Struct, '', [
      new WinccoaDpTypeNode('id', WinccoaElementType.Int),
      new WinccoaDpTypeNode('text', WinccoaElementType.String),
      new WinccoaDpTypeNode('typeRef', WinccoaElementType.Typeref, 'ExampleDP_Float'),
      new WinccoaDpTypeNode('struct', WinccoaElementType.Struct, '', [
        new WinccoaDpTypeNode('id2', WinccoaElementType.Int),
        new WinccoaDpTypeNode('text2', WinccoaElementType.String)
      ])
    ]);
  console.log(await winccoa.dpTypeCreate(tree));
}
test1();
```

<a id="dptypedelete"></a>

##### dpTypeDelete()

> **dpTypeDelete**(`dpt`): `Promise`\<`boolean`\>

Deletes an existing data point type.

###### Parameters

###### dpt

`string`

Name of the data point type to delete.

###### Returns

`Promise`\<`boolean`\>

Promise - will be resolved to `true` if successful
         or rejected with [WinccoaError](#winccoaerror) in case of:
- invalid argument type is given
- __dpt__ does not exist

###### See

- [CTRL function `dpTypeDelete()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpTypeDelete.html)
- [dpTypeCreate](#dptypecreate)
- [dpTypeChange](#dptypechange)

###### Example

```ts
console.log(await winccoa.dpTypeDelete('MyType1'));
```

<a id="dptypeget"></a>

##### dpTypeGet()

> **dpTypeGet**(`dpt`, `includeSubTypes`): [`WinccoaDpTypeNode`](#winccoadptypenode)

Returns the structure of a data point type.

###### Parameters

###### dpt

`string`

Data point type.

###### includeSubTypes

`boolean` = `false`

true: subtypes will be passed

###### Returns

[`WinccoaDpTypeNode`](#winccoadptypenode)

Data point type structure as a tree of [WinccoaDpTypeNode](#winccoadptypenode)

###### Throws

[WinccoaError](#winccoaerror) in case of:
- an invalid argument type or
- __dpt__ does not exist

###### See

- [CTRL function `dpTypeGet()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpTypeGet.html)
- [WinccoaDpTypeNode](#winccoadptypenode)
- [WinccoaElementType](#winccoaelementtype)

###### Example

```ts
import { WinccoaDpTypeNode,  WinccoaElementType, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

console.log(winccoa.dpTypeGet('ExampleDP_Float'));
```

<a id="dptypename"></a>

##### dpTypeName()

> **dpTypeName**(`dp`): `string`

Returns the data point type for the data point name.

###### Parameters

###### dp

`string`

Name of the data point (for example, "ExampleDP_Trend1")

###### Returns

`string`

Data Point Type name

###### Throws

[WinccoaError](#winccoaerror) in case of:
- an invalid argument type or
- __dp__ does not exist

###### See

- [CTRL function `dpTypeName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpTypeName.html)

###### Example

```ts
console.log(winccoa.dpTypeName('ExampleDP_Trend1'));
```

<a id="dptyperefname"></a>

##### dpTypeRefName()

> **dpTypeRefName**(`dpe`): `string`

Returns the type reference of the selected DPE.

###### Parameters

###### dpe

`string`

Name of the data point element (for example, "_mp_PUMP1.state.mode")

###### Returns

`string`

Empty string or type reference as string.

###### Throws

[WinccoaError](#winccoaerror) in case of:
- an invalid argument type or
- __dpe__ does not exist

###### See

- [CTRL function `dpTypeRefName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/dpTypeRefName.html)

###### Example

```ts
console.log(winccoa.dpTypeRefName('_mp_PUMP1.state.mode')); // output MODE_STATE
```

#### Logging

<a id="logdebugf"></a>

##### logDebugF()

> **logDebugF**(`flag`, ...`args`): `void`

Writes a log entry if debug __flag__ is set.

> __Note__
>
> When setting a debug flag from the command line, the `-dbg` option
> must be positioned __before__ the name of the JavaScript file (as
> any other WinCC OA manager option).

###### Parameters

###### flag

Name or number of the debug flag that must be set to actually
            write the log entry.

`string` | `number`

###### args

...`unknown`[]

Debug information to be written to log.

###### Returns

`void`

###### See

- [isDbgFlag](#isdbgflag)

###### Example

```ts
const note = 'Additional note.';
winccoa.logDebugF('DebugFlag', 'Debug message', note);
```

<a id="logfatal"></a>

##### logFatal()

> **logFatal**(...`args`): `void`

Writes a fatal error log entry. This also exits the WinCC OA manager.

###### Parameters

###### args

...`unknown`[]

Fatal error information to be written to log.

###### Returns

`void`

###### Example

```ts
const note = 'Additional note.';
winccoa.logFatal('Fatal message', note);
```

<a id="loginfo"></a>

##### logInfo()

> **logInfo**(...`args`): `void`

Writes an information log entry. `console.log()` and `console.info()` are mapped
to this method.

###### Parameters

###### args

...`unknown`[]

Information to be written to log.

###### Returns

`void`

###### Example

```ts
const note = 'Additional note.';
winccoa.logInfo('Info message', note);
```

<a id="logsevere"></a>

##### logSevere()

> **logSevere**(...`args`): `void`

Writes a severe error log entry. `console.error()` is mapped to this method.

###### Parameters

###### args

...`unknown`[]

Severe error information to be written to log.

###### Returns

`void`

###### Example

```ts
const note = 'Additional note.';
winccoa.logSevere('Severe message', note);
```

<a id="logwarning"></a>

##### logWarning()

> **logWarning**(...`args`): `void`

Writes a warning log entry. `console.warn()` is mapped to this method.

###### Parameters

###### args

...`unknown`[]

Warning information to be written to log.

###### Returns

`void`

###### Example

```ts
const note = 'Additional note.';
winccoa.logWarning('Warning message', note);
```

<a id="securityevent"></a>

##### securityEvent()

> **securityEvent**(`id`, ...`args`): `void`

Reports a security event, this must be called whenever a security-relevant
action is made in JavaScript (like opening a server port).

###### Parameters

###### id

[`WinccoaSecurityEventId`](#winccoasecurityeventid)

ID of the security event.

###### args

...`unknown`[]

Arguments for the security event, depending on the value
            of id. See [WinccoaSecurityEventId](#winccoasecurityeventid) for details.

###### Returns

`void`

###### Throws

[WinccoaError](#winccoaerror) when id is not known, required arguments
        are missing in args.

###### See

[WinccoaSecurityEventId](#winccoasecurityeventid)

###### Example

```ts
import { WinccoaManager, WinccoaSecurityEventId } from 'winccoa-manager';
const winccoa = new WinccoaManager();

winccoa.securityEvent(WinccoaSecurityEventId.PortOpened, 8443, 'https://');
```

#### Manager

<a id="sysconnect"></a>

##### sysConnect

###### Get Signature

> **get** **sysConnect**(): [`WinccoaSysConnect`](#winccoasysconnect)

Gets access sysConnect updates, which uses the Node.js event emitter
mechanism to inform clients of various events. For details and examples
see [WinccoaSysConnect](#winccoasysconnect).

###### See

[WinccoaSysConnect](#winccoasysconnect)

###### Returns

[`WinccoaSysConnect`](#winccoasysconnect)

<a id="cfgreadcontent"></a>

##### cfgReadContent()

> **cfgReadContent**(`configName`, `level`): `object`

Returns the content of a given config for the installation or the project.

> __Note:__ For easier access to the data returned by this method, use the helper class
> [WinccoaConfig](#winccoaconfig).

###### Parameters

###### configName

`string` = `'config'`

The name of the config file which content will be retrieved (optional).
       By default the __config__ is used.

###### level

`number` = `WinccoaDirectoryLevel.Proj`

The directory level from which the config will be retrieved (optional). Can be specified as a number or
       as an enum [WinccoaDirectoryLevel](#winccoadirectorylevel). The default is the current project level.
> __Note:__ When a config file of a specific sub-project is needed, then the index of the sub-project can be specified.
> The index of a sub-project can be found using [getPaths](#getpaths).

###### Returns

`object`

Object where key is the section name of config and a value is an object which has content of a section.
         The object of each section contains config name as a key and config value as a value.
         In case the config file with the given name is not found then an empty object is returned.

###### See

- [WinccoaDirectoryLevel](#winccoadirectorylevel)
- [WinccoaConfig](#winccoaconfig)
- [getPaths](#getpaths)

###### Example

```ts
const configObj = winccoa.cfgReadContent('config');
Object.keys(configObj).forEach((key:string)=>{
   if (key == 'webClient')
     console.info('webClient httpsPort = ' + configObj[key as keyof typeof configObj]['httpsPort']);
 });
}
```

<a id="exit"></a>

##### exit()

> **exit**(`exitCode`): `void`

Exits the WinCC OA manager.

> __NOTE__
>
> For details about using an exit listener with WinCC OA, see the
> note in the documentation for [WinccoaSysConEvent](#winccoasysconevent).

###### Parameters

###### exitCode

`number` = `0`

Exit code to return to the operating system.

###### Returns

`void`

###### Example

```ts
winccoa.exit();
```

<a id="findfile"></a>

##### findFile()

> **findFile**(`fileDirName`): `string`

Search for file or directory in WinCC OA project and installation paths.

###### Parameters

###### fileDirName

`string`

the file or directory to search for

###### Returns

`string`

full path of the file or directory or an empty string if not found

###### Throws

[WinccoaError](#winccoaerror) when invalid argument type is given.

###### Example

```ts
let configPath;
try {
  configPath = winccoa.findFile('config/config');
} catch (exc) {
  console.error(exc);
}

console.info("Config file full path: " + configPath);
```

<a id="getoptions"></a>

##### getOptions()

> **getOptions**(): [`WinccoaOptions`](#winccoaoptions)

Returns all available options and their values.
The options can be set with [setOptions](#setoptions).

###### Returns

[`WinccoaOptions`](#winccoaoptions)

Object containing all current option values.

###### See

- [setOptions](#setoptions)
- [WinccoaOptions](#winccoaoptions)

###### Example

```ts
let options = winccoa.getOptions();
for (const [key, value] of Object.entries(options)) {
  console.info(`Name: ${key} - Value: ${value}`);
}
```

<a id="getpaths"></a>

##### getPaths()

> **getPaths**(): readonly `string`[]

Returns list of project, sub-project and product installation paths.

###### Returns

readonly `string`[]

List of project, sub-project and product installation paths.
The project path is always a first entry and the installation path is always the last.

###### Example

```ts
let paths = winccoa.getPaths();
for (let i = 0; i < paths.length; i++) {
  console.info(paths.at(i));
}
```

<a id="getprojectlangs"></a>

##### getProjectLangs()

> **getProjectLangs**(): `string`[]

Gets list of project language names.

###### Returns

`string`[]

List of project language names.
- Language names are in the same order as for a [WinccoaLangString](#winccoalangstring) with
  format [WinccoaLangStringFormat.Array](#array).
- Language names are the same as the keys of a [WinccoaLangString](#winccoalangstring) with
  format [WinccoaLangStringFormat.Object](#object).

###### Example

```ts
console.info(winccoa.getProjectLangs());
```

<a id="getsystemid"></a>

##### getSystemId()

> **getSystemId**(`systemName?`): `number`

Returns the system ID.

###### Parameters

###### systemName?

`string`

The name of the system (optional).
If it is not given, then the system ID of its own system will be returned.

###### Returns

`number`

The system ID.

###### Throws

[WinccoaError](#winccoaerror) when invalid system name is given.

###### See

- [getSystemName](#getsystemname)
- [CTRL function `getSystemId()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/getSystemId.html)

###### Example

```ts
let ownId;
let system1Id;
try {
  ownId = winccoa.getSystemId();
  system1Id = winccoa.getSystemId('System1:');
} catch (exc) {
  console.error(exc);
}

console.info("Own system id = " + ownId);
console.info("System1 id = " + system1Id);
```

<a id="getsystemname"></a>

##### getSystemName()

> **getSystemName**(`systemId?`): `string`

Returns the system name.

###### Parameters

###### systemId?

`number`

System ID (optional).
If it is not given, then the system name of its own system will be returned.

###### Returns

`string`

The system name.

###### Throws

[WinccoaError](#winccoaerror) when invalid system ID is given.

###### See

- [getSystemId](#getsystemid)
- [CTRL function `getSystemName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/getSystemName.html)

###### Example

```ts
try {
  const ownName = winccoa.getSystemName();
  const id1Name = winccoa.getSystemName(1);
  console.info(
    `Own system name = '${ownName}, system with id 1 name = '${id1Name}'`
  );
} catch (exc) {
  console.error(exc);
}
```

<a id="getuserid"></a>

##### getUserId()

> **getUserId**(`userName?`): `undefined` \| `number`

Gets the ID of the user with given __userName__ or currently used by this
instance (if no __userName__ is given).

###### Parameters

###### userName?

`string`

Name of the user for which the user name will be returned. If not given,
          the user ID currently used by this instance will be returned.

###### Returns

`undefined` \| `number`

User ID or `undefined` if no user exists with __userName__.

###### See

- [CTRL function `getUserId()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/getUserId.html)
- [getUserName](#getusername)

###### Example

```ts
console.info(winccoa.getUserName());
console.info(winccoa.getUserName(2048));
```

<a id="getusername"></a>

##### getUserName()

> **getUserName**(`id?`): `undefined` \| `string`

Gets the name of the user with given __id__ or currently used by this
instance (if no __id__ is given).

###### Parameters

###### id?

`number`

ID of the user for which the user name will be returned. If not given,
          the user name currently used by this instance will be returned.

###### Returns

`undefined` \| `string`

User name or `undefined` if no user exists with __id__.

###### See

- [CTRL function `getUserName()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/getUserName.html)
- [getUserId](#getuserid)

###### Example

```ts
console.info(winccoa.getUserId());
console.info(winccoa.getUserId('operatorAll'));
```

<a id="getversioninfo"></a>

##### getVersionInfo()

> **getVersionInfo**(): [`WinccoaVersionDetails`](#winccoaversiondetails)

Returns information about current API and WinCC OA versions.

###### Returns

[`WinccoaVersionDetails`](#winccoaversiondetails)

API and WinCC OA versions.

<a id="isdbgflag"></a>

##### isDbgFlag()

> **isDbgFlag**(`flag`): `boolean`

Queries the value of a debug flag.

###### Parameters

###### flag

Number or name of the debug flag to query.

`string` | `number`

###### Returns

`boolean`

`true` if debug flag is set, `false` if not set.

###### See

- [logDebugF](#logdebugf)
- [CTRL function `isDbgFlag()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/isDbgFlag.html)

###### Example

```ts
console.info(winccoa.isDbgFlag('REDU'));
```

<a id="setoptions"></a>

##### setOptions()

> **setOptions**(`options`): `boolean`

Set one or more options.
The options and their values can be retrieved with [getOptions](#getoptions).

###### Parameters

###### options

`Partial`\<`Omit`\<[`WinccoaOptions`](#winccoaoptions), `"userId"`\>\>

The options to be set (see [WinccoaOptions](#winccoaoptions) for possible options).

###### Returns

`boolean`

Boolean `true` on success, otherwise [WinccoaError](#winccoaerror) wil be thrown instead.

###### Remarks

The userId option cannot be set with this method.
<br>The user can be set with [setUserId](#setuserid) for the instance of `WinccoaManager`.
<br>The user can be set with `-user` manager option for the node manager,
see [Administration of managers](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Pmon_Consolepanel/Pmon_Consolepanel-23.html).

###### Throws

[WinccoaError](#winccoaerror) if option has wrong type or option value is out of range.

###### See

- [getOptions](#getoptions)
- [WinccoaOptions](#winccoaoptions)
- [setUserId](#setuserid)
- [Administration of managers](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Pmon_Consolepanel/Pmon_Consolepanel-23.html)

###### Example

```ts
import { WinccoaManager, WinccoaLangStringFormat } from 'winccoa-manager';
const winccoa = new WinccoaManager();

function setOptionsTest() {
  try {
    winccoa.setOptions({
      langStringFormat: WinccoaLangStringFormat.StringFixed,
      langIdx: 1,
    });
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="setuserid"></a>

##### setUserId()

> **setUserId**(`id`, `password?`): `boolean`

Sets the current user ID to the specified value for the current instance of [WinccoaManager](#winccoamanager).

> Note that when
> [Server-side Authentication for Managers](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/Authentication/Serverside_auth_managers/topics/serversideauthman_basics.html)
> is activated and the JavaScript manager is not started as `root`, trying to change the user ID will lead
> to a __fatal error__ and the JavaScript manager will be terminated immediately.

###### Parameters

###### id

`number`

User ID to set.

###### password?

`string`

Password to use to set user (not needed if manager started as `root`).

###### Returns

`boolean`

Boolean `true` in case of a success, otherwise [WinccoaError](#winccoaerror) wil be thrown instead.

###### Throws

[WinccoaError](#winccoaerror) when __id__ is not found or invalid.

###### See

- [CTRL function `setUserId()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlS_Z/setUserId.html)

###### Example

```ts
let isSuccess = false;
try {
  isSuccess = winccoa.setUserId(2048);  // operatorAll user id
} catch (exc) {
  console.error(exc);
}

console.info('User id is set to operatorAll user id successfully - ' + isSuccess);
```

#### Redundancy

<a id="isreduactive"></a>

##### isReduActive()

> **isReduActive**(): `boolean`

Checks if the event manager to which this manager is connected is currently
the active REDU partner.

###### Returns

`boolean`

`true` if the event manager to which this manager is connected is
         currently the active REDU partner.

###### See

- [CTRL function `isReduActive()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/isReduActive.html)

###### Example

```ts
const isEventReduActive = winccoa.isReduActive();
console.info('Event currently is active - ' + isEventReduActive);
```

<a id="isredundant"></a>

##### isRedundant()

> **isRedundant**(): `boolean`

Checks whether the project has been configured as redundant.

###### Returns

`boolean`

`true` if project has been configured as redundant.

###### See

- [CTRL function `isRedundant()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/isRedundant.html)

###### Example

```ts
const isProjectRedundant = winccoa.isRedundant();
console.info('My project is redundant - ' + isProjectRedundant);
```

<a id="myreduhost"></a>

##### myReduHost()

> **myReduHost**(): `string`

Returns the host name of the Event Manager this manager is connected to. Use this method only on redundant computers.

###### Returns

`string`

Host name of the Event Manager this manager is connected to.

###### See

- [CTRL function `myReduHost()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/myReduHost.html)

###### Example

```ts
const reduHostName = winccoa.myReduHost();
console.info('My redu host name - ' + reduHostName);
```

<a id="myreduhostnum"></a>

##### myReduHostNum()

> **myReduHostNum**(): `number`

Returns host number in a redundant system depending on the connection to the Event Manager - manager 1 or 2 (for example, eventHost = "host1$host2").
In a non-redundant configuration this always returns 1.

###### Returns

`number`

Host number.

###### See

- [CTRL function `myReduHostNum()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/myReduHostNum.html)

###### Example

```ts
const reduHostNumber = winccoa.myReduHostNum();
console.info('My redu host number - ' + reduHostNumber);
```

***

<a id="winccoasysconnect"></a>

### WinccoaSysConnect

Class that provides access to system events. It can be accessed with
[WinccoaManager.sysConnect](#sysconnect) and uses the Node.js event emitter
mechanism to inform clients of various global system events.

Clients can connect using the method `on()` and specifying the
event name and a listener function that will be called whenever the
event occurs. The enumerator [WinccoaSysConEvent](#winccoasysconevent) enumerates all
events for which a listener can be registered.

To disconnect, the  method `off()` togther with the event name can be used.

#### See

 - [WinccoaSysConEvent](#winccoasysconevent)
 - [WinccoaManager.sysConnect](#sysconnect)
 - [Node.js event emitter](https://nodejs.org/en/learn/asynchronous-work/the-nodejs-event-emitter)
 - [CTRL function `sysConnect()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlS_Z/sysConnect.html?hl=sysconnect)

#### Example

```ts
import {
  WinccoaManager,
  WinccoaSysConEvent,
  WinccoaSysConDpDetails
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function dpCreatedListener(details: WinccoaSysConDpDetails) {
  console.log('DP created - details:');
  console.log(details);
}

async function dpCreate() {
  winccoa.sysConnect.on(WinccoaSysConEvent.DpCreated, dpCreatedListener);

  // create data points
  ...

  winccoa.sysConnect.off(WinccoaSysConEvent.DpCreated, dpCreatedListener);
}
```

#### Extends

- `EventEmitter`

#### Properties

<a id="capturerejections"></a>

##### captureRejections

> `static` **captureRejections**: `boolean`

Value: [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type)

Change the default `captureRejections` option on all new `EventEmitter` objects.

###### Since

v13.4.0, v12.16.0

###### Inherited from

`EventEmitter.captureRejections`

<a id="capturerejectionsymbol"></a>

##### captureRejectionSymbol

> `readonly` `static` **captureRejectionSymbol**: *typeof* [`captureRejectionSymbol`](#capturerejectionsymbol)

Value: `Symbol.for('nodejs.rejection')`

See how to write a custom `rejection handler`.

###### Since

v13.4.0, v12.16.0

###### Inherited from

`EventEmitter.captureRejectionSymbol`

<a id="defaultmaxlisteners"></a>

##### defaultMaxListeners

> `static` **defaultMaxListeners**: `number`

By default, a maximum of `10` listeners can be registered for any single
event. This limit can be changed for individual `EventEmitter` instances
using the `emitter.setMaxListeners(n)` method. To change the default
for _all_`EventEmitter` instances, the `events.defaultMaxListeners` property
can be used. If this value is not a positive number, a `RangeError` is thrown.

Take caution when setting the `events.defaultMaxListeners` because the
change affects _all_ `EventEmitter` instances, including those created before
the change is made. However, calling `emitter.setMaxListeners(n)` still has
precedence over `events.defaultMaxListeners`.

This is not a hard limit. The `EventEmitter` instance will allow
more listeners to be added but will output a trace warning to stderr indicating
that a "possible EventEmitter memory leak" has been detected. For any single
`EventEmitter`, the `emitter.getMaxListeners()` and `emitter.setMaxListeners()` methods can be used to
temporarily avoid this warning:

```js
import { EventEmitter } from 'node:events';
const emitter = new EventEmitter();
emitter.setMaxListeners(emitter.getMaxListeners() + 1);
emitter.once('event', () => {
  // do stuff
  emitter.setMaxListeners(Math.max(emitter.getMaxListeners() - 1, 0));
});
```

The `--trace-warnings` command-line flag can be used to display the
stack trace for such warnings.

The emitted warning can be inspected with `process.on('warning')` and will
have the additional `emitter`, `type`, and `count` properties, referring to
the event emitter instance, the event's name and the number of attached
listeners, respectively.
Its `name` property is set to `'MaxListenersExceededWarning'`.

###### Since

v0.11.2

###### Inherited from

`EventEmitter.defaultMaxListeners`

<a id="errormonitor"></a>

##### errorMonitor

> `readonly` `static` **errorMonitor**: *typeof* [`errorMonitor`](#errormonitor)

This symbol shall be used to install a listener for only monitoring `'error'` events. Listeners installed using this symbol are called before the regular `'error'` listeners are called.

Installing a listener using this symbol does not change the behavior once an `'error'` event is emitted. Therefore, the process will still crash if no
regular `'error'` listener is installed.

###### Since

v13.6.0, v12.17.0

###### Inherited from

`EventEmitter.errorMonitor`

#### Methods

<a id="capturerejectionsymbol-1"></a>

##### \[captureRejectionSymbol\]()?

> `optional` **\[captureRejectionSymbol\]**\<`K`\>(`error`, `event`, ...`args`): `void`

###### Type Parameters

###### K

`K`

###### Parameters

###### error

`Error`

###### event

`string` | `symbol`

###### args

...`AnyRest`

###### Returns

`void`

###### Inherited from

`EventEmitter.[captureRejectionSymbol]`

<a id="addlistener"></a>

##### addListener()

> **addListener**\<`K`\>(`eventName`, `listener`): `this`

Alias for `emitter.on(eventName, listener)`.

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

`string` | `symbol`

###### listener

(...`args`) => `void`

###### Returns

`this`

###### Since

v0.1.26

###### Inherited from

`EventEmitter.addListener`

<a id="emit"></a>

##### emit()

> **emit**\<`K`\>(`eventName`, ...`args`): `boolean`

Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments
to each.

Returns `true` if the event had listeners, `false` otherwise.

```js
import { EventEmitter } from 'node:events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

console.log(myEmitter.listeners('event'));

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// [
//   [Function: firstListener],
//   [Function: secondListener],
//   [Function: thirdListener]
// ]
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
```

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

`string` | `symbol`

###### args

...`AnyRest`

###### Returns

`boolean`

###### Since

v0.1.26

###### Inherited from

`EventEmitter.emit`

<a id="eventnames"></a>

##### eventNames()

> **eventNames**(): (`string` \| `symbol`)[]

Returns an array listing the events for which the emitter has registered
listeners. The values in the array are strings or `Symbol`s.

```js
import { EventEmitter } from 'node:events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
```

###### Returns

(`string` \| `symbol`)[]

###### Since

v6.0.0

###### Inherited from

`EventEmitter.eventNames`

<a id="getmaxlisteners"></a>

##### getMaxListeners()

> **getMaxListeners**(): `number`

Returns the current max listener value for the `EventEmitter` which is either
set by `emitter.setMaxListeners(n)` or defaults to [EventEmitter.defaultMaxListeners](#defaultmaxlisteners).

###### Returns

`number`

###### Since

v1.0.0

###### Inherited from

`EventEmitter.getMaxListeners`

<a id="listenercount"></a>

##### listenerCount()

> **listenerCount**\<`K`\>(`eventName`, `listener?`): `number`

Returns the number of listeners listening for the event named `eventName`.
If `listener` is provided, it will return how many times the listener is found
in the list of the listeners of the event.

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

The name of the event being listened for

`string` | `symbol`

###### listener?

`Function`

The event handler function

###### Returns

`number`

###### Since

v3.2.0

###### Inherited from

`EventEmitter.listenerCount`

<a id="listeners"></a>

##### listeners()

> **listeners**\<`K`\>(`eventName`): `Function`[]

Returns a copy of the array of listeners for the event named `eventName`.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
console.log(util.inspect(server.listeners('connection')));
// Prints: [ [Function] ]
```

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

`string` | `symbol`

###### Returns

`Function`[]

###### Since

v0.1.26

###### Inherited from

`EventEmitter.listeners`

<a id="off"></a>

##### off()

> **off**\<`K`\>(`eventName`, `listener`): `this`

Alias for `emitter.removeListener()`.

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

`string` | `symbol`

###### listener

(...`args`) => `void`

###### Returns

`this`

###### Since

v10.0.0

###### Inherited from

`EventEmitter.off`

<a id="on"></a>

##### on()

> **on**\<`K`\>(`eventName`, `listener`): `this`

Adds the `listener` function to the end of the listeners array for the event
named `eventName`. No checks are made to see if the `listener` has already
been added. Multiple calls passing the same combination of `eventName` and
`listener` will result in the `listener` being added, and called, multiple times.

```js
server.on('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'node:events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

The name of the event.

`string` | `symbol`

###### listener

(...`args`) => `void`

The callback function

###### Returns

`this`

###### Since

v0.1.101

###### Inherited from

`EventEmitter.on`

<a id="once"></a>

##### once()

> **once**\<`K`\>(`eventName`, `listener`): `this`

Adds a **one-time** `listener` function for the event named `eventName`. The
next time `eventName` is triggered, this listener is removed and then invoked.

```js
server.once('connection', (stream) => {
  console.log('Ah, we have our first user!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the
event listener to the beginning of the listeners array.

```js
import { EventEmitter } from 'node:events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
```

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

The name of the event.

`string` | `symbol`

###### listener

(...`args`) => `void`

The callback function

###### Returns

`this`

###### Since

v0.3.0

###### Inherited from

`EventEmitter.once`

<a id="prependlistener"></a>

##### prependListener()

> **prependListener**\<`K`\>(`eventName`, `listener`): `this`

Adds the `listener` function to the _beginning_ of the listeners array for the
event named `eventName`. No checks are made to see if the `listener` has
already been added. Multiple calls passing the same combination of `eventName`
and `listener` will result in the `listener` being added, and called, multiple times.

```js
server.prependListener('connection', (stream) => {
  console.log('someone connected!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

The name of the event.

`string` | `symbol`

###### listener

(...`args`) => `void`

The callback function

###### Returns

`this`

###### Since

v6.0.0

###### Inherited from

`EventEmitter.prependListener`

<a id="prependoncelistener"></a>

##### prependOnceListener()

> **prependOnceListener**\<`K`\>(`eventName`, `listener`): `this`

Adds a **one-time**`listener` function for the event named `eventName` to the _beginning_ of the listeners array. The next time `eventName` is triggered, this
listener is removed, and then invoked.

```js
server.prependOnceListener('connection', (stream) => {
  console.log('Ah, we have our first user!');
});
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

The name of the event.

`string` | `symbol`

###### listener

(...`args`) => `void`

The callback function

###### Returns

`this`

###### Since

v6.0.0

###### Inherited from

`EventEmitter.prependOnceListener`

<a id="rawlisteners"></a>

##### rawListeners()

> **rawListeners**\<`K`\>(`eventName`): `Function`[]

Returns a copy of the array of listeners for the event named `eventName`,
including any wrappers (such as those created by `.once()`).

```js
import { EventEmitter } from 'node:events';
const emitter = new EventEmitter();
emitter.once('log', () => console.log('log once'));

// Returns a new Array with a function `onceWrapper` which has a property
// `listener` which contains the original listener bound above
const listeners = emitter.rawListeners('log');
const logFnWrapper = listeners[0];

// Logs "log once" to the console and does not unbind the `once` event
logFnWrapper.listener();

// Logs "log once" to the console and removes the listener
logFnWrapper();

emitter.on('log', () => console.log('log persistently'));
// Will return a new Array with a single function bound by `.on()` above
const newListeners = emitter.rawListeners('log');

// Logs "log persistently" twice
newListeners[0]();
emitter.emit('log');
```

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

`string` | `symbol`

###### Returns

`Function`[]

###### Since

v9.4.0

###### Inherited from

`EventEmitter.rawListeners`

<a id="removealllisteners"></a>

##### removeAllListeners()

> **removeAllListeners**(`eventName?`): `this`

Removes all listeners, or those of the specified `eventName`.

It is bad practice to remove listeners added elsewhere in the code,
particularly when the `EventEmitter` instance was created by some other
component or module (e.g. sockets or file streams).

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

###### eventName?

`string` | `symbol`

###### Returns

`this`

###### Since

v0.1.26

###### Inherited from

`EventEmitter.removeAllListeners`

<a id="removelistener"></a>

##### removeListener()

> **removeListener**\<`K`\>(`eventName`, `listener`): `this`

Removes the specified `listener` from the listener array for the event named `eventName`.

```js
const callback = (stream) => {
  console.log('someone connected!');
};
server.on('connection', callback);
// ...
server.removeListener('connection', callback);
```

`removeListener()` will remove, at most, one instance of a listener from the
listener array. If any single listener has been added multiple times to the
listener array for the specified `eventName`, then `removeListener()` must be
called multiple times to remove each instance.

Once an event is emitted, all listeners attached to it at the
time of emitting are called in order. This implies that any `removeListener()` or `removeAllListeners()` calls _after_ emitting and _before_ the last listener finishes execution
will not remove them from`emit()` in progress. Subsequent events behave as expected.

```js
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
```

Because listeners are managed using an internal array, calling this will
change the position indices of any listener registered _after_ the listener
being removed. This will not impact the order in which listeners are called,
but it means that any copies of the listener array as returned by
the `emitter.listeners()` method will need to be recreated.

When a single function has been added as a handler multiple times for a single
event (as in the example below), `removeListener()` will remove the most
recently added instance. In the example the `once('ping')` listener is removed:

```js
import { EventEmitter } from 'node:events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Type Parameters

###### K

`K`

###### Parameters

###### eventName

`string` | `symbol`

###### listener

(...`args`) => `void`

###### Returns

`this`

###### Since

v0.1.26

###### Inherited from

`EventEmitter.removeListener`

<a id="setmaxlisteners"></a>

##### setMaxListeners()

> **setMaxListeners**(`n`): `this`

By default `EventEmitter`s will print a warning if more than `10` listeners are
added for a particular event. This is a useful default that helps finding
memory leaks. The `emitter.setMaxListeners()` method allows the limit to be
modified for this specific `EventEmitter` instance. The value can be set to `Infinity` (or `0`) to indicate an unlimited number of listeners.

Returns a reference to the `EventEmitter`, so that calls can be chained.

###### Parameters

###### n

`number`

###### Returns

`this`

###### Since

v0.3.5

###### Inherited from

`EventEmitter.setMaxListeners`

<a id="addabortlistener"></a>

##### addAbortListener()

> `static` **addAbortListener**(`signal`, `resource`): `Disposable`

**`Experimental`**

Listens once to the `abort` event on the provided `signal`.

Listening to the `abort` event on abort signals is unsafe and may
lead to resource leaks since another third party with the signal can
call `e.stopImmediatePropagation()`. Unfortunately Node.js cannot change
this since it would violate the web standard. Additionally, the original
API makes it easy to forget to remove listeners.

This API allows safely using `AbortSignal`s in Node.js APIs by solving these
two issues by listening to the event such that `stopImmediatePropagation` does
not prevent the listener from running.

Returns a disposable so that it may be unsubscribed from more easily.

```js
import { addAbortListener } from 'node:events';

function example(signal) {
  let disposable;
  try {
    signal.addEventListener('abort', (e) => e.stopImmediatePropagation());
    disposable = addAbortListener(signal, (e) => {
      // Do something when signal is aborted.
    });
  } finally {
    disposable?.[Symbol.dispose]();
  }
}
```

###### Parameters

###### signal

`AbortSignal`

###### resource

(`event`) => `void`

###### Returns

`Disposable`

Disposable that removes the `abort` listener.

###### Since

v20.5.0

###### Inherited from

`EventEmitter.addAbortListener`

<a id="geteventlisteners"></a>

##### getEventListeners()

> `static` **getEventListeners**(`emitter`, `name`): `Function`[]

Returns a copy of the array of listeners for the event named `eventName`.

For `EventEmitter`s this behaves exactly the same as calling `.listeners` on
the emitter.

For `EventTarget`s this is the only way to get the event listeners for the
event target. This is useful for debugging and diagnostic purposes.

```js
import { getEventListeners, EventEmitter } from 'node:events';

{
  const ee = new EventEmitter();
  const listener = () => console.log('Events are fun');
  ee.on('foo', listener);
  console.log(getEventListeners(ee, 'foo')); // [ [Function: listener] ]
}
{
  const et = new EventTarget();
  const listener = () => console.log('Events are fun');
  et.addEventListener('foo', listener);
  console.log(getEventListeners(et, 'foo')); // [ [Function: listener] ]
}
```

###### Parameters

###### emitter

`EventTarget` | `EventEmitter`\<`DefaultEventMap`\>

###### name

`string` | `symbol`

###### Returns

`Function`[]

###### Since

v15.2.0, v14.17.0

###### Inherited from

`EventEmitter.getEventListeners`

<a id="getmaxlisteners-2"></a>

##### getMaxListeners()

> `static` **getMaxListeners**(`emitter`): `number`

Returns the currently set max amount of listeners.

For `EventEmitter`s this behaves exactly the same as calling `.getMaxListeners` on
the emitter.

For `EventTarget`s this is the only way to get the max event listeners for the
event target. If the number of event handlers on a single EventTarget exceeds
the max set, the EventTarget will print a warning.

```js
import { getMaxListeners, setMaxListeners, EventEmitter } from 'node:events';

{
  const ee = new EventEmitter();
  console.log(getMaxListeners(ee)); // 10
  setMaxListeners(11, ee);
  console.log(getMaxListeners(ee)); // 11
}
{
  const et = new EventTarget();
  console.log(getMaxListeners(et)); // 10
  setMaxListeners(11, et);
  console.log(getMaxListeners(et)); // 11
}
```

###### Parameters

###### emitter

`EventTarget` | `EventEmitter`\<`DefaultEventMap`\>

###### Returns

`number`

###### Since

v19.9.0

###### Inherited from

`EventEmitter.getMaxListeners`

<a id="listenercount-2"></a>

##### ~~listenerCount()~~

> `static` **listenerCount**(`emitter`, `eventName`): `number`

A class method that returns the number of listeners for the given `eventName` registered on the given `emitter`.

```js
import { EventEmitter, listenerCount } from 'node:events';

const myEmitter = new EventEmitter();
myEmitter.on('event', () => {});
myEmitter.on('event', () => {});
console.log(listenerCount(myEmitter, 'event'));
// Prints: 2
```

###### Parameters

###### emitter

`EventEmitter`

The emitter to query

###### eventName

The event name

`string` | `symbol`

###### Returns

`number`

###### Since

v0.9.12

###### Deprecated

Since v3.2.0 - Use `listenerCount` instead.

###### Inherited from

`EventEmitter.listenerCount`

<a id="on-2"></a>

##### on()

###### Call Signature

> `static` **on**(`emitter`, `eventName`, `options?`): `AsyncIterator`\<`any`[]\>

```js
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

// Emit later on
process.nextTick(() => {
  ee.emit('foo', 'bar');
  ee.emit('foo', 42);
});

for await (const event of on(ee, 'foo')) {
  // The execution of this inner block is synchronous and it
  // processes one event at a time (even with await). Do not use
  // if concurrent execution is required.
  console.log(event); // prints ['bar'] [42]
}
// Unreachable here
```

Returns an `AsyncIterator` that iterates `eventName` events. It will throw
if the `EventEmitter` emits `'error'`. It removes all listeners when
exiting the loop. The `value` returned by each iteration is an array
composed of the emitted event arguments.

An `AbortSignal` can be used to cancel waiting on events:

```js
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ac = new AbortController();

(async () => {
  const ee = new EventEmitter();

  // Emit later on
  process.nextTick(() => {
    ee.emit('foo', 'bar');
    ee.emit('foo', 42);
  });

  for await (const event of on(ee, 'foo', { signal: ac.signal })) {
    // The execution of this inner block is synchronous and it
    // processes one event at a time (even with await). Do not use
    // if concurrent execution is required.
    console.log(event); // prints ['bar'] [42]
  }
  // Unreachable here
})();

process.nextTick(() => ac.abort());
```

Use the `close` option to specify an array of event names that will end the iteration:

```js
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

// Emit later on
process.nextTick(() => {
  ee.emit('foo', 'bar');
  ee.emit('foo', 42);
  ee.emit('close');
});

for await (const event of on(ee, 'foo', { close: ['close'] })) {
  console.log(event); // prints ['bar'] [42]
}
// the loop will exit after 'close' is emitted
console.log('done'); // prints 'done'
```

###### Parameters

###### emitter

`EventEmitter`

###### eventName

`string` | `symbol`

###### options?

`StaticEventEmitterIteratorOptions`

###### Returns

`AsyncIterator`\<`any`[]\>

An `AsyncIterator` that iterates `eventName` events emitted by the `emitter`

###### Since

v13.6.0, v12.16.0

###### Inherited from

`EventEmitter.on`

###### Call Signature

> `static` **on**(`emitter`, `eventName`, `options?`): `AsyncIterator`\<`any`[]\>

```js
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

// Emit later on
process.nextTick(() => {
  ee.emit('foo', 'bar');
  ee.emit('foo', 42);
});

for await (const event of on(ee, 'foo')) {
  // The execution of this inner block is synchronous and it
  // processes one event at a time (even with await). Do not use
  // if concurrent execution is required.
  console.log(event); // prints ['bar'] [42]
}
// Unreachable here
```

Returns an `AsyncIterator` that iterates `eventName` events. It will throw
if the `EventEmitter` emits `'error'`. It removes all listeners when
exiting the loop. The `value` returned by each iteration is an array
composed of the emitted event arguments.

An `AbortSignal` can be used to cancel waiting on events:

```js
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ac = new AbortController();

(async () => {
  const ee = new EventEmitter();

  // Emit later on
  process.nextTick(() => {
    ee.emit('foo', 'bar');
    ee.emit('foo', 42);
  });

  for await (const event of on(ee, 'foo', { signal: ac.signal })) {
    // The execution of this inner block is synchronous and it
    // processes one event at a time (even with await). Do not use
    // if concurrent execution is required.
    console.log(event); // prints ['bar'] [42]
  }
  // Unreachable here
})();

process.nextTick(() => ac.abort());
```

Use the `close` option to specify an array of event names that will end the iteration:

```js
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

// Emit later on
process.nextTick(() => {
  ee.emit('foo', 'bar');
  ee.emit('foo', 42);
  ee.emit('close');
});

for await (const event of on(ee, 'foo', { close: ['close'] })) {
  console.log(event); // prints ['bar'] [42]
}
// the loop will exit after 'close' is emitted
console.log('done'); // prints 'done'
```

###### Parameters

###### emitter

`EventTarget`

###### eventName

`string`

###### options?

`StaticEventEmitterIteratorOptions`

###### Returns

`AsyncIterator`\<`any`[]\>

An `AsyncIterator` that iterates `eventName` events emitted by the `emitter`

###### Since

v13.6.0, v12.16.0

###### Inherited from

`EventEmitter.on`

<a id="once-2"></a>

##### once()

###### Call Signature

> `static` **once**(`emitter`, `eventName`, `options?`): `Promise`\<`any`[]\>

Creates a `Promise` that is fulfilled when the `EventEmitter` emits the given
event or that is rejected if the `EventEmitter` emits `'error'` while waiting.
The `Promise` will resolve with an array of all the arguments emitted to the
given event.

This method is intentionally generic and works with the web platform [EventTarget](https://dom.spec.whatwg.org/#interface-eventtarget) interface, which has no special`'error'` event
semantics and does not listen to the `'error'` event.

```js
import { once, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

process.nextTick(() => {
  ee.emit('myevent', 42);
});

const [value] = await once(ee, 'myevent');
console.log(value);

const err = new Error('kaboom');
process.nextTick(() => {
  ee.emit('error', err);
});

try {
  await once(ee, 'myevent');
} catch (err) {
  console.error('error happened', err);
}
```

The special handling of the `'error'` event is only used when `events.once()` is used to wait for another event. If `events.once()` is used to wait for the
'`error'` event itself, then it is treated as any other kind of event without
special handling:

```js
import { EventEmitter, once } from 'node:events';

const ee = new EventEmitter();

once(ee, 'error')
  .then(([err]) => console.log('ok', err.message))
  .catch((err) => console.error('error', err.message));

ee.emit('error', new Error('boom'));

// Prints: ok boom
```

An `AbortSignal` can be used to cancel waiting for the event:

```js
import { EventEmitter, once } from 'node:events';

const ee = new EventEmitter();
const ac = new AbortController();

async function foo(emitter, event, signal) {
  try {
    await once(emitter, event, { signal });
    console.log('event emitted!');
  } catch (error) {
    if (error.name === 'AbortError') {
      console.error('Waiting for the event was canceled!');
    } else {
      console.error('There was an error', error.message);
    }
  }
}

foo(ee, 'foo', ac.signal);
ac.abort(); // Abort waiting for the event
ee.emit('foo'); // Prints: Waiting for the event was canceled!
```

###### Parameters

###### emitter

`EventEmitter`

###### eventName

`string` | `symbol`

###### options?

`StaticEventEmitterOptions`

###### Returns

`Promise`\<`any`[]\>

###### Since

v11.13.0, v10.16.0

###### Inherited from

`EventEmitter.once`

###### Call Signature

> `static` **once**(`emitter`, `eventName`, `options?`): `Promise`\<`any`[]\>

Creates a `Promise` that is fulfilled when the `EventEmitter` emits the given
event or that is rejected if the `EventEmitter` emits `'error'` while waiting.
The `Promise` will resolve with an array of all the arguments emitted to the
given event.

This method is intentionally generic and works with the web platform [EventTarget](https://dom.spec.whatwg.org/#interface-eventtarget) interface, which has no special`'error'` event
semantics and does not listen to the `'error'` event.

```js
import { once, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

process.nextTick(() => {
  ee.emit('myevent', 42);
});

const [value] = await once(ee, 'myevent');
console.log(value);

const err = new Error('kaboom');
process.nextTick(() => {
  ee.emit('error', err);
});

try {
  await once(ee, 'myevent');
} catch (err) {
  console.error('error happened', err);
}
```

The special handling of the `'error'` event is only used when `events.once()` is used to wait for another event. If `events.once()` is used to wait for the
'`error'` event itself, then it is treated as any other kind of event without
special handling:

```js
import { EventEmitter, once } from 'node:events';

const ee = new EventEmitter();

once(ee, 'error')
  .then(([err]) => console.log('ok', err.message))
  .catch((err) => console.error('error', err.message));

ee.emit('error', new Error('boom'));

// Prints: ok boom
```

An `AbortSignal` can be used to cancel waiting for the event:

```js
import { EventEmitter, once } from 'node:events';

const ee = new EventEmitter();
const ac = new AbortController();

async function foo(emitter, event, signal) {
  try {
    await once(emitter, event, { signal });
    console.log('event emitted!');
  } catch (error) {
    if (error.name === 'AbortError') {
      console.error('Waiting for the event was canceled!');
    } else {
      console.error('There was an error', error.message);
    }
  }
}

foo(ee, 'foo', ac.signal);
ac.abort(); // Abort waiting for the event
ee.emit('foo'); // Prints: Waiting for the event was canceled!
```

###### Parameters

###### emitter

`EventTarget`

###### eventName

`string`

###### options?

`StaticEventEmitterOptions`

###### Returns

`Promise`\<`any`[]\>

###### Since

v11.13.0, v10.16.0

###### Inherited from

`EventEmitter.once`

<a id="setmaxlisteners-2"></a>

##### setMaxListeners()

> `static` **setMaxListeners**(`n?`, ...`eventTargets?`): `void`

```js
import { setMaxListeners, EventEmitter } from 'node:events';

const target = new EventTarget();
const emitter = new EventEmitter();

setMaxListeners(5, target, emitter);
```

###### Parameters

###### n?

`number`

A non-negative number. The maximum number of listeners per `EventTarget` event.

###### eventTargets?

...(`EventTarget` \| `EventEmitter`\<`DefaultEventMap`\>)[]

Zero or more {EventTarget} or {EventEmitter} instances. If none are specified, `n` is set as the default max for all newly created {EventTarget} and {EventEmitter}
objects.

###### Returns

`void`

###### Since

v15.4.0

###### Inherited from

`EventEmitter.setMaxListeners`

## Interfaces

<a id="winccoaoptions"></a>

### WinccoaOptions

#### Properties

<a id="langidx"></a>

##### langIdx

> **langIdx**: `number`

Property that applies only when [langStringFormat](#langstringformat) is `StringFixed`.
It holds the index of the project language to return for LangStrings.
Language index starts with 0 and default is `0`.

###### See

- [WinccoaManager.getOptions](#getoptions)
- [WinccoaManager.setOptions](#setoptions)
- [langStringFormat](#langstringformat)
- [WinccoaLangStringFormat](#winccoalangstringformat)

###### Example

```ts
import { WinccoaManager, WinccoaLangStringFormat } from 'winccoa-manager';
const winccoa = new WinccoaManager();

let isSuccess = false;
try {
  isSuccess = winccoa.setOptions({
    langStringFormat: WinccoaLangStringFormat.StringFixed,
    langIdx: 1
  });
} catch (exc) {
  console.error(exc);
}

if (isSuccess){
  try {
    let description = winccoa.dpGetDescription('ExampleDP_Rpt1.');
    console.info('DP description for 2nd project language: ' + description);
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="langstringformat"></a>

##### langStringFormat

> **langStringFormat**: [`WinccoaLangStringFormat`](#winccoalangstringformat)

Property which defines in which format a [WinccoaLangString](#winccoalangstring) will be
returned from the API. Default is `StringActiveLanguage`.

###### See

- [WinccoaManager.getOptions](#getoptions)
- [WinccoaManager.setOptions](#setoptions)
- [WinccoaLangStringFormat](#winccoalangstringformat)

###### Example

```ts
let isSuccess = false;
try {
  isSuccess = winccoa.setOptions({
    langStringFormat: WinccoaLangStringFormat.StringActiveLanguage,
   });
} catch (exc) {
  console.error(exc);
}

if (isSuccess){
  try {
    let description = winccoa.dpGetDescription('ExampleDP_Rpt1.');
    console.info('DP description for active lang only: ' + description);
  } catch (exc) {
    console.error(exc);
  }
}
```

<a id="langtextformat"></a>

##### ~~langTextFormat?~~

> `optional` **langTextFormat**: [`WinccoaLangTextFormat`](#winccoalangtextformat)

###### Deprecated

Use [langStringFormat](#langstringformat) instead.

<a id="longasbigint"></a>

##### longAsBigInt

> **longAsBigInt**: `boolean`

Property that indicates whether `long` and `unsigned` long Variables should be `
returned as `BigInt` or `number.
Default is `false`.

###### See

- [WinccoaManager.getOptions](#getoptions)
- [WinccoaManager.setOptions](#setoptions)

<a id="splittimeout"></a>

##### splitTimeout

> **splitTimeout**: `number`

Property which indicates how long to keep a long-running
split requests like [WinccoaManager.dpQuerySplit](#dpquerysplit)
active before cancelling it in milliseconds.
Default is `60000` (= 1 minute).

###### See

- [WinccoaManager.dpQuerySplit](#dpquerysplit)
- [WinccoaManager.getOptions](#getoptions)
- [WinccoaManager.setOptions](#setoptions)

<a id="timeformat"></a>

##### timeFormat

> **timeFormat**: [`WinccoaTimeFormat`](#winccoatimeformat)

Property that defines how a [WinccoaTime](#winccoatime) will be returned from the API.
Default is `Date`.

###### See

- [WinccoaManager.getOptions](#getoptions)
- [WinccoaManager.setOptions](#setoptions)
- [WinccoaTimeFormat](#winccoatimeformat)

<a id="userid-1"></a>

##### userId

> `readonly` **userId**: `number`

Read only property of the __userId__ with which the manager was started.

###### See

- [WinccoaManager.setUserId](#setuserid)
- [WinccoaManager.getOptions](#getoptions)

## Type Aliases

<a id="winccoacnsobservercallback"></a>

### WinccoaCnsObserverCallback()

> **WinccoaCnsObserverCallback** = (`cnsPath`, `changeType`, `action`) => `void` \| `Promise`\<`void`\>

Type of callbacks registered with [WinccoaManager.cnsAddObserver](#cnsaddobserver).

#### Parameters

##### cnsPath

`string`

Path of the CNS node where a change happend.

##### changeType

[`WinccoaCnsChangeType`](#winccoacnschangetype)

Type of the change that happened.

##### action

[`WinccoaCnsAction`](#winccoacnsaction)

Action that was executed on the node.

#### Returns

`void` \| `Promise`\<`void`\>

#### See

- [WinccoaManager.cnsAddObserver](#cnsaddobserver)
- [WinccoaCnsChangeType](#winccoacnschangetype)
- [WinccoaCnsAction](#winccoacnsaction)

#### Example

```ts
import {
  WinccoaManager,
  WinccoaCnsAction,
  WinccoaCnsChangeType,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function cnsCB(
  path: string,
  changeType: WinccoaCnsChangeType,
  action: WinccoaCnsAction,
) {
  console.log(path, changeType, action);
}

function connect() : number {
  return winccoa.cnsAddObserver(cnsCb);
}
```

***

<a id="winccoactrlcallback"></a>

### WinccoaCtrlCallback()

> **WinccoaCtrlCallback** = (`value?`) => `unknown`

Type of callbacks that can be used with [WinccoaCtrlScript.constructor](#constructor-4),
[WinccoaCtrlScriptCache.constructor](#constructor-5) and [WinccoaCtrlScript.start](#start).

> ### CTRL
> The callback can be called from the CTRL script by using the CTRL function
>`callbackToJavaScript()`:
>
> `int callbackToJavaScript([anytype value[, <type> &returnValue]]);`
>
> #### Parameters
> - __value__: Optional parameter that will passed to the JavaScript
               callback function.
> - __returnValue__: Optional return parameter that will receive the return
>              value of the JavaScript callback function. Its type defines
>              how the JavaScript return value is converted to CTRL and
>              therefore cannot be a `mapping`, `anytype` or `mixed` or a
>              dynamic array of these types.
>
> __Returns__ `0` when successful, `-1 `in case of an error.

While not recommended, the callback can actually be an `async` function,
but there is no possibility to await the result from CTRL or JavaScript.
In this case, the return value must be ignored and `callbackToJavaScript()`
will return immediately while the callback function continues to execute.

#### Parameters

##### value?

`unknown`

Optional parameter that has been passed from CTRL.

#### Returns

`unknown`

Optional value that will be returned to CTRL.

#### Examples

```ts
import { WinccoaCtrlScript, WinccoaManager } from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function cbTest() {
  const ctrlCode = `int main() { return callbackToJavaScript(); }`;
  const script = new WinccoaCtrlScript(winccoa, ctrlCode, 'cbTest 1', () =>
    console.info('callback called'),
  );

  const sts = (await script.start()) as number;
  console.info(`Script finished with status ${sts}`);
}
```

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function hypotenuse(data: unknown) {
  const [a, b] = data as number[];
  return Math.sqrt(a * a + b * b);
}

async function cbTest() {
  const ctrlCode = `bool main(float a, float b)
  {
    float returnValue;
    dyn_anytype params = makeDynAnytype(a, b);
    bool success = (callbackToJavaScript(params, returnValue) == 0);
    if (success)
      DebugTN("Hypotenuse is " + returnValue);
    return success;
  }`;
const script = new WinccoaCtrlScript(winccoa, ctrlCode, 'cbTest 2', hypotenuse);

  const success = (await script.start(
    'main',
    [3.0, 4.0],
    [WinccoaCtrlType.float, WinccoaCtrlType.float],
  )) as boolean;
}
```

```ts
import {
  WinccoaCtrlScript,
  WinccoaCtrlType,
  WinccoaManager,
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

async function cbTest() {
  const ctrlCode = `int count(dyn_int range)
  {
    int sum, result;
    for (int i = range[1]; i <= range[2]; i++)
    {
      callbackToJavaScript(i, result);
      sum += result;
    }
    return sum;
  }`;
  const script = new WinccoaCtrlScript(winccoa, ctrlCode, 'cbTest 3', (data) =>
    Math.pow(data as number, 3),
  );

  const sum = (await script.start(
    'count',
    [[2, 12]],
    [WinccoaCtrlType.dyn_int],
  )) as number;

  console.log(`total sum is ${sum}`);
}
```

***

<a id="winccoadpconnectcallback"></a>

### WinccoaDpConnectCallback()

> **WinccoaDpConnectCallback** = (`dpeNames`, `values`, `type`, `error?`) => `void` \| `Promise`\<`void`\>

Type of callbacks from [WinccoaManager.dpConnect](#dpconnect).

#### Parameters

##### dpeNames

`string`[]

Names of the updated data point elements. Will always be an array, also
                if it contains only one name.

##### values

`unknown`[]

Updated values. Will always be an array, also if it contains only one value.

##### type

[`WinccoaConnectUpdateType`](#winccoaconnectupdatetype)

Type of the update.

##### error?

[`WinccoaError`](#winccoaerror)

In case of an error, the other parameters are undefined and this parameter will
             contain error information.

#### Returns

`void` \| `Promise`\<`void`\>

#### See

- [WinccoaManager.dpConnect](#dpconnect)
- [WinccoaConnectUpdateType](#winccoaconnectupdatetype)

#### Example

#### TypeScript
```ts
import {
  WinccoaManager,
  WinccoaConnectUpdateType,
  WinccoaError
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function connectCB(
  names: string[],
  values: unknown[],
  type: WinccoaConnectUpdateType,
  error?: WinccoaError
) {
  if (error) {
    console.log(error);
    return;
  }

  if (type == WinccoaConnectUpdateType.Answer)
    console.warn('--- Initial update ---');

  for (let i = 0; i < names.length; i++)
    console.info(`[${i}] '${names[i]}' : ${values[i]}`);
}

function connect() {
  let id = -1;
  try {
    id = winccoa.dpConnect(
      connectCB,
      ['ExampleDP_Arg1.', 'ExampleDP_Arg2.'],
      true
    );
  } catch (exc) {
   console.error(exc);
  }
}
```
#### JavaScript
```js
const { WinccoaManager, WinccoaConnectUpdateType } = require('winccoa-manager');
const winccoa = new WinccoaManager();

function connectCB(names, values, type, error) {
  if (error) {
    console.log(error);
    return;
  }

  if (type == WinccoaConnectUpdateType.Answer)
    console.warn('--- Initial update ---');

  for (let i = 0; i < names.length; i++)
    console.info(`[${i}] '${names[i]}' : ${values[i]}`);
}

function connect() {
  let id = -1;
  try {
    id = winccoa.dpConnect(
      connectCB,
      ['ExampleDP_Arg1.', 'ExampleDP_Arg2.'],
      true,
    );
  } catch (exc) {
    console.error(exc);
  }
}
```

***

<a id="winccoadpqueryconnectcallback"></a>

### WinccoaDpQueryConnectCallback()

> **WinccoaDpQueryConnectCallback** = (`values`, `type`, `error?`) => `void` \| `Promise`\<`void`\>

Type of callbacks from [WinccoaManager.dpQueryConnectAll](#dpqueryconnectall) and [WinccoaManager.dpQueryConnectSingle](#dpqueryconnectsingle).

#### Parameters

##### values

`unknown`[][]

Updated value(s) in a table-like structure:
[0][0] (empty)    | [0][1] column header   |         ...
----------------- | ---------------------- | ----------------------
[1][0] line name  | [1][0] content of line |         ...
[2][0] line name  | [2][1] content of line |         ...
...               | ...                    |         ...

e.g. this is the output for the query `"SELECT '_original.._value' FROM 'ExampleDP_Arg*'"` converted
to JSON:
```
[
  ["",":_original.._value"],
  ["System1:ExampleDP_Arg1.",2.43],
  ["System1:ExampleDP_Arg2.",5.76]
]
```

##### type

[`WinccoaConnectUpdateType`](#winccoaconnectupdatetype)

Type of the update.

##### error?

[`WinccoaError`](#winccoaerror)

In case of an error, the other parameters are undefined and this parameter will
             contain error information.
> When the query passed to [WinccoaManager.dpQueryConnectAll](#dpqueryconnectall) or
> [WinccoaManager.dpQueryConnectSingle](#dpqueryconnectsingle) is invalid, no exception will be thrown by
> these methods, but the first (and only) callback will contain a [WinccoaError](#winccoaerror) in this parameter.

#### Returns

`void` \| `Promise`\<`void`\>

#### See

- [WinccoaManager.dpQueryConnectAll](#dpqueryconnectall)
- [WinccoaManager.dpQueryConnectSingle](#dpqueryconnectsingle)
- [WinccoaConnectUpdateType](#winccoaconnectupdatetype)

#### Example

```ts
import {
  WinccoaManager,
  WinccoaConnectUpdateType,
  WinccoaError
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function  queryConnectCB (
  values: unknown[][],
  type: WinccoaConnectUpdateType,
  error?: WinccoaError,
) {
  if (error) {
    console.error(error);
    return;
  }

  if (type == WinccoaConnectUpdateType.Answer)
    console.warn('--- Initial update ---');

  // ignore line with index 0 (it's a header) and start with index 1
  for (let i = 1; i < values.length; i++) {
    console.info(`DPE = '%s', value = %s`, ...values[i]);
  }
};

function connect() {
  let id = -1;
  try {
    id = winccoa.dpQueryConnectSingle(
      queryConnectCB,
      true,
      "SELECT '_original.._value' FROM 'ExampleDP_Arg*'"
    );
  } catch (exc) {
    console.error(exc);
  }
}
 ```
#### Connecting with user data
To pass user data to the callback, it is not necessary to use a different
API method. Instead, an arrow function can be used to include user data
whenever a callback is called. The same pattern can also be used for
other callbacks, e. g. from [WinccoaManager.dpConnect](#dpconnect)
```ts
import {
  WinccoaManager,
  WinccoaConnectUpdateType,
  WinccoaError
} from 'winccoa-manager';
const winccoa = new WinccoaManager();

function  queryConnectCB (
  userData: string,
  values: unknown[][],
  type: WinccoaConnectUpdateType,
  error?: WinccoaError,
) {
  if (error) {
    console.error(error);
    return;
  }

  if (type == WinccoaConnectUpdateType.Answer)
    console.warn('--- Initial update --- ' + userData);

  // ignore line with index 0 (it's a header) and start with index 1
  for (let i = 1; i < values.length; i++) {
    console.info(`DPE = '%s', value = %s`, ...values[i]);
  }
}

function connectUserData(userData: string) {
  let id = -1;
  try {
    id = winccoa.dpQueryConnectSingle(
      // use arrow function to add userData for callback
      (values, type, error?) => queryConnectCB(userData, values, type, error),
      true,
      "SELECT '_original.._value' FROM 'ExampleDP_Arg*'",
    );
  } catch (exc) {
    console.error(exc);
  }
}
```

***

<a id="winccoalangstring"></a>

### WinccoaLangString

> **WinccoaLangString** = `string` \| `string`[] \| `object`

Represents a WinCC OA multi-language string in all possible [WinccoaLangStringFormat](#winccoalangstringformat)s.

***

<a id="winccoasyscondist"></a>

### WinccoaSysConDist

> **WinccoaSysConDist** = `object`

Data type that contains details about DIST events.

#### See

[WinccoaSysConEvent.Dist](#dist)

#### Properties

<a id="event"></a>

##### event

> **event**: [`WinccoaSysConEvent`](#winccoasysconevent)

Event that triggered the listener

<a id="reason"></a>

##### reason

> **reason**: `string`

Reason for the notification

<a id="system-2"></a>

##### system?

> `optional` **system**: `number`

System ID

<a id="systemname"></a>

##### systemName?

> `optional` **systemName**: `string`

System name

***

<a id="winccoasyscondpchanged"></a>

### WinccoaSysConDpChanged

> **WinccoaSysConDpChanged** = [`WinccoaSysConDpDetails`](#winccoasyscondpdetails) & `object`

Data type that contains details about a renamed data point or changed alias.

#### Type declaration

##### newName

> **newName**: `string`

new name of the renamed data point

##### oldName

> **oldName**: `string`

old name of the renamed data point

#### See

 - [WinccoaSysConEvent.DpRenamed](#dprenamed)
 - [WinccoaSysConEvent.DpAlias](#dpalias)

***

<a id="winccoasyscondpdescription"></a>

### WinccoaSysConDpDescription

> **WinccoaSysConDpDescription** = [`WinccoaSysConDpDetails`](#winccoasyscondpdetails) & `object`

Data type that contains details about a changed data point description.

> __NOTE__
>
> the language strings contained in __oldText__ and __newText__
> are always returned in [WinccoaLangStringFormat.Object](#object)

#### Type declaration

##### newText

> **newText**: [`WinccoaLangString`](#winccoalangstring)

new description of the data point

##### oldText

> **oldText**: [`WinccoaLangString`](#winccoalangstring)

old description of the data point

#### See

- [WinccoaSysConEvent.DpDescription](#dpdescription)
- [WinccoaLangString](#winccoalangstring)

***

<a id="winccoasyscondpdetails"></a>

### WinccoaSysConDpDetails

> **WinccoaSysConDpDetails** = `object`

Data type that contains details about a created or deleted data point.

#### See

 - [WinccoaSysConEvent.DpCreated](#dpcreated)
 - [WinccoaSysConEvent.DpDeleted](#dpdeleted)

#### Properties

<a id="dp-3"></a>

##### dp

> **dp**: `string`

Data point name

<a id="dptype"></a>

##### dpType

> **dpType**: `string`

Data point type

<a id="event-1"></a>

##### event

> **event**: [`WinccoaSysConEvent`](#winccoasysconevent)

Event that triggered the listener

<a id="requestermanagerid"></a>

##### requesterManagerId

> **requesterManagerId**: `number`

ID of the manager that requested the change

<a id="requesteruserid"></a>

##### requesterUserId

> **requesterUserId**: `number`

ID of the user that requested the change

***

<a id="winccoasyscondpformatunit"></a>

### WinccoaSysConDpFormatUnit

> **WinccoaSysConDpFormatUnit** = [`WinccoaSysConDpDetails`](#winccoasyscondpdetails) & `object`

Data type that contains details about a changed data point format and/or unit.

#### Type declaration

##### newFormat

> **newFormat**: `string`

new format  of the data point

##### newUnit

> **newUnit**: `string`

new unit  of the data point

##### oldFormat

> **oldFormat**: `string`

old format  of the data point

##### oldUnit

> **oldUnit**: `string`

old unit  of the data point

#### See

[WinccoaSysConEvent.DpFormatUnit](#dpformatunit)

***

<a id="winccoasyscondptypechanged"></a>

### WinccoaSysConDpTypeChanged

> **WinccoaSysConDpTypeChanged** = [`WinccoaSysConDpTypeDetails`](#winccoasyscondptypedetails) & `object`

Data type that contains details about a created or deleted data point type.

#### Type declaration

##### newName

> **newName**: `string`

New data point type name

##### oldName

> **oldName**: `string`

Old data point type name

#### See

[WinccoaSysConEvent.DpTypeChanged](#dptypechanged)

***

<a id="winccoasyscondptypedetails"></a>

### WinccoaSysConDpTypeDetails

> **WinccoaSysConDpTypeDetails** = `object`

Data type that contains details about a created or deleted data point type.

#### See

 - [WinccoaSysConEvent.DpTypeCreated](#dptypecreated)
 - [WinccoaSysConEvent.DpTypeDeleted](#dptypedeleted)

#### Properties

<a id="dptype-1"></a>

##### dpType

> **dpType**: `string`

Data point type

<a id="event-2"></a>

##### event

> **event**: [`WinccoaSysConEvent`](#winccoasysconevent)

Event that triggered the listener

<a id="requestermanagerid-1"></a>

##### requesterManagerId

> **requesterManagerId**: `number`

ID of the manager that requested the change

<a id="requesteruserid-1"></a>

##### requesterUserId

> **requesterUserId**: `number`

ID of the user that requested the change

<a id="system-3"></a>

##### system

> **system**: `number`

System ID

<a id="systemname-1"></a>

##### systemName

> **systemName**: `string`

System name

***

<a id="winccoasysconredu"></a>

### WinccoaSysConRedu

> **WinccoaSysConRedu** = `object`

Data type that contains details about REDU events.

#### See

[WinccoaSysConEvent.Redu](#redu)

#### Properties

<a id="event-3"></a>

##### event

> **event**: [`WinccoaSysConEvent`](#winccoasysconevent)

Event that triggered the listener

<a id="hostnum"></a>

##### hostNum?

> `optional` **hostNum**: `number`

Number of the host that reported the event

<a id="reason-1"></a>

##### reason

> **reason**: `string`

Reason for the notification

<a id="seconds"></a>

##### seconds?

> `optional` **seconds**: `number`

Delay in seconds

***

<a id="winccoatime"></a>

### WinccoaTime

> **WinccoaTime** = `Date` \| `number`

Represents a WinCC OA time value in all possible [WinccoaTimeFormat](#winccoatimeformat)s.

***

<a id="winccoaversiondetails"></a>

### WinccoaVersionDetails

> **WinccoaVersionDetails** = `object`

Version information returned by [WinccoaManager.getVersionInfo](#getversioninfo)

#### Properties

<a id="api"></a>

##### api

> **api**: `object`

API version details

###### version

> **version**: `number`

API version number, e.g. `7`

<a id="winccoa-1"></a>

##### winccoa

> **winccoa**: `object`

WinCC OA version details

###### display

> **display**: `string`

WinCC OA version for display purposes, e.g. `'3.20'`

###### major

> **major**: `number`

WinCC OA major version number, e.g. `3`

###### minor

> **minor**: `number`

WinCC OA minor version number, e.g. `20`

###### numeric

> **numeric**: `number`

WinCC OA version as an integer, e.g. `320000`

###### numeric\_full

> **numeric\_full**: `number`

WinCC OA version number including patch as an integer, e.g. `320011`

###### patch

> **patch**: `number`

WinCC OA patch number, e.g. `4`

###### platform

> **platform**: `string`

WinCC OA platform info , e.g. `'Windows AMD64'`

###### revision

> **revision**: `number`

WinCC OA revision number, e.g. `0`

###### version

> **version**: `string`

WinCC OA version, e.g. `'3.20'`

## Variables

<a id="log"></a>

### log

> `const` **log**: `Readonly`\<\{ `debugF`: (`flag`, ...`data`) => `void`; `fatal`: (...`data`) => `void`; `info`: (...`data`) => `void`; `severe`: (...`data`) => `void`; `warning`: (...`data`) => `void`; \}\> = `ConnectionBinding.instance.log`

Convenience access to logging methods when no instance of [WinccoaManager](#winccoamanager)
is available.

This is particularly useful for `log.debugF()` and `log.fatal()`, which
don't have a corresponding method on `console`.

#### Example

```ts
import { log } from 'winccoa-manager';
log.debugF('REDU', `This message is only logged when debug flag 'REDU' is set`);
```

## Functions

<a id="delay"></a>

### delay()

> **delay**(`seconds`, `milliseconds`): `Promise`\<`unknown`\>

Convenience method for waiting a given time period (in seconds plus optional milliseconds).
Implements the same interface as CTRL function delay().

#### Parameters

##### seconds

`number`

Seconds to wait before continuing.

##### milliseconds

`number` = `0`

Milliseconds to wait before continuing.

#### Returns

`Promise`\<`unknown`\>

Promise - will be resolved after given time interval is elapsed.

#### See

- [CTRL function `delay()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlA_D/delay.html?hl=delay)

#### Example

```ts
import { WinccoaManager, delay } from 'winccoa-manager';
const winccoa = new WinccoaManager();

await delay(1, 500); // wait for 1.5 seconds
```

***

<a id="isdbgflag-2"></a>

### isDbgFlag()

> **isDbgFlag**(`flag`): `boolean`

Queries the value of a debug flag.

#### Parameters

##### flag

Number or name of the debug flag to query.

`string` | `number`

#### Returns

`boolean`

`true` if debug flag is set, `false` if not set.

#### See

- [log](#log)
- [CTRL function `isDbgFlag()`](https://www.winccoa.com/documentation/WinCCOA/latest/en_US/ControlE_R/isDbgFlag.html)

#### Example

```ts
import { isDbgFlag } from 'winccoa-manager';
console.info(isDbgFlag('REDU'));
```
