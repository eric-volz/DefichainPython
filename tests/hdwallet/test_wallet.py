import pytest
import json
from defichain import Wallet
from defichain.networks import DefichainMainnet


class TestVectors:
    DEFAULT_1_ADDRESS: str
    BECH32_1_ADDRESS: str
    LEGACY_1_ADDRESS: str
    WIF_1_KEY: str
    UNCOMPRESSED_1: str
    COMPRESSED_1: str
    PRIVATE_1_KEY: str
    PUBLIC_1_KEY: str
    CHAIN_CODE_1: str
    HASH_1: str
    FINGER_PRINT_1: str
    DUMPS_1: str
    ENCRYPTED_1: str

    DEFAULT_2_ADDRESS: str
    BECH32_2_ADDRESS: str
    LEGACY_2_ADDRESS: str
    WIF_2_KEY: str
    UNCOMPRESSED_2: str
    COMPRESSED_2: str
    PRIVATE_2_KEY: str
    PUBLIC_2_KEY: str
    CHAIN_CODE_2: str
    HASH_2: str
    FINGER_PRINT_2: str
    DUMPS_2: str
    ENCRYPTED_2: str

    DEFAULT_PASSPHRASE_ADDRESS: str
    BECH32_PASSPHRASE_ADDRESS: str
    LEGACY_PASSPHRASE_ADDRESS: str
    WIF_PASSPHRASE_KEY: str
    UNCOMPRESSED_PASSPHRASE: str
    COMPRESSED_PASSPHRASE: str
    PRIVATE_PASSPHRASE_KEY: str
    PUBLIC_PASSPHRASE_KEY: str
    CHAIN_CODE_PASSPHRASE: str
    HASH_PASSPHRASE: str
    FINGER_PRINT_PASSPHRASE: str
    DUMPS_PASSPHRASE: str
    ENCRYPTED_PASSPHRASE: str

    ENTROPY: str
    MNEMONIC: str
    SEED: str
    SEED_PASSPHRASE: str
    xPRIVATE_KEY: str
    xPUBLIC_KEY: str
    WIF: str
    PRIVATE_KEY: str
    PUBLIC_KEY: str
    PATH_1: str
    PATH_2: str
    INDEX_1: str
    INDEX_2: str
    INDEX_3: str
    INDEX_4: str

    ROOT_xPRIVATE_KEY: str
    ROOT_xPUBLIC_KEY: str
    ROOT_xPRIVATE_KEY_PASSPHRASE: str
    ROOT_xPUBLIC_KEY_PASSPHRASE: str
    STRENGHT: str
    PASSPHRASE: str
    LANGUAGE: str
    CRYPTOCURRENCY: str
    SYMBOL: str
    SEMANTIC: str
    NETWORK: str

    FILENAME: str


