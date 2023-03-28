from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_filter

class ConditionalAccessClientApplications(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessClientApplications and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Service principal IDs excluded from the policy scope.
        self._exclude_service_principals: Optional[List[str]] = None
        # Service principal IDs included in the policy scope, or ServicePrincipalsInMyTenant.
        self._include_service_principals: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Filter that defines the dynamic-servicePrincipal-syntax rule to include/exclude service principals. A filter can use custom security attributes to include/exclude service principals.
        self._service_principal_filter: Optional[conditional_access_filter.ConditionalAccessFilter] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessClientApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessClientApplications
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessClientApplications()
    
    @property
    def exclude_service_principals(self,) -> Optional[List[str]]:
        """
        Gets the excludeServicePrincipals property value. Service principal IDs excluded from the policy scope.
        Returns: Optional[List[str]]
        """
        return self._exclude_service_principals
    
    @exclude_service_principals.setter
    def exclude_service_principals(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeServicePrincipals property value. Service principal IDs excluded from the policy scope.
        Args:
            value: Value to set for the exclude_service_principals property.
        """
        self._exclude_service_principals = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_filter

        fields: Dict[str, Callable[[Any], None]] = {
            "excludeServicePrincipals": lambda n : setattr(self, 'exclude_service_principals', n.get_collection_of_primitive_values(str)),
            "includeServicePrincipals": lambda n : setattr(self, 'include_service_principals', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "servicePrincipalFilter": lambda n : setattr(self, 'service_principal_filter', n.get_object_value(conditional_access_filter.ConditionalAccessFilter)),
        }
        return fields
    
    @property
    def include_service_principals(self,) -> Optional[List[str]]:
        """
        Gets the includeServicePrincipals property value. Service principal IDs included in the policy scope, or ServicePrincipalsInMyTenant.
        Returns: Optional[List[str]]
        """
        return self._include_service_principals
    
    @include_service_principals.setter
    def include_service_principals(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeServicePrincipals property value. Service principal IDs included in the policy scope, or ServicePrincipalsInMyTenant.
        Args:
            value: Value to set for the include_service_principals property.
        """
        self._include_service_principals = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("excludeServicePrincipals", self.exclude_service_principals)
        writer.write_collection_of_primitive_values("includeServicePrincipals", self.include_service_principals)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("servicePrincipalFilter", self.service_principal_filter)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_principal_filter(self,) -> Optional[conditional_access_filter.ConditionalAccessFilter]:
        """
        Gets the servicePrincipalFilter property value. Filter that defines the dynamic-servicePrincipal-syntax rule to include/exclude service principals. A filter can use custom security attributes to include/exclude service principals.
        Returns: Optional[conditional_access_filter.ConditionalAccessFilter]
        """
        return self._service_principal_filter
    
    @service_principal_filter.setter
    def service_principal_filter(self,value: Optional[conditional_access_filter.ConditionalAccessFilter] = None) -> None:
        """
        Sets the servicePrincipalFilter property value. Filter that defines the dynamic-servicePrincipal-syntax rule to include/exclude service principals. A filter can use custom security attributes to include/exclude service principals.
        Args:
            value: Value to set for the service_principal_filter property.
        """
        self._service_principal_filter = value
    

