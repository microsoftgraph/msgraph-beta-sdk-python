from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

kerberos_sign_on_mapping_attribute_type = lazy_import('msgraph.generated.models.kerberos_sign_on_mapping_attribute_type')

class KerberosSignOnSettings(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new kerberosSignOnSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Internal Application SPN of the application server. This SPN needs to be in the list of services to which the connector can present delegated credentials.
        self._kerberos_service_principal_name: Optional[str] = None
        # The Delegated Login Identity for the connector to use on behalf of your users. For more information, see Working with different on-premises and cloud identities . Possible values are: userPrincipalName, onPremisesUserPrincipalName, userPrincipalUsername, onPremisesUserPrincipalUsername, onPremisesSAMAccountName.
        self._kerberos_sign_on_mapping_attribute_type: Optional[kerberos_sign_on_mapping_attribute_type.KerberosSignOnMappingAttributeType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KerberosSignOnSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: KerberosSignOnSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return KerberosSignOnSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "kerberos_service_principal_name": lambda n : setattr(self, 'kerberos_service_principal_name', n.get_str_value()),
            "kerberos_sign_on_mapping_attribute_type": lambda n : setattr(self, 'kerberos_sign_on_mapping_attribute_type', n.get_enum_value(kerberos_sign_on_mapping_attribute_type.KerberosSignOnMappingAttributeType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def kerberos_service_principal_name(self,) -> Optional[str]:
        """
        Gets the kerberosServicePrincipalName property value. The Internal Application SPN of the application server. This SPN needs to be in the list of services to which the connector can present delegated credentials.
        Returns: Optional[str]
        """
        return self._kerberos_service_principal_name
    
    @kerberos_service_principal_name.setter
    def kerberos_service_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the kerberosServicePrincipalName property value. The Internal Application SPN of the application server. This SPN needs to be in the list of services to which the connector can present delegated credentials.
        Args:
            value: Value to set for the kerberosServicePrincipalName property.
        """
        self._kerberos_service_principal_name = value
    
    @property
    def kerberos_sign_on_mapping_attribute_type(self,) -> Optional[kerberos_sign_on_mapping_attribute_type.KerberosSignOnMappingAttributeType]:
        """
        Gets the kerberosSignOnMappingAttributeType property value. The Delegated Login Identity for the connector to use on behalf of your users. For more information, see Working with different on-premises and cloud identities . Possible values are: userPrincipalName, onPremisesUserPrincipalName, userPrincipalUsername, onPremisesUserPrincipalUsername, onPremisesSAMAccountName.
        Returns: Optional[kerberos_sign_on_mapping_attribute_type.KerberosSignOnMappingAttributeType]
        """
        return self._kerberos_sign_on_mapping_attribute_type
    
    @kerberos_sign_on_mapping_attribute_type.setter
    def kerberos_sign_on_mapping_attribute_type(self,value: Optional[kerberos_sign_on_mapping_attribute_type.KerberosSignOnMappingAttributeType] = None) -> None:
        """
        Sets the kerberosSignOnMappingAttributeType property value. The Delegated Login Identity for the connector to use on behalf of your users. For more information, see Working with different on-premises and cloud identities . Possible values are: userPrincipalName, onPremisesUserPrincipalName, userPrincipalUsername, onPremisesUserPrincipalUsername, onPremisesSAMAccountName.
        Args:
            value: Value to set for the kerberosSignOnMappingAttributeType property.
        """
        self._kerberos_sign_on_mapping_attribute_type = value
    
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
            value: Value to set for the OdataType property.
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
        writer.write_str_value("kerberosServicePrincipalName", self.kerberos_service_principal_name)
        writer.write_enum_value("kerberosSignOnMappingAttributeType", self.kerberos_sign_on_mapping_attribute_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