class Vectors(TestVectors):
    DEFAULT_1_ADDRESS = "db1UZE7tyvZ8R6V4HavCeCifKzLUiFDqxa"
    BECH32_1_ADDRESS = "df1q2n54p3xnvk3djulmdvresl3p5xmzzn43zm264a"
    LEGACY_1_ADDRESS = "8Nppz7bUwsQHTrwJdKKeYVPaGS9mcZyf2J"
    WIF_1_KEY = "L2qGxrTTFxoU5vygbRDHz7g8aa1951ZvDwiTK46t8jCvH37C3GUN"
    UNCOMPRESSED_1 = "ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07baed4b3d4c6a1a7d720dfa1f7cf1d12bc97a5baee53dde8c2697a83cada6569c"
    COMPRESSED_1 = "02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07"
    PRIVATE_1_KEY = "a77ba904f0a431f49be1c83bb8847b5d1002f551a5e0fda5f4954fd90d78807d"
    PUBLIC_1_KEY = "02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07"
    CHAIN_CODE_1 = "dc75ac21bc729ea83d363d289746ec59d61b2d9c8f56bd61d6ef062dd9e8222b"
    HASH_1 = "54e950c4d365a2d973fb6b07987e21a1b6214eb1"
    FINGER_PRINT_1 = "54e950c4"
    ENCRYPTED_1 = "6766504f554258586468666d5278616c77714562365842414969372f7952462f58456f38663749446f623279305474577330745a5a3445466933744b68324e56596752754f525133546b664262434f3836427675786b4754726e796a7a496b797967652b702b58663333626d6a7a364839393875344b4f37594a67552b4d6e5476726336644f76367271443448536d3739734c50553550676c63314744717a5072502b5a2b5973396648376970397953315847505565776671784757466b6b69322f77674c79766d2b71616777496f58764b76754353674a4e78416b4b7a6c65427862505a594b594e78382f495a79384f726a30315538376c747838626a7a2f71537364766d736249557264463965305a6e75567477625739624b444d4a6637484469636b6167376b50633339456e512b692b4b556647734d44543862764975717a4154575a6a733175796d76703051315a39334b6d6f4f6d745352666c426350706c5a5a7139587a5a7332363156734d4b524d5251466b6941517059496139654358664136326255453665302f387338356278444c52657676517a5a737363307a435656614273315354736c36373731317842574561397274317a6b6e6a315258537673666a67695434554533692f57636b47514c7970464b4a2f345470677577562f53736a507259736d542b6c6b464b6b655452414b7449356a45316f6b64432f5447754d76537259495557305a314b6d4b474d736c5653424c2b2f314c41496c365767593244666d756f586f69694666447738426e663167456e4568444f316f4e756245525831554f616158762b784d6a6d6f38645a576d526f52567234317473627235724e384f4258324b62547266365065484e4b47706c3962754a4d48746270735a6a61787354706d45667146344a67376533685a54616b696e35386c594147362f446b53554c4538454a6239437071507252414b374656786b587a30516575744d4e54634b5774774c6946524476343658726a56784f2f665344566e48356952766a6b2f74337758667661346d633779344e465a39614437784c7170626c47336d663662776c39342f4d7668744a55576b6d4f453148597374486c492b3231514a2b4959567772734f7a69373874312f6367634e556e356a587541344e7138792f435263682b3269597a496343495345463930644775575a6f2b66457a532f4c5474744c683345694d634a704d6d4651527a4b6778727864473447644839696731746d376b64664b634b5674647655674868586b67526a514172475251346679453058566e66457176696c464943425038586579784f3067346b6946572b77417676634f414469692b6d516b4c2b4b412b7278524f6d51774b35464b776b6877426a58624d477037525a56624c47536974447039364c7455556d515472414a3877786e3644536b55714d654f4e347a597078506945543962302f4d663858664e484b43532f3832513162542b30357651414b6935566b4f4b2f556e63544c35334f6c54594430454f4a35743939526b4a45527859424375646654564e2b6d5768536b6869524d494f3142677965524f773930555966595a747a71477a546c4b56515967347868466f3156545a6c4130776974333561772f713231564c36446c6151656239786978314968656b747567656e324b656542456733386d2b6b306b684269554f6e6c372b5646456b704f7a53744e33387731485a6163484f325962456f313470744464643947557a4763515368344947486558336f484f6435506d584a3269776d6271473446632f42506a314e5a6d386e5a72624858312f4a633075664454635a51546566533270616e524f32532b6d3431772f485030534d517444676c553238324b58676679365a6a4466634f642b7561354574417236446861646b674c444152547867556664686f686d56332b79652b54386c57436454734a354273484d726b3246794c56624b6a2f504c463573625561547138797a6f6b77394d75724145797a396248554a4d45434c644d31746f664b7331452b776c68667a334f66484b4a736c75716b555467545475457176514a71454e474e4554684a35647837776b55526e76735a4c4c5048737973342b3465467a3871627458635035596b6e793641496b6378644b427173724d5575376e4f4e3472714c5733767642752f61717172586933497272666d32725234346868343673416d322b6e76496e6137714d65617047345a4b6f33426e4b73375168395a474a62634d46444a6d6b4f757162352f4d536e37616d65624d54554938493731666d766756556945716f53767334312f52733657516b48737873427a4734464831423652667150525930326c6a3632756d676b524156482b354c724d374a69582f6b514e714e75644833316b64626a4e3741436e3544474471624b47434453486e6b6e366d2f3975557761566844635243706b62467275614e61443649366973584a6e2f63376b38346e66586677566c78524849344e3272324b36326b323047776a4e50475270644e3263794b6a654e4c2b545945754b4f464b586a677a782f356a36696953524a4550596c714a475079336b57466e786967485642556863646644554435565964456f2f4e786155735441563434514c453535743632712b66553839725a4e6a79376a3050706d4377616c724246416766495448486e4c6674537967764b394f54765856307353444264462f4b47674d7946536865554c786947634e732b2b58332f70534c4a4a5347423978526c5963712f3975776d62366630546e4646686655463566325a5563697439576c614831626f50397a69735535394b364c"

    DEFAULT_2_ADDRESS = "dFmeYSHXymdybpjUmNTsUfvX4vxcznXXux"
    BECH32_2_ADDRESS = "df1qtmy47ksc9t8z0avnn9xqelyy4u5ujcsjeqx99y"
    LEGACY_2_ADDRESS = "8Pj3UbHEYBtXUkxo9DFrz3a6ShssS3tmLr"
    WIF_2_KEY = "KzxppKqb9MT8GP94tnypD8ux3b5NvfrQu7UFZfTFELSDq77Rx2C4"
    UNCOMPRESSED_2 = "da11be60fbc6b2dbadc6678370ed153463dc9f499ff9ac2efb91b0831686ff6f6f63fe47b165211d039c8cd78c4f2fbe3277317bf1e94a5dbfd7e0e73f6ddd10"
    COMPRESSED_2 = "02da11be60fbc6b2dbadc6678370ed153463dc9f499ff9ac2efb91b0831686ff6f"
    PRIVATE_2_KEY = "6fb11ca588b36b13e600bbd06af491f1dc2495f51cc6acaec6f0916648370af5"
    PUBLIC_2_KEY = "02da11be60fbc6b2dbadc6678370ed153463dc9f499ff9ac2efb91b0831686ff6f"
    CHAIN_CODE_2 = "3cfe54f06b1ea806db43e6cd6a10399615b535be64a9400229b1cb419e82e1f8"
    HASH_2 = "5ec95f5a182ace27f593994c0cfc84af29c96212"
    FINGER_PRINT_2 = "5ec95f5a"
    ENCRYPTED_2 = "573632466648776e72333856474f6d6a706e437964695978353865656f6e2b33432b396c4f41634c43622f4451444577565a62335a79667056546367464535756d64764a7344674653677554504e334a6f67365943797a4b6d624d6c7245563245797150587341356b7041774d34346b335776304f5568714a416c7a4847667279466a706666467761744a72783971705265344e535638324c484a31536745333346674a6737474d634c445144383735694d736275584b72506d49537a54725a3137617959486e6e774666636337484366512f482b312b455954525678374c4e32377a43544d46712b6e4659626841425370704f4534644a50394d59696375686376623159536f69414a6362446c35367068647a6e4c4c654562715576544b32754f464548627136657530646c544a464550325934355251766d4c76744b66506c794a706c364c4c4c4f384a5937726843386f4a68483861596f425a794648576e736b584a516d662b3347706547726547504e683957496c44724d6256535658736363757762473777462f4e68786b30314d6d4c6a50726e6a386c45777a352b47686663754f5149656442306d6c4b7a3273436c734a2b73503544637069466b47786c6d517275736b36452b6570303134783858685a744b5a76394d34697371336157476f5959654879444b6f44393831324e796c524465672f52376169546176682f77654731704f343651692f73376c4e4b376677436d5835734373716c36754574544a59726e506d4e4b4a6c336d6f7870676764704756424977566d365a7735494b44443645456f36326651684f2f7a67305041542f4367322f484a6e6f6b7a43745758636a586b45686b56514f482f517665434736432b7a654141576e4753694d333155366b594466567241625651414f345a752b6559435231524f554c45616555726f6b497a3375386954524a43456449747564766a6f7a7a6a63426a302f424572327371615173373167637434316c6671617a6f616c7a2f5857544d5973594a487759356139627a3941462b64744e4a6c4d6138674a684537334752756e43707759784c33714e6758754a6f696a3053464d5266736f6c6b7a446769475172776d42654d355979736966594f644c4d56764f41655641675771496e426131576a664b585369453142757a7a5346786a536d31622b4b5231516f6a4178376d7469737055655164674146706f56456d326a36784c716457567a6f53466743726f6f6f7776727070766f666354492f6f324b322b67584c36447637427342506e32676f6d492b6b316978594e7465785333627553465737724c4334503944715776315665412f58795453616432557278447363366954694551307a2f787a376d677a37476735744131636f4447734b6d474232726c69524f4b346751774577326b6d7a446866456a3951586f786f574247617871625830555939497a352f6f6f3435644764445a376b5a7258425a49473873424a30547241725438447a4436356b413872724f704d50437839426350367566426944374b4f4c6136752f554c31795761684270384346704a6f6e367658542f564f756536694d374d525570353741797a45757a31744a6c302b613873514f793368745a644e37694169742b2f3171456464436679373367413370784e5a59573572535656564737667376783667492f396e394e6f58596f324c79526f4a7861507a5a47575041352b6b5142635a302f4674624641374c466c64754854424a566647773265745467424d396b6d595454456b6152553579687247704d65305335753072706d39363879354b573964434e4958587274456c456c3655382f6a63425436652f4e4a61726c4d652b466e4871497370314b6563444d3564395737716368447a6d7453397732504b5672464379454e4b5358304846427a6a61545841657439697a5970576d4454677153694c632b467a734e4a5649486b464771644c4c5051326d316a414f396548473345596b6a5944416733324a68582f7175304f5a42536d69526c394c626f6862426949557a554c6251455436756f4771384850394939397779725836554a4b2f423643426e4d7a345659444179414c67375633495a473568374d79716a486c743835764450593262344c79324645496d757332324678312b5451732b6d41582f6b532b6f3534595733647a564153477677726853434b776b677851574a62374959586d64597a48684a46766f384b5178576263737a734e6f6e347a6d526c306c70464446657770523739494b473655477944477079653776656a796f6c684d2f4173534351557a3148546332342b667a424e6c4f2b4d795a365978757078504f75594b424759454f4c3538344c44526f47675a755968343973595178677847364c4564667259325245693771426a4a6e754e376a2b524f53736a765a57436c4856494e337966453755386474506f72435770615469357646384d555642446b325966733667756a785539717036365a3161533757627956594e304d79722f2b48637969756a41774c6b7754796c543834483972586c614c73344e2f6b6d73785a697265302f4c494a764f794d636c3565554573764b332f34367779717469426545734b567449307a4c56763039796b5a686748584d6a5376534f59524f6e5657547573574c6d38616c65337269746e32396b55574964574c376a4f6d737a643963464d397342614634316b65566e57454b49636c494c76782f6b4261512b623345465a6f4b7a446c446875765078462f38583074786a56335550684650622b4d6b54555a346c646642624c624e354c716f77334662584656535a3137494c4d"

    DEFAULT_PASSPHRASE_ADDRESS = "dM64uZpczPDYSgEEi3sC1FmfeD3VEsUAVX"
    BECH32_PASSPHRASE_ADDRESS = "df1qd4ke9dcyzeg09udmcryxlftplsatkl5wv024sv"
    LEGACY_PASSPHRASE_ADDRESS = "8R4Te8wY8pKxYjxT8Y7MjdeaQEXPw3TVWr"
    WIF_PASSPHRASE_KEY = "L1BN9Nn2tMr6Zvy8tL1wxRe1CXrkF7BjCEucocUKmWPpw2UjoGuu"
    UNCOMPRESSED_PASSPHRASE = "2e2927c66300c407e0e7f148f54b9be305385a68d9dcd68b522749dbe68e14d80c838cc503ad6e2024ce4387bc0dffb0296228d3f5f8d8176535f6a160a22f37"
    COMPRESSED_PASSPHRASE = "032e2927c66300c407e0e7f148f54b9be305385a68d9dcd68b522749dbe68e14d8"
    PRIVATE_PASSPHRASE_KEY = "762499a31b7b53451d7ebd62c49a5201632293ebb2dff0aa0962d2c465f80bff"
    PUBLIC_PASSPHRASE_KEY = "032e2927c66300c407e0e7f148f54b9be305385a68d9dcd68b522749dbe68e14d8"
    CHAIN_CODE_PASSPHRASE = "2ecdfb1efd4bdc514ddfcff2d6225c7b1604f4ede53ca1f52a3a1dda3000e989"
    HASH_PASSPHRASE = "6d6d92b7041650f2f1bbc0c86fa561fc3abb7e8e"
    FINGER_PRINT_PASSPHRASE = "6d6d92b7"
    DUMPS_PASSPHRASE = "{'cryptocurrency': 'Defichain', 'symbol': 'DFI', 'network': 'mainnet', 'strength': 128, 'entropy': 'ee535b143b0d9d1f87546f9df0d06b1a', 'mnemonic': 'unusual onion shallow invite supply more bubble mistake over make bracket cry', 'language': 'english', 'passphrase': None, 'seed': '313a29e024ad78b0ce1d978c850c4e0284ec18caff25059449fd583e6f7aa265f1c2968cb2e5867fc6d51ad2a40c72ee451f3b81a36d5f3dc4ea4e94a25c8f79', 'root_xprivate_key': 'xprv9s21ZrQH143K3wyDj3RFDZ2NyueHmj42SkAhqN62guhz5hr5N2qzPKzLnzrRsYdi4DwoeBeqKyjizqdiSNr3yAn2yMMMwWoJQp2PsC4BPLp', 'root_xpublic_key': 'xpub661MyMwAqRbcGS3gq4xFagy7XwUnBBmsoy6JdkVeFFExxWBDuaAEw8JpeFVhYKJctV1ZXFdV6SPoN41MVkNMdTcZpxcqJoRWgJvede7ME9n', 'uncompressed': 'ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07baed4b3d4c6a1a7d720dfa1f7cf1d12bc97a5baee53dde8c2697a83cada6569c', 'compressed': '02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07', 'chain_code': 'dc75ac21bc729ea83d363d289746ec59d61b2d9c8f56bd61d6ef062dd9e8222b', 'private_key': 'a77ba904f0a431f49be1c83bb8847b5d1002f551a5e0fda5f4954fd90d78807d', 'public_key': '02ff92aed3b7563d73da7c2c8810ec78182574e12a8210878b5d7b91ee0ae70f07', 'wif': 'L2qGxrTTFxoU5vygbRDHz7g8aa1951ZvDwiTK46t8jCvH37C3GUN', 'finger_print': '54e950c4', 'semantic': 'p2pkh', 'path': 'm/1129/0/0/0', 'hash': '54e950c4d365a2d973fb6b07987e21a1b6214eb1', 'addresses': {'legacy': '8Nppz7bUwsQHTrwJdKKeYVPaGS9mcZyf2J', 'bech32': 'df1q2n54p3xnvk3djulmdvresl3p5xmzzn43zm264a', 'default': 'db1UZE7tyvZ8R6V4HavCeCifKzLUiFDqxa'}}"
    ENCRYPTED_PASSPHRASE = "315567506e5a46367a43666a326d70594d50674e416c566f5845716f6e4272366a303668464232422f476178426e44595a48424a30434436593435716b715a7468712f5951414a586c52345a7679674e355848527951466a734c4e56355035707733664b794e63534d4d58486f466f796a562f4d3956435a3068437a422b3878613038724743776a58316d2b6e6c446b73516a664e31624d2b615469355634614b614542523276636e6c693973334e2f7938584368645638644253366b435730797073333739377357624856454e57354e34494b343775516d545471434137546d71546345434235654a6e6f7a6d624b41694c724e5931683158664466593845582b4f424f723142676b694f4868726857366f7269752b687449316f396c382f6b6f51644b6467616b6f46306e694866447752314470374f322f4241616e4e69416b2f7865615841547a5a33714b354154467a705066707941586863506776784d3656566373666c7665703375736d417554765457666766725961547443494c6369484535454b536975784a78634e625336486255564e714f6a34675063334c7762476b47754b4437376f43367172454b7670416b3270307a5854304752736b524d624a684d446c7335736348503872646f6e33414a486b4b6a7067685454386e7172742b6f4c6475422b5357447875786c792b674b4579506f424f5a463363716b636470316a5233526759597368636b494b706747434d6966362b6b444b755848707650684349506c4344487170366b4633623673336133586b3343544e736b7858796f53332f476559466a4270346356424a4b664534744d63506b49453561426b3369433539593073524a365a754259665a6a63617150616467574d323135554f7376522b715262426a664b3970527674616d6d5645434543515467556536336f4d2b464e78594d38355a47476a424e553242583672526876676a6f515a383077513159734c66666561733433674d4a636f376a4d74326e614c3534463247496f30373956544d546a47397974644b4149675476466d5073762b776b774573347153495077586e72654a6a48376473436f487449744a4330747a447765493175336a776d6732586a393439326f417743746b427179505256735a442f436d6b7342565a56394f754f657375745376435459504472477269506852723151476c67494377354856347636524c52387563694c6a2b442b787271732b5943762b61764b445661626a704242306e73584e37746e6d41534a6f792b774e5a595062464d45496a4e4f394f6838697a566945426b4c62334d676e4a494d512b534d5a37764f304c68305539574d585a517a316b7a424e585a3439716b7530486479377754537431735178706770476b513572356370577655794344773875364d31466c53552f6d3763352f7a504a72484c4d754a48585a48575a6439687742567763694b4e356f4a4869384c4a4f714b3157777654442f774639354b535476507877346656644c58615067772f562f573955504d47384d414445794c353644376f786957735172302b624465597a74356f52464955327a785474383042645a4b584e775777624d4f5641527631346e484f6b66505579744d4c7348627531696c30304e2f6b46354e774d384c34664a3161667643744a39573946754a782f7478396c3035424968436a4e643952584d4e336436774f58435770354e4361446554306142363556756a457352584b484674714a38674e6d716b614e56556764776c65573750703946646f64663044792f4c736f34655a4d4567425358632f38514e7272446344616c46346358764a445947454346376a5962364b396e4978664e554a31373367566b7a6e694c64335474434e796e4a696d304331554b334369512b464d4563326379743731394a67552b7533316c38437262573373523847584646397232682f445844647050772b6249776c554e2b3053723453674e536f7649635178707677497879505632725a4e7a2b4f77566a33326f31693066484575524536684d33546e4665696b5433616a52685662772b417853437a7656304b31577a4c6f2f367634654732554c6273625179744c57435841364c7366456c3253695a694d557672565335453576654d483544446c4f314f38422f51344d55355a47677978706f6a74337a556d35646d4441703349487a59552f4d6b696a456b4d474e4d78394f4b526662792f42774172446d6a5968465631646663594b4f316962335166775934683977437a472f6434745141324f437044344d706145435a397335365954575039637a4277316c7362574f30595a5679563850622f494739574c73656479506f6a62314975654b695a6964533157504741354a466663756930514d4c39556f66314e704166333334565367754249375349793659795a42533746656e6d794c6a6a2b7671546637754c314e50352b3237477138776e7269414144363463667779683043693451527a59366f507a386357515a3055765676743146703041436e72444659654a32754871457375463267313443634d6d3274396d6e6a4d484e4b36706c31326768673145676f3243434b6e676347345043506f49552b4c316b4d4c644b4a454b4b30384755696439694132766a3562474f2f7176555170374d6e73444732704a4d7853367648342b4a6147376e786f46685249575878773646634330696c7a3651515974535344654c38534d4371445931477144572b4369386f4e77507330366f65535138446c58413854586b394577646251674261595962735a514971734f47787778624a31696b6b566b3067536b4d64766245387a426747466a32566d554d42615061646e546436626532773d3d"

    ENTROPY = "ee535b143b0d9d1f87546f9df0d06b1a"
    MNEMONIC = "unusual onion shallow invite supply more bubble mistake over make bracket cry"
    SEED = "313a29e024ad78b0ce1d978c850c4e0284ec18caff25059449fd583e6f7aa265f1c2968cb2e5867fc6d51ad2a40c72ee451f3b81a36d5f3dc4ea4e94a25c8f79"
    SEED_PASSPHRASE = "df653d88cc549d56cc460a34167f429ee987d4b8651065abe88f05cb1d9be82e836bb749db36eddb306d6eb1bb6bd6bb77e55a0961673c804359eb13b80a61bf"
    PATH_1 = "m/1129/0/0/0"
    PATH_2 = "m/1129/0/0/1"
    INDEX_1 = "1129"
    INDEX_2 = "0"
    INDEX_3 = "0"
    INDEX_4 = "0"

    ROOT_xPRIVATE_KEY = "xprv9s21ZrQH143K3wyDj3RFDZ2NyueHmj42SkAhqN62guhz5hr5N2qzPKzLnzrRsYdi4DwoeBeqKyjizqdiSNr3yAn2yMMMwWoJQp2PsC4BPLp"
    ROOT_xPUBLIC_KEY = "xpub661MyMwAqRbcGS3gq4xFagy7XwUnBBmsoy6JdkVeFFExxWBDuaAEw8JpeFVhYKJctV1ZXFdV6SPoN41MVkNMdTcZpxcqJoRWgJvede7ME9n"
    ROOT_xPRIVATE_KEY_PASSPHRASE = "xprv9s21ZrQH143K4VewJbSSUZf9MCBYFLRkEG1vWgtCLqJ68nmSCsicHifVpfEGBxsWgJQooWXe8HRg6gsghddtJkKAPgf416F3o47XBov2N2U"
    ROOT_xPUBLIC_KEY_PASSPHRASE = "xpub661MyMwAqRbcGyjQQcySqhbsuE22eo9bbUwXK5HouAq51b6akR2rqWyyfxEmqVRnDf2S42JeF9YiQ6RmtNQv2VLHY6JtPcqXJfk5c1F3w4D"
    STRENGHT = 128
    PASSPHRASE = "passphrase"
    LANGUAGE = "english"
    CRYPTOCURRENCY = "Defichain"
    SYMBOL = "DFI"
    SEMANTIC = "p2pkh"
    NETWORK = "mainnet"

    FILENAME = "wallet"


