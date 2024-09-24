import globals from "globals";
import pluginJs from "@eslint/js";
import pluginReact, { rules } from "eslint-plugin-react";
import eslintPluginPrettier from "eslint-plugin-prettier";

export default [
  {files: ["**/*.{js,mjs,cjs,jsx}"]},
  {languageOptions: { globals: globals.browser }},
  rules["react-in-jsx-scope"],
  pluginJs.configs.recommended,
  pluginReact.configs.flat.recommended,
  eslintPluginPrettier.configs.recommended,
];