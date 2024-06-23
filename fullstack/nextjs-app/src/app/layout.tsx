import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { AppRouterCacheProvider } from '@mui/material-nextjs/v13-appRouter';
import { ThemeProvider } from '@mui/material/styles';
import theme from '../theme';
import { AppBar, Breadcrumbs } from "@mui/material"
import MenuDrawer from "./components/menudrawer"


 export default function RootLayout(props) {
   return (
     <html lang="en">
       <body>
        <AppRouterCacheProvider>
          <ThemeProvider theme={theme}>
            <AppBar>
              <MenuDrawer/>
              Demo App
            </AppBar>
            <Breadcrumbs></Breadcrumbs>
              {props.children}
          </ThemeProvider>
        </AppRouterCacheProvider>
       </body>
     </html>
   );
 }