@pytest.mark.hdwallet
def test_wallet():  # 01
    assert Wallet(DefichainMainnet)
    assert Wallet(DefichainMainnet, "P2PKH")
    assert Wallet(network=DefichainMainnet, semantic="P2PKH", use_default_path=True)


@pytest.mark.hdwallet
def test_from_entropy():  # 02
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY, language="english", passphrase=None)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_mnemonic():  # 03
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_mnemonic(mnemonic=Vectors.MNEMONIC, language="english", passphrase=None)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_seed():  # 04
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_seed(seed=Vectors.SEED)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_xprivate_key():  # 05
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_xprivate_key(xprivate_key=Vectors.ROOT_xPRIVATE_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_xpublic_key():  # 06
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_xpublic_key(xpublic_key=Vectors.ROOT_xPUBLIC_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    # assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    # assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    # assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_wif():  # 07
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_wif(Vectors.WIF_1_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    # assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    # assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    # assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    # assert Vectors.SEMANTIC == wallet.semantic()
    # assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_private_key():  # 08
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_private_key(private_key=Vectors.PRIVATE_1_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    # assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    # assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    # assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    # assert Vectors.SEMANTIC == wallet.semantic()
    # assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_public_key():  # 09
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_public_key(public_key=Vectors.PUBLIC_1_KEY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    # assert Vectors.STRENGHT == wallet.strength()
    # assert Vectors.ENTROPY == wallet.entropy()
    # assert Vectors.MNEMONIC == wallet.mnemonic()
    # assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    # assert Vectors.SEED == wallet.seed()
    # assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    # assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    # assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    # assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    # assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    # assert Vectors.SEMANTIC == wallet.semantic()
    # assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_path():  # 10
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()

    wallet.from_path("m/1129/0/0/1")

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_2 == wallet.uncompressed()
    assert Vectors.COMPRESSED_2 == wallet.compressed()
    assert Vectors.CHAIN_CODE_2 == wallet.chain_code()
    assert Vectors.PRIVATE_2_KEY == wallet.private_key()
    assert Vectors.PUBLIC_2_KEY == wallet.public_key()
    assert Vectors.WIF_2_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_2 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_2 == wallet.path()
    assert Vectors.HASH_2 == wallet.hash()
    assert Vectors.DEFAULT_2_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_2_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_2_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_from_index():  # 11
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key()
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()

    wallet.clean_derivation()
    wallet.from_index(index=1129)
    wallet.from_index(index=0)
    wallet.from_index(index=0)
    wallet.from_index(index=1)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_2 == wallet.uncompressed()
    assert Vectors.COMPRESSED_2 == wallet.compressed()
    assert Vectors.CHAIN_CODE_2 == wallet.chain_code()
    assert Vectors.PRIVATE_2_KEY == wallet.private_key()
    assert Vectors.PUBLIC_2_KEY == wallet.public_key()
    assert Vectors.WIF_2_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_2 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_2 == wallet.path()
    assert Vectors.HASH_2 == wallet.hash()
    assert Vectors.DEFAULT_2_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_2_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_2_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_wallet_with_passphrase():  # 12
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY, passphrase=Vectors.PASSPHRASE)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert Vectors.PASSPHRASE is wallet.passphrase()
    assert Vectors.SEED_PASSPHRASE == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY_PASSPHRASE == wallet.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY_PASSPHRASE == wallet.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_PASSPHRASE == wallet.uncompressed()
    assert Vectors.COMPRESSED_PASSPHRASE == wallet.compressed()
    assert Vectors.CHAIN_CODE_PASSPHRASE == wallet.chain_code()
    assert Vectors.PRIVATE_PASSPHRASE_KEY == wallet.private_key()
    assert Vectors.PUBLIC_PASSPHRASE_KEY == wallet.public_key()
    assert Vectors.WIF_PASSPHRASE_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_PASSPHRASE == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_PASSPHRASE == wallet.hash()
    assert Vectors.DEFAULT_PASSPHRASE_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_PASSPHRASE_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_PASSPHRASE_ADDRESS == wallet.legacy_address()


@pytest.mark.hdwallet
def test_wallet_encrypt():  # 13
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY)

    filename = Vectors.FILENAME + ".dp"

    wallet.from_path("m/1127/0/0/0")
    assert len(Vectors.ENCRYPTED_1) == len(wallet.encrypt(passphrase=Vectors.PASSPHRASE, filename=filename))

    wallet.from_path("m/1127/0/0/1")
    assert len(Vectors.ENCRYPTED_2) == len(wallet.encrypt(passphrase=Vectors.PASSPHRASE, filename=filename))


@pytest.mark.hdwallet
def test_wallet_decrypt():  # 14
    filename = Vectors.FILENAME + ".dp"

    wallet2 = Wallet.decrypt(Vectors.PASSPHRASE, filename=filename)
    assert Vectors.CRYPTOCURRENCY == wallet2.cryptocurrency()
    assert Vectors.SYMBOL == wallet2.symbol()
    assert Vectors.NETWORK == wallet2.network()
    assert Vectors.STRENGHT == wallet2.strength()
    assert Vectors.ENTROPY == wallet2.entropy()
    assert Vectors.MNEMONIC == wallet2.mnemonic()
    assert Vectors.LANGUAGE == wallet2.language()
    assert None is wallet2.passphrase()
    assert Vectors.SEED == wallet2.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet2.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY == wallet2.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_1 == wallet2.uncompressed()
    assert Vectors.COMPRESSED_1 == wallet2.compressed()
    assert Vectors.CHAIN_CODE_1 == wallet2.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet2.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet2.public_key()
    assert Vectors.WIF_1_KEY == wallet2.wif()
    assert Vectors.FINGER_PRINT_1 == wallet2.finger_print()
    assert Vectors.SEMANTIC == wallet2.semantic()
    assert Vectors.PATH_1 == wallet2.path()
    assert Vectors.HASH_1 == wallet2.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet2.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet2.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet2.legacy_address()

    wallet_passphrase = Wallet.decrypt(Vectors.PASSPHRASE, data=Vectors.ENCRYPTED_PASSPHRASE)
    assert Vectors.CRYPTOCURRENCY == wallet_passphrase.cryptocurrency()
    assert Vectors.SYMBOL == wallet_passphrase.symbol()
    assert Vectors.NETWORK == wallet_passphrase.network()
    assert Vectors.STRENGHT == wallet_passphrase.strength()
    assert Vectors.ENTROPY == wallet_passphrase.entropy()
    assert Vectors.MNEMONIC == wallet_passphrase.mnemonic()
    assert Vectors.LANGUAGE == wallet_passphrase.language()
    assert Vectors.PASSPHRASE == wallet_passphrase.passphrase()
    assert Vectors.SEED_PASSPHRASE == wallet_passphrase.seed()
    assert Vectors.ROOT_xPRIVATE_KEY_PASSPHRASE == wallet_passphrase.root_xprivate_key()
    assert Vectors.ROOT_xPUBLIC_KEY_PASSPHRASE == wallet_passphrase.root_xpublic_key()
    assert Vectors.UNCOMPRESSED_PASSPHRASE == wallet_passphrase.uncompressed()
    assert Vectors.COMPRESSED_PASSPHRASE == wallet_passphrase.compressed()
    assert Vectors.CHAIN_CODE_PASSPHRASE == wallet_passphrase.chain_code()
    assert Vectors.PRIVATE_PASSPHRASE_KEY == wallet_passphrase.private_key()
    assert Vectors.PUBLIC_PASSPHRASE_KEY == wallet_passphrase.public_key()
    assert Vectors.WIF_PASSPHRASE_KEY == wallet_passphrase.wif()
    assert Vectors.FINGER_PRINT_PASSPHRASE == wallet_passphrase.finger_print()
    assert Vectors.SEMANTIC == wallet_passphrase.semantic()
    assert Vectors.PATH_1 == wallet_passphrase.path()
    assert Vectors.HASH_PASSPHRASE == wallet_passphrase.hash()
    assert Vectors.DEFAULT_PASSPHRASE_ADDRESS == wallet_passphrase.default_address()
    assert Vectors.BECH32_PASSPHRASE_ADDRESS == wallet_passphrase.bech32_address()
    assert Vectors.LEGACY_PASSPHRASE_ADDRESS == wallet_passphrase.legacy_address()


@pytest.mark.hdwallet
def test_query_all_correct_data():  # 15
    wallet = Wallet(network=DefichainMainnet)
    wallet.from_entropy(entropy=Vectors.ENTROPY)

    assert Vectors.CRYPTOCURRENCY == wallet.cryptocurrency()
    assert Vectors.SYMBOL == wallet.symbol()
    assert Vectors.NETWORK == wallet.network()
    assert Vectors.STRENGHT == wallet.strength()
    assert Vectors.ENTROPY == wallet.entropy()
    assert Vectors.MNEMONIC == wallet.mnemonic()
    assert Vectors.LANGUAGE == wallet.language()
    assert None is wallet.passphrase()
    assert Vectors.SEED == wallet.seed()
    assert Vectors.ROOT_xPRIVATE_KEY == wallet.root_xprivate_key(encoded=True)
    assert Vectors.ROOT_xPUBLIC_KEY == wallet.root_xpublic_key(encoded=True)
    assert Vectors.UNCOMPRESSED_1 == wallet.uncompressed(compressed=wallet.compressed())
    assert Vectors.COMPRESSED_1 == wallet.compressed(uncompressed=wallet.uncompressed())
    assert Vectors.CHAIN_CODE_1 == wallet.chain_code()
    assert Vectors.PRIVATE_1_KEY == wallet.private_key()
    assert Vectors.PUBLIC_1_KEY == wallet.public_key(compressed=True, private_key=wallet.private_key())
    assert Vectors.WIF_1_KEY == wallet.wif()
    assert Vectors.FINGER_PRINT_1 == wallet.finger_print()
    assert Vectors.SEMANTIC == wallet.semantic()
    assert Vectors.PATH_1 == wallet.path()
    assert Vectors.HASH_1 == wallet.hash()
    assert Vectors.DEFAULT_1_ADDRESS == wallet.default_address()
    assert Vectors.BECH32_1_ADDRESS == wallet.bech32_address()
    assert Vectors.LEGACY_1_ADDRESS == wallet.legacy_address()
