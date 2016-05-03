# CMSC 127 Final Project

##Requirements
* Python 2.7.11
* Django 1.9.5
* PostgreSQL 9.5
* Psycopg2 2.6.1

###Beta University Annual Funds

###General Description
The Development Office of Beta University seeks to obtain donations for its Annual Fund from a variety of donors. The fund collects over ten million dollars each year. Donors include graduating seniors, alumni, parents, faculty, administrators, staff, corporations, or other friends of the university. There are approximately 100,000 potential donors. The Annual Fund is directed by Suzanne Hayes, who is responsible for raising funds and keeping track of donations. Suzanne wishes to create a database to help with both of these major responsibilities.

###Basic Operations
Suzanne tries to raise funds in several ways during each fiscal year, which extends from July 1 to June 30. Each fall, all potential donors to the Annual Fund receive personalized letters from her, emphasizing their close ties to Beta University. The letters contain reply envelopes and forms on which the donors can fill in the amount they are pledging to contribute that year, and the method of payment they choose. Payment can be sent as a single check in the envelope, donors can choose deferred payments over a period of a year, or they can provide their credit card numbers to pay in a single lump sum. Often, the employer of the donor or of the donor’s spouse has a program to make a matching gift to the university, and the donor provides the contact information on the envelope. A letter acknowledging the gift and thanking the donor is sent as soon as the pledge is received. Suzanne is responsible for following up with the employer to collect the matching gift, which is paid in a single lump sum by the corporation. 
Several fundraising events are held during the year. Suzanne solicits donations at a fall carnival, a holiday dinner dance, and a spring golf outing, among other events. Each class has a class coordinator who helps by contacting members of his or her graduating class. An additional letter from the class coordinator is made to ask for larger donations from reunion classes, those who are marking an important anniversary of graduation – whether five years, ten years, etc. – prior to their reunion celebration weekend. Each spring there is a phonothon during which current students and other volunteers call other potential donors and solicit pledges. All alumni who have not contributed by the end of May receive telephone calls from their class coordinator asking them for a donation. If the class coordinator is unable to contact his or her classmates, Suzanne or a volunteer makes these calls instead. 
The donations are categorized by the group they are from, by the year of the donor (if applicable) and by size. There are ten “donor circles”, which are categorized by the size of the gift – President’s Circle for gifts over $50,000, Platinum Circle for gifts over $25,000, and so on. Gifts under $100 are not listed as belonging to a circle. An annual report listing all donors by category, year and donor circle is published and mailed to all actual and potential donors during the summer. The report does not list the actual amount each person contributed.

###Information Needs
At present, Suzanne has a mailing list on a word processor that is used to generate labels and letters to potential donors. She would like to be able to personalize the letter further by adding a reminder of the amount of money the donor gave the previous year. A spreadsheet is used to keep track of pledges and donations. Large pledges from individual donors are ordinarily paid in monthly installments rather than in one payment, but currently there is no way to keep track of those payments. When a database is developed, Suzanne would like to be able to send reminders if payments are over a month late. 
An Annual Fund Gift form is sent with all letters soliciting funds, with blanks for the donor to fill in the applicable information, as follows:
Beta University Annual Fund Gift Donor Name, Donor Address, Category (a check list specifying senior, alumnus/alumna, parent, administrator, etc.), Year of Graduation, Date of Pledge/Gift, Amount Pledged, Amount Enclosed, Payment Method, Number of Payments Chosen, Credit Card Number, Matching Corporation Name, Matching Corporation Address, Name of Spouse (if matching gift is from spouse’s employer).
When pledges are received by class representatives or during the phonothon, the same information is collected on similar forms.

###Reports needed include

#####Annual Report to Donors 

This report was described previously. It lists names only, not amounts. However, the names have to be categorized as indicated. The report also includes summaries, including the total amount raised from all sources, the total for each class, the percent participation for each class, the total for each category, the grand total for each donor circle, and the class total for each donor circle. It is an important fundraising tool for the following year’s drive, since it is mailed to each potential donor.

#####Monthly Report 

This is an internal report that Suzanne uses to evaluate the progress of the fundraising for the year so far. It gives the totals and percentages of pledges and gifts received for the current month in all categories.

#####Payments Due Report 

Suzanne would like a report each month listing the pledge payments that were due that month but were not received. It should list the donor’s name and address, the amount due, the date due, the amount of the pledge, the amount received so far, and the date of the previous payment, if any.

#####Event Report 

Suzanne would like to generate reports showing who attends each of the fundraising events, and what pledges and gifts were received from the attendees.

#####Class Representative Contact List 

For each class representative, Suzanne would like a list of classmates to be contacted, including the name, address, telephone number, last year’s donation information, and this year’s donation information.

#####Phonothon Volunteer Contact List 

Each volunteer caller is given a list with information about the potential donors he or she is expected to call, including the name, telephone number, address, category, year (if applicable), and last year’s donation information.

In addition to the forms and reports listed here, there are several others that would be useful. 
