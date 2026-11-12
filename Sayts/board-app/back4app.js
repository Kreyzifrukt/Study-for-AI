//import AsyncStorage from "@react-native-async-storage/async-storage";
//import parse from "parse/react-native";
//Parse.setAsyncStorage(AsyncStorage);

import Parse from "parse";

Parse.initialize(
    'crBG924StNSeSiy1CJcwPjXVOlLOxs18msYJtglK',
    'Vup3g61qVKF4QY0QaahIK59ZGfRcWmBp3IZLTRxD'
);

Parse.serverURL = 'https://parseapi.back4app.com';

export default Parse;
