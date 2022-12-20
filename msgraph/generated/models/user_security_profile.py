from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
security_vendor_information = lazy_import('msgraph.generated.models.security_vendor_information')
user_account = lazy_import('msgraph.generated.models.user_account')

class UserSecurityProfile(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def accounts(self,) -> Optional[List[user_account.UserAccount]]:
        """
        Gets the accounts property value. The accounts property
        Returns: Optional[List[user_account.UserAccount]]
        """
        return self._accounts
    
    @accounts.setter
    def accounts(self,value: Optional[List[user_account.UserAccount]] = None) -> None:
        """
        Sets the accounts property value. The accounts property
        Args:
            value: Value to set for the accounts property.
        """
        self._accounts = value
    
    @property
    def azure_subscription_id(self,) -> Optional[str]:
        """
        Gets the azureSubscriptionId property value. The azureSubscriptionId property
        Returns: Optional[str]
        """
        return self._azure_subscription_id
    
    @azure_subscription_id.setter
    def azure_subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureSubscriptionId property value. The azureSubscriptionId property
        Args:
            value: Value to set for the azureSubscriptionId property.
        """
        self._azure_subscription_id = value
    
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. The azureTenantId property
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. The azureTenantId property
        Args:
            value: Value to set for the azureTenantId property.
        """
        self._azure_tenant_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userSecurityProfile and sets the default values.
        """
        super().__init__()
        # The accounts property
        self._accounts: Optional[List[user_account.UserAccount]] = None
        # The azureSubscriptionId property
        self._azure_subscription_id: Optional[str] = None
        # The azureTenantId property
        self._azure_tenant_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The riskScore property
        self._risk_score: Optional[str] = None
        # The tags property
        self._tags: Optional[List[str]] = None
        # The userPrincipalName property
        self._user_principal_name: Optional[str] = None
        # The vendorInformation property
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSecurityProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSecurityProfile()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accounts": lambda n : setattr(self, 'accounts', n.get_collection_of_object_values(user_account.UserAccount)),
            "azure_subscription_id": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def risk_score(self,) -> Optional[str]:
        """
        Gets the riskScore property value. The riskScore property
        Returns: Optional[str]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[str] = None) -> None:
        """
        Sets the riskScore property value. The riskScore property
        Args:
            value: Value to set for the riskScore property.
        """
        self._risk_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accounts", self.accounts)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_object_value("vendorInformation", self.vendor_information)
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. The tags property
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. The tags property
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The userPrincipalName property
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The userPrincipalName property
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def vendor_information(self,) -> Optional[security_vendor_information.SecurityVendorInformation]:
        """
        Gets the vendorInformation property value. The vendorInformation property
        Returns: Optional[security_vendor_information.SecurityVendorInformation]
        """
        return self._vendor_information
    
    @vendor_information.setter
    def vendor_information(self,value: Optional[security_vendor_information.SecurityVendorInformation] = None) -> None:
        """
        Sets the vendorInformation property value. The vendorInformation property
        Args:
            value: Value to set for the vendorInformation property.
        """
        self._vendor_information = value
    

