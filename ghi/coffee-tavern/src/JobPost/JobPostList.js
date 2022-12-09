import * as React from 'react';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import {useState, useEffect} from "react"
// import { useNavigate } from 'react-router';
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';
import { useAuthContext } from '../useToken';

const theme = createTheme();

export default function JobPostList() {
  const [jobForm, setJobForm] = useState([]);
  const [ searchInput, setSearchInput ] = useState("");
  const { token } = useAuthContext();

  useEffect(() => {
    const getJobForm = async () => {
      if (token) {
      const response = await fetch(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/get_all_form`,  {
        method: "GET",
        headers: { Authorization: `Bearer ${token}`,
      },
    });
      const data = await response.json();
      setJobForm(data)
      console.log(data.account_id)

  }
  }
    getJobForm()
}, [token])


  const sendInfo = async (employer_id) => {
      const response = await fetch(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/apply/${employer_id}`,  {
        method: "POST",
        headers: { Authorization: `Bearer ${token}`,
      },
    });
    const data = await response.json();
  }


  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <main>
      {/* <div style={{backgroundImage: `URL(https://www.setaswall.com/wp-content/uploads/2017/07/Coffee-Background-45-2560x1600-768x480.jpg)`}}>
        Hello World
      </div> */}
        {/* Hero unit */}
        <Container sx={{ py: 8 }} maxWidth="md">
        <input type="text" placeholder="Search here" onChange={(event) => setSearchInput(event.target.value)} value={searchInput} label="Search" />
          {/* End hero unit */}
          <Grid container spacing={4}>
            {jobForm.filter(app => {
              console.log("APP", app)
                        if (searchInput === "") {
                            return app
                        } else if (app.employer.includes(searchInput)) {
                            return app
                        }
                    }).map((jobForms) => (
              <Grid item  xs={12} sm={6} md={4} key={jobForms.id}>
                  <Card
                  sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                  <CardContent sx={{ flexGrow: 1 }}>
                    <Typography gutterBottom variant="h5" component="h2">
                      Employer: {jobForms.employer}
                    </Typography>
                    <Typography>
                      position: {jobForms.position}
                    </Typography>
                    <Typography>
                      description: {jobForms.description}
                    </Typography>
                  </CardContent>
                  {/* <CardActions> */}
                    <Button size="small" onClick={(e) => sendInfo(jobForms.account_id)}>Send Info</Button>
                  {/* </CardActions> */}
                </Card>
              </Grid>
                ))}
          </Grid>
        </Container>
      </main>
      {/* Footer */}
      {/* <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
        <Typography variant="h6" align="center" gutterBottom>
          Footer
        </Typography>
        <Typography
          variant="subtitle1"
          align="center"
          color="text.secondary"
          component="p"
        >
          Something here to give the footer a purpose!
        </Typography>
      </Box> */}
      {/* End footer */}
    </ThemeProvider>
  );
}
