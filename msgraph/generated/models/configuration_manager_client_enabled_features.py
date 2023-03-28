from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ConfigurationManagerClientEnabledFeatures(AdditionalDataHolder, Parsable):
    """
    configuration Manager client enabled features
    """
    def __init__(self,) -> None:
        """
        Instantiates a new configurationManagerClientEnabledFeatures and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Whether compliance policy is managed by Intune
        self._compliance_policy: Optional[bool] = None
        # Whether device configuration is managed by Intune
        self._device_configuration: Optional[bool] = None
        # Whether Endpoint Protection is managed by Intune
        self._endpoint_protection: Optional[bool] = None
        # Whether inventory is managed by Intune
        self._inventory: Optional[bool] = None
        # Whether modern application is managed by Intune
        self._modern_apps: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Whether Office application is managed by Intune
        self._office_apps: Optional[bool] = None
        # Whether resource access is managed by Intune
        self._resource_access: Optional[bool] = None
        # Whether Windows Update for Business is managed by Intune
        self._windows_update_for_business: Optional[bool] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def compliance_policy(self,) -> Optional[bool]:
        """
        Gets the compliancePolicy property value. Whether compliance policy is managed by Intune
        Returns: Optional[bool]
        """
        return self._compliance_policy
    
    @compliance_policy.setter
    def compliance_policy(self,value: Optional[bool] = None) -> None:
        """
        Sets the compliancePolicy property value. Whether compliance policy is managed by Intune
        Args:
            value: Value to set for the compliance_policy property.
        """
        self._compliance_policy = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigurationManagerClientEnabledFeatures:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerClientEnabledFeatures
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConfigurationManagerClientEnabledFeatures()
    
    @property
    def device_configuration(self,) -> Optional[bool]:
        """
        Gets the deviceConfiguration property value. Whether device configuration is managed by Intune
        Returns: Optional[bool]
        """
        return self._device_configuration
    
    @device_configuration.setter
    def device_configuration(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceConfiguration property value. Whether device configuration is managed by Intune
        Args:
            value: Value to set for the device_configuration property.
        """
        self._device_configuration = value
    
    @property
    def endpoint_protection(self,) -> Optional[bool]:
        """
        Gets the endpointProtection property value. Whether Endpoint Protection is managed by Intune
        Returns: Optional[bool]
        """
        return self._endpoint_protection
    
    @endpoint_protection.setter
    def endpoint_protection(self,value: Optional[bool] = None) -> None:
        """
        Sets the endpointProtection property value. Whether Endpoint Protection is managed by Intune
        Args:
            value: Value to set for the endpoint_protection property.
        """
        self._endpoint_protection = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "compliancePolicy": lambda n : setattr(self, 'compliance_policy', n.get_bool_value()),
            "deviceConfiguration": lambda n : setattr(self, 'device_configuration', n.get_bool_value()),
            "endpointProtection": lambda n : setattr(self, 'endpoint_protection', n.get_bool_value()),
            "inventory": lambda n : setattr(self, 'inventory', n.get_bool_value()),
            "modernApps": lambda n : setattr(self, 'modern_apps', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "officeApps": lambda n : setattr(self, 'office_apps', n.get_bool_value()),
            "resourceAccess": lambda n : setattr(self, 'resource_access', n.get_bool_value()),
            "windowsUpdateForBusiness": lambda n : setattr(self, 'windows_update_for_business', n.get_bool_value()),
        }
        return fields
    
    @property
    def inventory(self,) -> Optional[bool]:
        """
        Gets the inventory property value. Whether inventory is managed by Intune
        Returns: Optional[bool]
        """
        return self._inventory
    
    @inventory.setter
    def inventory(self,value: Optional[bool] = None) -> None:
        """
        Sets the inventory property value. Whether inventory is managed by Intune
        Args:
            value: Value to set for the inventory property.
        """
        self._inventory = value
    
    @property
    def modern_apps(self,) -> Optional[bool]:
        """
        Gets the modernApps property value. Whether modern application is managed by Intune
        Returns: Optional[bool]
        """
        return self._modern_apps
    
    @modern_apps.setter
    def modern_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the modernApps property value. Whether modern application is managed by Intune
        Args:
            value: Value to set for the modern_apps property.
        """
        self._modern_apps = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def office_apps(self,) -> Optional[bool]:
        """
        Gets the officeApps property value. Whether Office application is managed by Intune
        Returns: Optional[bool]
        """
        return self._office_apps
    
    @office_apps.setter
    def office_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the officeApps property value. Whether Office application is managed by Intune
        Args:
            value: Value to set for the office_apps property.
        """
        self._office_apps = value
    
    @property
    def resource_access(self,) -> Optional[bool]:
        """
        Gets the resourceAccess property value. Whether resource access is managed by Intune
        Returns: Optional[bool]
        """
        return self._resource_access
    
    @resource_access.setter
    def resource_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the resourceAccess property value. Whether resource access is managed by Intune
        Args:
            value: Value to set for the resource_access property.
        """
        self._resource_access = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("compliancePolicy", self.compliance_policy)
        writer.write_bool_value("deviceConfiguration", self.device_configuration)
        writer.write_bool_value("endpointProtection", self.endpoint_protection)
        writer.write_bool_value("inventory", self.inventory)
        writer.write_bool_value("modernApps", self.modern_apps)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("officeApps", self.office_apps)
        writer.write_bool_value("resourceAccess", self.resource_access)
        writer.write_bool_value("windowsUpdateForBusiness", self.windows_update_for_business)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def windows_update_for_business(self,) -> Optional[bool]:
        """
        Gets the windowsUpdateForBusiness property value. Whether Windows Update for Business is managed by Intune
        Returns: Optional[bool]
        """
        return self._windows_update_for_business
    
    @windows_update_for_business.setter
    def windows_update_for_business(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsUpdateForBusiness property value. Whether Windows Update for Business is managed by Intune
        Args:
            value: Value to set for the windows_update_for_business property.
        """
        self._windows_update_for_business = value
    

