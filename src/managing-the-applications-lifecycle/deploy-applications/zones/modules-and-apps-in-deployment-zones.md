---
summary: Frequently asked questions about modules of the same app on different deployment zones and the changes introduced in Platform Server 11.8.0.
---

# Modules and apps in deployment zones
From the release of Platform Server 11.8.0 only complete applications can be configured for different deployment zones. Mixed-mode configurations—different deployment zones for individual modules of the same app—is deprecated. 

<div class="info" markdown="1">

While existing applications with modules in different deployment zones are still supported, OutSystems will stop supporting this option in the future. We strongly suggest unifying applications’ modules under the same deployment zone. The recommended option is to select a deployment zone for the whole application, which will modify the deployment zone for each of its modules. In case some modules need to stay in a separate deployment zone, you will need to create extra applications. Please follow one of the two unification approaches described below.

</div>

**After upgrading the Platform Server what will be the behavior of my apps with modules configured for different modes?**
 
Nothing changes. Mixed-mode apps will keep their current configurations untouched at the module level.

**Can modules in a mixed-mode scenario be changed?**

Modules in mixed-mode scenarios can be changed, just as any other module. All module-level operations are still available. They can also be moved to other deployment zones.

**Can new modules be added to mixed-mode apps?**

New modules can be added to mixed-mode apps. New modules will be created on the [default deployment zone](intro.md) for that environment. Just like other modules in a mixed-mode application, they can be changed to another deployment zone.

**What about new apps?**

It will not be possible to define mixed-mode scenarios for new apps. The configuration of deployment zones for new apps applies only to the whole app.

**What happens if we configure a deployment zone for an application with modules in different deployment zones?**

The deployment zone configurations at module level will be deleted and the application-level configuration will be used.

## Unification approaches
### Application unification
If you are able to have all the modules of this application residing under the same deployment zone, your best option might be to set it at application configuration level. This will overwrite the deployment zones for all your modules.

To do this, go to Service Center:
1. Select the application that you want to unify zones for
2. Go to Operation tab
3. Select the desired Deployment Zone from the dropdown menu
4. Click Save
5. Click Publish to republish your application with the new changes

 
### Application split
If you need to keep these modules in separate deployment zones, you will need to group them under different applications - one per deployment zone. Then move your modules under those applications accordingly. The current application should be used for the deployment zone hosting the bigger number of modules at the moment.

To do this, open Service Studio:
1. Create as many applications as zones you need for the current application
2. Open the existing application
3. Move your modules to the newly created applications
4. Then assign the applications’ deployment zones following the steps described for the unification approach
5. Stage all the new applications all the way through to Production environment
