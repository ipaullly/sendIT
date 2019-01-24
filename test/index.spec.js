import puppeteer from "puppeteer";

const localUrlBase = 'http://127.0.0.1:8080';
const routes = {
    public: {
        register: `${localUrlBase}/register_page`,
        login: `${localUrlBase}/login`
    },
    user: {
        userPage: `${localUrlBase}/orders_display_users`,
        singleOrderPage: `${localUrlBase}/order_display_page`
    },
    admin: {
        adminPage: `${localUrlBase}/orders_display_admin`
    }
};

const user = {
    email: 'paul@hotmail.com',
    emailFail: 'paulhotmail.com',
    password: 'Tykenyke',
    passwordFail: 'tykenyke'
};
const admin = {
    email: 'Davidtroy@sendIT.org',
    password: 'Tykenyke'
};

let browser;
let page;

beforeAll(async () => {
    browser = await puppeteer.launch();
    page = await browser.newPage();
});

describe('Registration', () => {
    test('generation of response', async () => {
        await page.goto(routes.public.register)
        await page.waitForSelector('[data-testid="registerForm"]')
        await page.click('[data-testid="emailInput"]')
        await page.type('[data-testid="emailInput"]', user.email)
        await page.click('[data-testid="passwordInput"]')
        await page.type('[data-testid="passwordInput"]', user.password)
        await page.click('[data-testid="registerSubmitButton"]')
        await page.waitForSelector('[data-testid="responseBox"]')
    });
    test('duplicate email response message', async () => {
        await page.type('[data-testid="emailInput"]', user.emailFail)
        await page.click('[data-testid="passwordInput"]')
        await page.type('[data-testid="passwordInput"]', user.passwordFail)
        await page.click('[data-testid="registerSubmitButton"]')
        await page.waitForSelector('[data-testid="responseBox"]')
        const duplicateEmail = await page.$eval('[data-testid="responseBox"]', el => el.textContent)
        expect(duplicateEmail).toEqual("User with the email already exists")
    });
    test('wrong email format message', async () => {
        await page.goto(routes.public.register)
        await page.waitForSelector('[data-testid="registerForm"]')
        await page.click('[data-testid="emailInput"]')
        await page.type('[data-testid="emailInput"]', user.emailFail)
        await page.click('[data-testid="passwordInput"]')
        await page.type('[data-testid="passwordInput"]', user.password)
        await page.click('[data-testid="registerSubmitButton"]')
        await page.waitForSelector('[data-testid="responseBox"]')
        const wrongEmailFormat = await page.$eval('[data-testid="responseBox"]', el => el.textContent)
        expect(wrongEmailFormat).toEqual("Invalid email format")
    });
});

describe('Login', () => {
    test('throws error message for invalid email format', async () => {
        await page.goto(routes.public.login)
        await page.waitForSelector('[data-testid="logInForm"]')
        await page.click('[data-testid="logInEmailInput"]')
        await page.type('[data-testid="logInEmailInput"]', user.emailFail)
        await page.click('[data-testid="logInPasswordInput"]')
        await page.type('[data-testid="logInPasswordInput"]', user.password)
        await page.click('[data-testid="loginSubmitButton"]')
        await page.waitForSelector('[data-testid="logInResponseBox"]')
        const errorMessage = await page.$eval('[data-testid="logInResponseBox"]', el => el.textContent)
        expect(errorMessage).toEqual("Invalid email. please check the format")
    });
    test('throws error message for wrong login credentials', async () => {
        await page.goto(routes.public.login)
        await page.waitForSelector('[data-testid="logInForm"]')
        await page.click('[data-testid="logInEmailInput"]')
        await page.type('[data-testid="logInEmailInput"]', user.email)
        await page.click('[data-testid="logInPasswordInput"]')
        await page.type('[data-testid="logInPasswordInput"]', '  ')
        await page.click('[data-testid="loginSubmitButton"]')
        await page.waitForSelector('[data-testid="logInResponseBox"]')
        const errorMessage = await page.$eval('[data-testid="logInResponseBox"]', el => el.textContent)
        expect(errorMessage).toEqual("incorrect login credentials. please enter details again")
    });
    test('successful login triggers a redirect to user account', async () => {
        await page.goto(routes.public.login)
        await page.waitForSelector('[data-testid="logInForm"]')
        await page.click('[data-testid="logInEmailInput"]')
        await page.type('[data-testid="logInEmailInput"]', user.email)
        await page.click('[data-testid="logInPasswordInput"]')
        await page.type('[data-testid="logInPasswordInput"]', user.password)
        await page.click('[data-testid="loginSubmitButton"]')
        await page.waitForNavigation({waitUntil: "networkidle2"})
        await page.waitForSelector('[data-testid="logInRedirectResponse"]')
        const duplicateEmail = await page.$eval('[data-testid="logInRedirectResponse"]', el => el.textContent)
        expect(duplicateEmail).toEqual("Successfully logged in")  
    });
    test('successful login triggers a redirect to admin account', async () => {
        await page.goto(routes.public.login)
        await page.waitForSelector('[data-testid="logInForm"]')
        await page.click('[data-testid="logInEmailInput"]')
        await page.type('[data-testid="logInEmailInput"]', admin.email)
        await page.click('[data-testid="logInPasswordInput"]')
        await page.type('[data-testid="logInPasswordInput"]', admin.password)
        await page.click('[data-testid="loginSubmitButton"]')
        await page.waitForNavigation({waitUntil: "networkidle2"})
        await page.waitForSelector('[data-testid="allOrdersAdmin"]')
        const duplicateEmail = await page.$eval('[data-testid="allOrdersAdmin"]', el => el.textContent)
        expect(duplicateEmail).toEqual("View all Orders")  
    });
});

describe('User interactions', () => {
    test('assert user can view all orders they make', async () => {
        await page.goto(routes.public.login)
        await page.waitForSelector('[data-testid="logInForm"]')
        await page.click('[data-testid="logInEmailInput"]')
        await page.type('[data-testid="logInEmailInput"]', user.email)
        await page.click('[data-testid="logInPasswordInput"]')
        await page.type('[data-testid="logInPasswordInput"]', user.password)
        await page.click('[data-testid="loginSubmitButton"]')
        await page.waitForNavigation({waitUntil: "networkidle2"})
        await page.waitForSelector('[data-testid="viewUserOrderButton"]')
        await page.click('[data-testid="viewUserOrderButton"]')
        await page.waitForSelector('[data-testid="generatedUserOrders"]')        
    });
});

afterAll(async (done) => {
    browser.close();
    done();
});
