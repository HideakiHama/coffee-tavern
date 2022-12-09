import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useState } from "react";
import { useToken } from './useToken';
import { useNavigate } from "react-router-dom";

const theme = createTheme();

export default function SignUp() {
  const [token, login, logout, signup] = useToken();
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");
  const navigate = useNavigate();



  const handleSubmit = async(event) => {
    event.preventDefault();
    // const data = new FormData(event.currentTarget);
    // console.log(data.get("firstName"), data.get("email"), data.get("password"), data.get("role"))
    console.log(password, email, username, role)
    signup(password, email, username, role);
    
    if (role === "Employee") {
      navigate("/user/employee/info-form/create");
    } else if (role === "Employer") {
      navigate("/user/employer/info-form/create");
    }
  };

  const roles = ["Employee", "Employer"]
  const handleCheckEmployee = (event) => {
    if (event.target.checked) {
      setRole(roles[0])
    }
  }

  const handleCheckEmployer = (event) => {
    if (event.target.checked) {
      setRole(roles[1])
    }
  }

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
              <Grid container spacing={2}>
              <Grid item xs={12} sm={12}>
                <TextField
                  autoComplete="given-name"
                  name="firstName"
                  required
                  fullWidth
                  id="firstName"
                  label="User Name"
                  autoFocus
                  value={username}
                  onChange={(event => setUserName(event.target.value))}
                />
              </Grid>
              <Grid item xs={12} >
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                  value={email}
                  onChange={(event => setEmail(event.target.value))}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                  value={password}
                  onChange={(event => setPassword(event.target.value))}
                />
              </Grid>
              <Grid item xs={12}>
                <FormControlLabel onChange={handleCheckEmployee}
                  control={<Checkbox value="" id="Employee" color="primary" />}
                  label="Employee"
                />
                <FormControlLabel onChange={handleCheckEmployer}
                  control={<Checkbox value="" id="Employer" color="primary" />}
                  label="Employer"
                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="http://localhost:3000/token" variant="body2">
                  Already have an account? Sign in
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
