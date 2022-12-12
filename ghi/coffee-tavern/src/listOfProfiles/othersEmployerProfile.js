import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
// import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useAuthContext } from '../useToken';
import {useEffect, useState} from 'react';
import { useLocation } from "react-router-dom";
import axios from "axios";


const theme = createTheme();

function OthersEmployerProfile(){
  // set state name, email, etc

  const [otherEmployer, setOtherEmployer] = useState([])
  const { token } = useAuthContext();
  const IdData = useLocation();
  const account_id = IdData.state.account_id


  useEffect(() => {
    const getOthersEmployerInfo = async () => {
      if (token) {
        const id = account_id
        const response = await axios.get(`${process.env.REACT_APP_TAGS_API_HOST}/users/${id}/get_employer_info`,
        {headers: { Authorization: `Bearer ${token}`}});
        setOtherEmployer(response.data)
}};
    getOthersEmployerInfo();
  }, [token, account_id]);

  return (
    <ThemeProvider theme={theme}>
      <Grid container component="main" sx={{ height: '100vh' }}>
        <CssBaseline />
        <Grid
          item
          xs={false}
          sm={4}
          md={7}
          sx={{
            backgroundImage: `url(${otherEmployer.pic_url})`,
            backgroundRepeat: 'no-repeat',
            backgroundColor: (t) =>
              t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        />
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
          <Box
            sx={{
              my: 8,
              mx: 4,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            <Typography component="h1" variant="h2">
              <ul>
                <li>{otherEmployer.company_name}</li>
              </ul>
            </Typography>
            <Typography componenet="h6" variant="h4">
              <ul>
                <li>{otherEmployer.job_type}</li>
                <li>{otherEmployer.location}</li>
                <li>{otherEmployer.about}</li>
              </ul>
            </Typography>
          </Box>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

export default OthersEmployerProfile;