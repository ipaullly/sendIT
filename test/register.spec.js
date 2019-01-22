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

describe('registration', () => {
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


afterAll(() => {
    browser.close();
});
