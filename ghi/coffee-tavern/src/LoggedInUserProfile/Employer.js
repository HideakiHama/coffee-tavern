import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useAuthContext } from '../useToken';
import {useEffect, useState} from 'react';
import jwt_decode from 'jwt-decode';

const theme = createTheme();

const EmployerProfile = ({id}) => {

  const [name, setName] = useState('');
  const [job, setJob] = useState('');
  const [location, setLocation] = useState('');
  const [about, setAbout] = useState('');
  const [pic, setPic] = useState('')

  const { token } = useAuthContext();

  useEffect(() => {
    async function getEmployerInfo() {

      const decoded = jwt_decode(token)
      const id = decoded.account["id"]

      const employerURL = `http://localhost:8000/users/${id}/get_employer_info`;
  
      const employerResponse = await fetch(employerURL, {
        method: "GET",
        headers: { Authorization: `Bearer ${token}`}
      });
  
      if (employerResponse.ok) {
        const info = await employerResponse.json();

        setName(info.company_name)
        setJob(info.job_type)
        setLocation(info.location)
        setAbout(info.about)
        setPic(info.pic_url)
      }
    }
    getEmployerInfo()
  }, [id, token])

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
            backgroundImage: `url(${pic})`,
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
                <li>{name}</li>
              </ul>
            </Typography>
            <Typography componenet="h6" variant="h4">
              <ul>
                <li>{job}</li>
                <li>{location}</li>
                <li>{about}</li>
              </ul>
            </Typography>
            <button className="btn waves-effect waves-light" type="submit" name="action">
              <a href="/user/employer/info-form">Edit Info</a>
            </button>
          </Box>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

export default EmployerProfile;