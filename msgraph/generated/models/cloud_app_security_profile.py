from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_permissions_required = lazy_import('msgraph.generated.models.application_permissions_required')
entity = lazy_import('msgraph.generated.models.entity')
security_vendor_information = lazy_import('msgraph.generated.models.security_vendor_information')

class CloudAppSecurityProfile(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
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
        Instantiates a new cloudAppSecurityProfile and sets the default values.
        """
        super().__init__()
        # The azureSubscriptionId property
        self._azure_subscription_id: Optional[str] = None
        # The azureTenantId property
        self._azure_tenant_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The deploymentPackageUrl property
        self._deployment_package_url: Optional[str] = None
        # The destinationServiceName property
        self._destination_service_name: Optional[str] = None
        # The isSigned property
        self._is_signed: Optional[bool] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The manifest property
        self._manifest: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The permissionsRequired property
        self._permissions_required: Optional[application_permissions_required.ApplicationPermissionsRequired] = None
        # The platform property
        self._platform: Optional[str] = None
        # The policyName property
        self._policy_name: Optional[str] = None
        # The publisher property
        self._publisher: Optional[str] = None
        # The riskScore property
        self._risk_score: Optional[str] = None
        # The tags property
        self._tags: Optional[List[str]] = None
        # The type property
        self._type: Optional[str] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudAppSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudAppSecurityProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudAppSecurityProfile()
    
    @property
    def deployment_package_url(self,) -> Optional[str]:
        """
        Gets the deploymentPackageUrl property value. The deploymentPackageUrl property
        Returns: Optional[str]
        """
        return self._deployment_package_url
    
    @deployment_package_url.setter
    def deployment_package_url(self,value: Optional[str] = None) -> None:
        """
        Sets the deploymentPackageUrl property value. The deploymentPackageUrl property
        Args:
            value: Value to set for the deploymentPackageUrl property.
        """
        self._deployment_package_url = value
    
    @property
    def destination_service_name(self,) -> Optional[str]:
        """
        Gets the destinationServiceName property value. The destinationServiceName property
        Returns: Optional[str]
        """
        return self._destination_service_name
    
    @destination_service_name.setter
    def destination_service_name(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationServiceName property value. The destinationServiceName property
        Args:
            value: Value to set for the destinationServiceName property.
        """
        self._destination_service_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_subscription_id": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployment_package_url": lambda n : setattr(self, 'deployment_package_url', n.get_str_value()),
            "destination_service_name": lambda n : setattr(self, 'destination_service_name', n.get_str_value()),
            "is_signed": lambda n : setattr(self, 'is_signed', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "manifest": lambda n : setattr(self, 'manifest', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "permissions_required": lambda n : setattr(self, 'permissions_required', n.get_enum_value(application_permissions_required.ApplicationPermissionsRequired)),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "policy_name": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_signed(self,) -> Optional[bool]:
        """
        Gets the isSigned property value. The isSigned property
        Returns: Optional[bool]
        """
        return self._is_signed
    
    @is_signed.setter
    def is_signed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSigned property value. The isSigned property
        Args:
            value: Value to set for the isSigned property.
        """
        self._is_signed = value
    
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
    def manifest(self,) -> Optional[str]:
        """
        Gets the manifest property value. The manifest property
        Returns: Optional[str]
        """
        return self._manifest
    
    @manifest.setter
    def manifest(self,value: Optional[str] = None) -> None:
        """
        Sets the manifest property value. The manifest property
        Args:
            value: Value to set for the manifest property.
        """
        self._manifest = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def permissions_required(self,) -> Optional[application_permissions_required.ApplicationPermissionsRequired]:
        """
        Gets the permissionsRequired property value. The permissionsRequired property
        Returns: Optional[application_permissions_required.ApplicationPermissionsRequired]
        """
        return self._permissions_required
    
    @permissions_required.setter
    def permissions_required(self,value: Optional[application_permissions_required.ApplicationPermissionsRequired] = None) -> None:
        """
        Sets the permissionsRequired property value. The permissionsRequired property
        Args:
            value: Value to set for the permissionsRequired property.
        """
        self._permissions_required = value
    
    @property
    def platform(self,) -> Optional[str]:
        """
        Gets the platform property value. The platform property
        Returns: Optional[str]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[str] = None) -> None:
        """
        Sets the platform property value. The platform property
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def policy_name(self,) -> Optional[str]:
        """
        Gets the policyName property value. The policyName property
        Returns: Optional[str]
        """
        return self._policy_name
    
    @policy_name.setter
    def policy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the policyName property value. The policyName property
        Args:
            value: Value to set for the policyName property.
        """
        self._policy_name = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The publisher property
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The publisher property
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
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
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deploymentPackageUrl", self.deployment_package_url)
        writer.write_str_value("destinationServiceName", self.destination_service_name)
        writer.write_bool_value("isSigned", self.is_signed)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("manifest", self.manifest)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("permissionsRequired", self.permissions_required)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_str_value("publisher", self.publisher)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("type", self.type)
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
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
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
    

