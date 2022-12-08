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

const EmployeeProfile = () => {

  const [name, setName] = useState('');
  const [career, setCareer] = useState('');
  const [location, setLocation] = useState('');
  const [education, setEducation] = useState('');
  const [about, setAbout] = useState('');
  const [pic, setPic] = useState('')

  const { token } = useAuthContext();

  useEffect(() => {
    async function getEmployeeInfo() {
        
      const decoded = jwt_decode(token)
      const id = decoded.account["id"]

      const employeeURL = `http://localhost:8000/users/${id}/get_employee_info`;

      const employeeResponse = await fetch(employeeURL, {
        method: "GET",
        headers: { Authorization: `Bearer ${token}`}
      });
      console.log("hello")
      if (employeeResponse.ok) {
        const info = await employeeResponse.json();
        
        setName(info.full_name)
        setCareer(info.career_title)
        setLocation(info.location)
        setEducation(info.education)
        setAbout(info.about)
        setPic(info.pic_url)

        console.log(info.pic_url)
      }
    }
    getEmployeeInfo()
  }, [token])

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
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={24} square>
          <Box
            sx={{
              my: 10,
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
                <li>{career}</li>
                <li>{location}</li>
                <li>{education}</li>
                <li>{about}</li>
              </ul>
              {/* <img src={pic} alt="Profile Pic"/> */}
            </Typography>
            <a href="/user/employee/info-form">Edit Info</a>
          </Box>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

export default EmployeeProfile;